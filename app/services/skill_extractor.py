import spacy
import os
import csv

class SkillExtractor:
    def __init__(self):
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except:
            self.nlp = None
        self.skill_database = self.load_skills()
    
    def load_skills(self):
        skills = set()
        csv_path = os.path.join('dataset', 'skills_master.csv')
        if os.path.exists(csv_path):
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    skills.add(row['skill'].lower())
        return skills
    
    def extract_skills(self, text):
        text_lower = text.lower()
        found_skills = set()
        
        for skill in self.skill_database:
            if skill in text_lower:
                found_skills.add(skill.title())
        
        if self.nlp:
            doc = self.nlp(text)
            for ent in doc.ents:
                if ent.label_ in ['ORG', 'PRODUCT', 'GPE']:
                    skill_candidate = ent.text.lower()
                    if skill_candidate in self.skill_database:
                        found_skills.add(ent.text.title())
        
        return list(found_skills)
