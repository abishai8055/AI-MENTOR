class GapAnalyzer:
    @staticmethod
    def analyze_gaps(user_skills, required_skills_text):
        user_skills_lower = [skill.lower() for skill in user_skills]
        
        required_skills = [s.strip().lower() for s in required_skills_text.split(',')]
        
        missing_skills = [skill for skill in required_skills if skill not in user_skills_lower]
        
        return [skill.title() for skill in missing_skills]
    
    @staticmethod
    def calculate_match_percentage(user_skills, required_skills_text):
        user_skills_lower = set([skill.lower() for skill in user_skills])
        required_skills = set([s.strip().lower() for s in required_skills_text.split(',')])
        
        if not required_skills:
            return 0
        
        matched = len(user_skills_lower.intersection(required_skills))
        return round((matched / len(required_skills)) * 100, 2)
