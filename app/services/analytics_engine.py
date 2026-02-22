from datetime import datetime, timedelta
from collections import defaultdict

class AnalyticsEngine:
    @staticmethod
    def get_weekly_skill_growth(skills):
        weekly_data = defaultdict(int)
        today = datetime.now()
        
        for i in range(7):
            date = today - timedelta(days=i)
            date_key = date.strftime('%a')
            weekly_data[date_key] = 0
        
        for skill in skills:
            skill_date = skill.created_at
            if (today - skill_date).days <= 7:
                date_key = skill_date.strftime('%a')
                weekly_data[date_key] += 1
        
        days_order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        return {
            'labels': days_order,
            'data': [weekly_data.get(day, 0) for day in days_order]
        }
    
    @staticmethod
    def get_skill_strength_radar(skills):
        categories = ['Technical', 'Soft Skills', 'Tools', 'Languages', 'Frameworks']
        
        technical = ['python', 'java', 'javascript', 'c++', 'algorithms']
        soft = ['communication', 'leadership', 'teamwork', 'problem solving']
        tools = ['git', 'docker', 'kubernetes', 'jenkins']
        languages = ['python', 'java', 'javascript', 'typescript', 'go']
        frameworks = ['react', 'angular', 'django', 'flask', 'spring']
        
        skill_names = [s.name.lower() for s in skills]
        
        scores = [
            len([s for s in skill_names if s in technical]) * 20,
            len([s for s in skill_names if s in soft]) * 25,
            len([s for s in skill_names if s in tools]) * 25,
            len([s for s in skill_names if s in languages]) * 20,
            len([s for s in skill_names if s in frameworks]) * 20
        ]
        
        return {
            'labels': categories,
            'data': [min(score, 100) for score in scores]
        }
    
    @staticmethod
    def get_learning_streak(skills):
        if not skills:
            return 0
        
        sorted_skills = sorted(skills, key=lambda x: x.created_at, reverse=True)
        streak = 1
        current_date = sorted_skills[0].created_at.date()
        
        for skill in sorted_skills[1:]:
            skill_date = skill.created_at.date()
            diff = (current_date - skill_date).days
            if diff == 1:
                streak += 1
                current_date = skill_date
            elif diff > 1:
                break
        
        return streak
    
    @staticmethod
    def get_skill_progress(skills, total_target=20):
        current = len(skills)
        percentage = min((current / total_target) * 100, 100)
        return {
            'current': current,
            'target': total_target,
            'percentage': round(percentage, 2)
        }
