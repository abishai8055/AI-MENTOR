from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, make_response
from flask_login import login_required, current_user
from app import db
from app.models import Skill, Interview
from app.services.resume_parser import ResumeParser
from app.services.skill_extractor import SkillExtractor
from app.services.similarity_engine import SimilarityEngine
from app.services.gap_analyzer import GapAnalyzer
from app.services.roadmap_generator import RoadmapGenerator
from app.services.interview_engine import InterviewEngine
from app.services.score_engine import ScoreEngine
from app.services.analytics_engine import AnalyticsEngine
from app.services.chatbot_engine import ChatbotEngine
from app.services.portfolio_generator import PortfolioGenerator
import json

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("home.html")

@main.route("/dashboard")
@login_required
def dashboard():
    skills = Skill.query.filter_by(user_id=current_user.id).all()
    skill_count = len(skills)
    
    skill_completion = ScoreEngine.get_skill_completion_rate(skills)
    
    current_user.career_score = ScoreEngine.calculate_career_score(
        skill_match=min(skill_count * 5, 100),
        internship_similarity=50,
        interview_score=current_user.interview_score,
        skill_completion=skill_completion
    )
    db.session.commit()
    
    return render_template("dashboard.html", 
                         user=current_user, 
                         skill_count=skill_count, 
                         skills=skills)

@main.route("/upload-resume", methods=["POST"])
@login_required
def upload_resume():
    if 'resume' not in request.files:
        flash("No file uploaded", "danger")
        return redirect(url_for("main.dashboard"))
    
    file = request.files['resume']
    if file.filename == '':
        flash("No file selected", "danger")
        return redirect(url_for("main.dashboard"))
    
    if file and file.filename.endswith('.pdf'):
        try:
            resume_text = ResumeParser.extract_text_from_pdf(file)
            current_user.resume_text = resume_text
            db.session.commit()
            
            skill_extractor = SkillExtractor()
            extracted_skills = skill_extractor.extract_skills(resume_text)
            
            for skill_name in extracted_skills:
                existing = Skill.query.filter_by(user_id=current_user.id, name=skill_name).first()
                if not existing:
                    skill = Skill(name=skill_name, user_id=current_user.id, source='extracted')
                    db.session.add(skill)
            
            db.session.commit()
            flash(f"Resume uploaded! Extracted {len(extracted_skills)} skills.", "success")
        except Exception as e:
            flash(f"Error processing resume: {str(e)}", "danger")
    else:
        flash("Please upload a PDF file", "danger")
    
    return redirect(url_for("main.dashboard"))

@main.route("/add-skill", methods=["POST"])
@login_required
def add_skill():
    skill_name = request.form.get("skill_name", "").strip()
    if skill_name:
        existing = Skill.query.filter_by(user_id=current_user.id, name=skill_name).first()
        if not existing:
            skill = Skill(name=skill_name, user_id=current_user.id, source='manual')
            db.session.add(skill)
            db.session.commit()
            flash(f"Skill '{skill_name}' added!", "success")
        else:
            flash("Skill already exists", "info")
    return redirect(url_for("main.dashboard"))

@main.route("/delete-skill/<int:skill_id>")
@login_required
def delete_skill(skill_id):
    skill = Skill.query.get_or_404(skill_id)
    if skill.user_id == current_user.id:
        db.session.delete(skill)
        db.session.commit()
        flash("Skill deleted", "success")
    return redirect(url_for("main.dashboard"))

@main.route("/analyze")
@login_required
def analyze():
    skills = Skill.query.filter_by(user_id=current_user.id).all()
    user_skills = [skill.name for skill in skills]
    
    if not user_skills:
        flash("Please add skills or upload resume first", "warning")
        return redirect(url_for("main.dashboard"))
    
    engine = SimilarityEngine()
    recommendations = engine.recommend_internships(user_skills, top_n=3)
    
    analysis_data = []
    for rec in recommendations:
        gaps = GapAnalyzer.analyze_gaps(user_skills, rec['skills_required'])
        roadmap = RoadmapGenerator.generate_roadmap(gaps[:3])
        
        analysis_data.append({
            'internship': rec,
            'gaps': gaps,
            'roadmap': roadmap
        })
    
    return render_template("analysis.html", analysis_data=analysis_data, user_skills=user_skills)

