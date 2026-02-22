import csv
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class InterviewEngine:
    def __init__(self):
        self.questions_db = self.load_questions()
    
    def load_questions(self):
        questions = {}
        csv_path = os.path.join('dataset', 'interview_questions.csv')
        if os.path.exists(csv_path):
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    role = row['role']
                    if role not in questions:
                        questions[role] = []
                    questions[role].append({
                        'question': row['question'],
                        'expected_keywords': row['expected_keywords']
                    })
        return questions
    
    def get_questions_for_role(self, role, count=5):
        if role in self.questions_db:
            return self.questions_db[role][:count]
        return []
    
    def evaluate_answer(self, answer, expected_keywords):
        if not answer or not expected_keywords:
            return 0.0
        
        vectorizer = TfidfVectorizer(stop_words='english')
        try:
            vectors = vectorizer.fit_transform([answer.lower(), expected_keywords.lower()])
            similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
            score = min(similarity * 100, 100)
            return round(score, 2)
        except:
            return 0.0
    
    def calculate_overall_score(self, answers_scores):
        if not answers_scores:
            return 0.0
        return round(sum(answers_scores) / len(answers_scores), 2)
    
    def get_feedback(self, score):
        if score >= 80:
            return "Excellent! You're well-prepared for interviews."
        elif score >= 60:
            return "Good job! Practice more technical concepts."
        elif score >= 40:
            return "Fair performance. Focus on key concepts and practice."
        else:
            return "Needs improvement. Study fundamentals and practice more."
