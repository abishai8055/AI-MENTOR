from datetime import datetime, timedelta

class RoadmapGenerator:
    @staticmethod
    def generate_roadmap(missing_skills):
        if not missing_skills:
            return []
        
        roadmap = []
        start_date = datetime.now()
        days_per_skill = 14 // len(missing_skills) if len(missing_skills) > 0 else 14
        
        for i, skill in enumerate(missing_skills):
            week_start = start_date + timedelta(days=i * days_per_skill)
            week_end = week_start + timedelta(days=days_per_skill - 1)
            
            roadmap.append({
                'skill': skill,
                'week': f"Days {i * days_per_skill + 1}-{(i + 1) * days_per_skill}",
                'start_date': week_start.strftime('%b %d'),
                'end_date': week_end.strftime('%b %d'),
                'tasks': RoadmapGenerator.get_tasks_for_skill(skill),
                'resources': RoadmapGenerator.get_resources_for_skill(skill)
            })
        
        return roadmap
    
    @staticmethod
    def get_tasks_for_skill(skill):
        return [
            f"Learn {skill} fundamentals",
            f"Complete {skill} tutorial",
            f"Build mini-project using {skill}",
            f"Practice {skill} exercises"
        ]
    
    @staticmethod
    def get_resources_for_skill(skill):
        return [
            f"Online course: {skill} Masterclass",
            f"Documentation: Official {skill} docs",
            f"Practice: {skill} coding challenges"
        ]