@main.route("/interview")
@login_required
def interview():
    return render_template("interview.html")

@main.route("/start-interview", methods=["POST"])
@login_required
def start_interview():
    role = request.form.get("role")
    engine = InterviewEngine()
    questions = engine.get_questions_for_role(role, count=5)
    
    if not questions:
        flash("No questions available for this role", "warning")
        return redirect(url_for("main.interview"))
    
    return render_template("interview.html", questions=questions, role=role, started=True)

@main.route("/submit-interview", methods=["POST"])
@login_required
def submit_interview():
    role = request.form.get("role")
    answers = []
    scores = []
    
    engine = InterviewEngine()
    questions = engine.get_questions_for_role(role, count=5)
    
    for i, q in enumerate(questions):
        answer = request.form.get(f"answer_{i}", "")
        answers.append(answer)
        score = engine.evaluate_answer(answer, q['expected_keywords'])
        scores.append(score)
    
    overall_score = engine.calculate_overall_score(scores)
    feedback = engine.get_feedback(overall_score)
    
    interview = Interview(
        user_id=current_user.id,
        role=role,
        score=overall_score,
        answers=json.dumps(answers)
    )
    db.session.add(interview)
    
    current_user.interview_score = overall_score
    db.session.commit()
    
    return render_template("interview.html", 
                         completed=True, 
                         overall_score=overall_score,
                         scores=scores,
                         feedback=feedback,
                         questions=questions,
                         answers=answers)

@main.route("/analytics")
@login_required
def analytics():
    skills = Skill.query.filter_by(user_id=current_user.id).all()
    
    weekly_growth = AnalyticsEngine.get_weekly_skill_growth(skills)
    skill_radar = AnalyticsEngine.get_skill_strength_radar(skills)
    learning_streak = AnalyticsEngine.get_learning_streak(skills)
    skill_progress = AnalyticsEngine.get_skill_progress(skills)
    
    score_breakdown = ScoreEngine.get_score_breakdown(current_user.career_score)
    
    return render_template("analytics.html",
                         weekly_growth=weekly_growth,
                         skill_radar=skill_radar,
                         learning_streak=learning_streak,
                         skill_progress=skill_progress,
                         score_breakdown=score_breakdown)

@main.route("/chatbot")
@login_required
def chatbot():
    return render_template("chatbot.html")

@main.route("/chat", methods=["POST"])
@login_required
def chat():
    message = request.json.get("message", "")
    skills = Skill.query.filter_by(user_id=current_user.id).all()
    
    user_data = {
        'username': current_user.username,
        'career_score': current_user.career_score,
        'interview_score': current_user.interview_score,
        'missing_skills': []
    }
    
    response = ChatbotEngine.get_response(message, user_data)
    return jsonify({'response': response})

@main.route("/portfolio")
@login_required
def portfolio():
    skills = Skill.query.filter_by(user_id=current_user.id).all()
    
    user_data = {
        'username': current_user.username,
        'email': current_user.email,
        'skills': [s.name for s in skills],
        'career_score': current_user.career_score,
        'interview_score': current_user.interview_score
    }
    
    portfolio_html = PortfolioGenerator.generate_html(user_data)
    
    return render_template("portfolio.html", portfolio_preview=portfolio_html)

@main.route("/download-portfolio")
@login_required
def download_portfolio():
    skills = Skill.query.filter_by(user_id=current_user.id).all()
    
    user_data = {
        'username': current_user.username,
        'email': current_user.email,
        'skills': [s.name for s in skills],
        'career_score': current_user.career_score,
        'interview_score': current_user.interview_score
    }
    
    portfolio_html = PortfolioGenerator.generate_html(user_data)
    
    response = make_response(portfolio_html)
    response.headers['Content-Type'] = 'text/html'
    response.headers['Content-Disposition'] = f'attachment; filename={current_user.username}_portfolio.html'
    
    return response
