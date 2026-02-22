class ScoreEngine:
    @staticmethod
    def calculate_career_score(skill_match, internship_similarity, interview_score, skill_completion):
        career_score = (
            (skill_match * 0.40) +
            (internship_similarity * 0.30) +
            (interview_score * 0.20) +
            (skill_completion * 0.10)
        )
        return round(career_score, 2)
    
    @staticmethod
    def get_skill_match_percentage(user_skills_count, required_skills_count):
        if required_skills_count == 0:
            return 0
        return min((user_skills_count / required_skills_count) * 100, 100)
    
    @staticmethod
    def get_skill_completion_rate(user_skills):
        if not user_skills:
            return 0
        total_proficiency = sum([skill.proficiency for skill in user_skills])
        avg_proficiency = total_proficiency / len(user_skills)
        return round(avg_proficiency, 2)
    
    @staticmethod
    def get_score_breakdown(career_score):
        if career_score >= 80:
            return {
                'level': 'Expert',
                'color': '#4ade80',
                'message': 'Outstanding! You are career-ready.'
            }
        elif career_score >= 60:
            return {
                'level': 'Advanced',
                'color': '#60a5fa',
                'message': 'Great progress! Keep improving.'
            }
        elif career_score >= 40:
            return {
                'level': 'Intermediate',
                'color': '#fbbf24',
                'message': 'Good start! Focus on skill gaps.'
            }
        else:
            return {
                'level': 'Beginner',
                'color': '#f87171',
                'message': 'Keep learning! Build your foundation.'
            }
