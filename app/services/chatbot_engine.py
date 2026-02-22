class ChatbotEngine:
    @staticmethod
    def get_response(message, user_data):
        message_lower = message.lower()
        
        if any(word in message_lower for word in ['hello', 'hi', 'hey']):
            return f"Hello {user_data['username']}! How can I help you with your career today?"
        
        elif any(word in message_lower for word in ['skill', 'learn', 'improve']):
            if user_data['missing_skills']:
                skills = ', '.join(user_data['missing_skills'][:3])
                return f"Based on your profile, I recommend learning: {skills}. These skills will boost your career prospects!"
            return "Great! Keep adding more skills to your profile. Focus on in-demand technologies."
        
        elif any(word in message_lower for word in ['interview', 'practice']):
            if user_data['interview_score'] < 60:
                return "Your interview score needs improvement. Practice with our AI Interview Simulator to boost your confidence!"
            return "You're doing well in interviews! Keep practicing to maintain your edge."
        
        elif any(word in message_lower for word in ['internship', 'job', 'opportunity']):
            return "Check out the Analysis page for personalized internship recommendations based on your skills!"
        
        elif any(word in message_lower for word in ['score', 'readiness']):
            score = user_data['career_score']
            if score >= 70:
                return f"Your career readiness score is {score}%. Excellent! You're on the right track."
            else:
                return f"Your career readiness score is {score}%. Focus on building skills and practicing interviews."
        
        elif any(word in message_lower for word in ['roadmap', 'plan', 'guide']):
            return "I can help you create a personalized learning roadmap! Visit the Analysis page to see skill gaps and recommended learning paths."
        
        elif any(word in message_lower for word in ['portfolio', 'website']):
            return "Create a stunning portfolio website to showcase your skills! Visit the Portfolio page to generate yours."
        
        elif any(word in message_lower for word in ['help', 'what can you do']):
            return """I can help you with:
• Skill recommendations
• Interview preparation tips
• Career readiness insights
• Learning roadmap guidance
• Internship suggestions
Just ask me anything!"""
        
        else:
            return "I'm here to help with your career! Ask me about skills, interviews, internships, or your career score."
