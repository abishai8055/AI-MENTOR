from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import os

class SimilarityEngine:
    def __init__(self):
        self.internships = self.load_internships()
        self.vectorizer = TfidfVectorizer(stop_words='english')
    
    def load_internships(self):
        csv_path = os.path.join('dataset', 'internships.csv')
        if os.path.exists(csv_path):
            return pd.read_csv(csv_path)
        return pd.DataFrame(columns=['title', 'company', 'skills_required', 'description'])
    
    def recommend_internships(self, user_skills, top_n=3):
        if self.internships.empty or not user_skills:
            return []
        
        user_skills_text = ' '.join(user_skills)
        
        all_texts = [user_skills_text] + self.internships['skills_required'].tolist()
        
        tfidf_matrix = self.vectorizer.fit_transform(all_texts)
        
        user_vector = tfidf_matrix[0:1]
        internship_vectors = tfidf_matrix[1:]
        
        similarities = cosine_similarity(user_vector, internship_vectors)[0]
        
        top_indices = similarities.argsort()[-top_n:][::-1]
        
        recommendations = []
        for idx in top_indices:
            if similarities[idx] > 0:
                recommendations.append({
                    'title': self.internships.iloc[idx]['title'],
                    'company': self.internships.iloc[idx]['company'],
                    'skills_required': self.internships.iloc[idx]['skills_required'],
                    'description': self.internships.iloc[idx]['description'],
                    'match_percentage': round(similarities[idx] * 100, 2)
                })
        
        return recommendations
