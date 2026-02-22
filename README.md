# AI Career Mentor Pro

## 🎯 Project Overview

AI Career Mentor Pro is a production-ready, full-stack SaaS web application that leverages artificial intelligence, machine learning, and natural language processing to provide comprehensive career guidance. The platform offers resume analysis, intelligent internship matching, AI-powered interview simulation, skill gap detection, career readiness scoring, growth analytics, an AI chatbot assistant, and automated portfolio generation.

## 🚨 Problem Statement

Modern job seekers and students face multiple challenges:
- **Skill Uncertainty**: Not knowing which skills are in demand
- **Resume Optimization**: Difficulty extracting and showcasing relevant skills
- **Interview Preparation**: Lack of personalized practice and feedback
- **Career Direction**: Unclear path from current skills to dream jobs
- **Progress Tracking**: No systematic way to measure career readiness
- **Portfolio Creation**: Time-consuming manual portfolio building

AI Career Mentor Pro solves all these problems with intelligent automation and personalized guidance.

## ✨ Core Features

### 1. **Resume Analyzer**
- Upload PDF resumes
- Automatic text extraction using PyPDF2
- NLP-based skill extraction with spaCy
- Intelligent skill matching against master database
- Store extracted skills in user profile

### 2. **Intelligent Internship Recommendation Engine**
- TF-IDF vectorization of user skills and job requirements
- Cosine similarity algorithm for precise matching
- Top 3 personalized recommendations with match percentages
- Detailed internship descriptions and requirements

### 3. **Skill Gap Detection**
- Compare user skills vs required skills
- Visual representation of missing skills
- Prioritized skill recommendations
- 2-week learning roadmap generation

### 4. **AI Interview Simulator**
- Role-based interview questions (Software Engineer, Data Scientist, Frontend, Backend)
- 5 technical questions per role
- Real-time answer evaluation using TF-IDF similarity
- Individual question scoring (0-100%)
- Overall interview score calculation
- Personalized feedback and improvement suggestions

### 5. **Career Readiness Score Engine**
Comprehensive scoring algorithm:
```
Career Score = (Skill Match × 40%) + (Internship Similarity × 30%) + 
               (Interview Score × 20%) + (Skill Completion Rate × 10%)
```
- Real-time score updates
- Score breakdown visualization
- Career level classification (Beginner/Intermediate/Advanced/Expert)
- Actionable improvement recommendations

### 6. **Skill Growth Analytics Dashboard**
- **Weekly Learning Graph**: Track skills added over 7 days (Chart.js bar chart)
- **Skill Strength Radar**: Visualize proficiency across 5 categories (Chart.js radar)
- **Learning Streak**: Consecutive days of skill addition
- **Progress Tracking**: Current vs target skill count with circular progress
- **Career Level Badge**: Dynamic level indicator with color coding

### 7. **AI Career Chatbot**
Intelligent rule-based assistant providing:
- Personalized skill recommendations
- Interview preparation guidance
- Internship suggestions
- Career score insights
- Learning roadmap advice
- Portfolio creation tips
Modern chat UI with message bubbles and real-time responses

### 8. **Portfolio Website Generator**
- Auto-generate professional portfolio HTML
- Sections: Hero, About, Skills, Career Stats, Contact
- Modern gradient design with glassmorphism
- Live preview in iframe
- One-click HTML download
- Fully responsive and ready to deploy

## 🏗️ Architecture

### Tech Stack
- **Backend**: Python Flask 3.0 (App Factory Pattern, Blueprints)
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-Login + Flask-Bcrypt (password hashing)
- **ML/NLP**: scikit-learn (TF-IDF, Cosine Similarity), spaCy (en_core_web_sm)
- **PDF Processing**: PyPDF2
- **Frontend**: HTML5, Bootstrap 5, Custom CSS (Glassmorphism)
- **Charts**: Chart.js 4.0
- **Fonts**: Google Fonts (Poppins)
- **Icons**: Font Awesome 6.4
- **Deployment**: Gunicorn-ready, .env support

### Project Structure
```
AI-Career-Mentor/
│
├── app/
│   ├── __init__.py              # App factory, extensions init
│   ├── models.py                # User, Skill, Interview models
│   ├── routes.py                # Main application routes
│   ├── auth.py                  # Authentication routes
│   │
│   └── services/
│       ├── resume_parser.py     # PDF text extraction
│       ├── skill_extractor.py   # NLP skill extraction
│       ├── similarity_engine.py # ML recommendation engine
│       ├── gap_analyzer.py      # Skill gap detection
│       ├── roadmap_generator.py # Learning path creation
│       ├── interview_engine.py  # Interview Q&A evaluation
│       ├── score_engine.py      # Career score calculation
│       ├── analytics_engine.py  # Growth tracking & charts
│       ├── chatbot_engine.py    # AI assistant logic
│       └── portfolio_generator.py # HTML portfolio creation
│
├── dataset/
│   ├── internships.csv          # 10 internship listings
│   ├── skills_master.csv        # 80+ technical skills
│   └── interview_questions.csv  # 20 role-based questions
│
├── templates/
│   ├── base.html                # Base template with navbar
│   ├── home.html                # Landing page
│   ├── login.html               # Login page
│   ├── register.html            # Registration page
│   ├── dashboard.html           # Main dashboard
│   ├── analysis.html            # Internship recommendations
│   ├── interview.html           # Interview simulator
│   ├── analytics.html           # Growth analytics
│   ├── chatbot.html             # AI chatbot interface
│   └── portfolio.html           # Portfolio generator
│
├── static/
│   ├── css/style.css            # Premium glassmorphism CSS
│   └── js/script.js             # Interactive JavaScript
│
├── config.py                    # Configuration settings
├── run.py                       # Application entry point
├── reset_db.py                  # Database reset utility
├── requirements.txt             # Python dependencies
├── Procfile                     # Heroku deployment
├── .env.example                 # Environment variables template
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

## 🤖 Machine Learning Approach

### 1. **TF-IDF Vectorization**
- **Purpose**: Convert text (skills) into numerical vectors
- **How it works**: 
  - Term Frequency: How often a skill appears
  - Inverse Document Frequency: How unique a skill is
  - Creates weighted vectors representing skill importance
- **Implementation**: scikit-learn's TfidfVectorizer
- **Use cases**: Internship matching, answer evaluation

### 2. **Cosine Similarity**
- **Purpose**: Measure similarity between skill vectors
- **Formula**: `similarity = (A · B) / (||A|| × ||B||)`
- **Range**: 0 (no match) to 1 (perfect match)
- **Conversion**: Multiply by 100 for percentage
- **Use cases**: 
  - Internship recommendations (user skills vs job requirements)
  - Interview answer scoring (user answer vs expected keywords)

### 3. **NLP Skill Extraction**
- **Tool**: spaCy (en_core_web_sm model)
- **Process**:
  1. Parse resume text with spaCy
  2. Extract named entities (ORG, PRODUCT, GPE)
  3. Match against curated skill database (80+ skills)
  4. Return matched skills with proper capitalization
- **Fallback**: Keyword matching for non-entity skills

### 4. **Career Score Algorithm**
Weighted multi-factor scoring:
```python
career_score = (
    skill_match * 0.40 +           # 40% weight
    internship_similarity * 0.30 +  # 30% weight
    interview_score * 0.20 +        # 20% weight
    skill_completion * 0.10         # 10% weight
)
```
- **Skill Match**: (user_skills / target_skills) × 100
- **Internship Similarity**: Average cosine similarity
- **Interview Score**: Average question scores
- **Skill Completion**: Average proficiency across skills

## 🎨 UI/UX Design

### Design Philosophy
Premium SaaS-level aesthetic inspired by modern EdTech platforms

### Color Palette
- **Primary Gradient**: #0f2027 → #203a43 → #2c5364
- **Accent Gradient**: #667eea → #764ba2
- **Success**: #4ade80
- **Warning**: #fbbf24
- **Danger**: #f87171

### Design Elements
- **Glassmorphism**: Frosted glass effect with backdrop blur
- **Floating Animation**: Subtle vertical movement (3s loop)
- **Glowing Buttons**: Gradient backgrounds with hover glow
- **Smooth Transitions**: 0.3s ease on all interactions
- **Rounded Corners**: 16-20px border radius
- **Soft Shadows**: Multi-layer shadows for depth
- **Animated Counters**: Number count-up on page load
- **Progress Indicators**: Circular and linear progress bars
- **Chart Visualizations**: Interactive Chart.js graphs

### Typography
- **Font Family**: Poppins (Google Fonts)
- **Weights**: 300 (Light), 400 (Regular), 500 (Medium), 600 (Semi-Bold), 700 (Bold)
- **Hierarchy**: Clear size differentiation for headings and body text

## 📊 Database Schema

### User Model
```python
- id: Integer (Primary Key)
- username: String(80) (Unique)
- email: String(120) (Unique)
- password: String(200) (Hashed with Bcrypt)
- resume_text: Text (Nullable)
- career_score: Float (Default: 0.0)
- interview_score: Float (Default: 0.0)
- created_at: DateTime
- Relationships: skills, interviews
```

### Skill Model
```python
- id: Integer (Primary Key)
- name: String(100)
- user_id: Integer (Foreign Key → User)
- source: String(20) ('manual' or 'extracted')
- proficiency: Integer (Default: 50, Range: 0-100)
- created_at: DateTime
```

### Interview Model
```python
- id: Integer (Primary Key)
- user_id: Integer (Foreign Key → User)
- role: String(100)
- score: Float (0-100)
- answers: Text (JSON serialized)
- created_at: DateTime
```

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- 500MB free disk space

### Step-by-Step Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd AI-Career-Mentor/AI-MENTOR
```

2. **Create virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download spaCy language model**
```bash
python -m spacy download en_core_web_sm
```

5. **Set environment variables**
```bash
# Windows
set SECRET_KEY=your-super-secret-key-change-in-production

# Linux/Mac
export SECRET_KEY=your-super-secret-key-change-in-production
```

6. **Initialize database**
```bash
python reset_db.py
```

7. **Run the application**
```bash
python run.py
```

8. **Access the application**
```
http://localhost:5000
```

## 🚀 Deployment

### Heroku Deployment

1. **Create Procfile** (already included)
```
web: gunicorn run:app
```

2. **Create Heroku app**
```bash
heroku create your-app-name
```

3. **Set environment variables**
```bash
heroku config:set SECRET_KEY=your-production-secret-key
```

4. **Deploy**
```bash
git push heroku main
```

5. **Initialize database**
```bash
heroku run python reset_db.py
```

### AWS/Azure/GCP Deployment

1. **Use Gunicorn as WSGI server**
```bash
gunicorn -w 4 -b 0.0.0.0:8000 run:app
```

2. **Configure reverse proxy (Nginx)**
```nginx
location / {
    proxy_pass http://127.0.0.1:8000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}
```

3. **Set environment variables**
```bash
export SECRET_KEY=production-secret-key
export FLASK_ENV=production
```

4. **Enable HTTPS** with Let's Encrypt or cloud provider SSL

## 📸 Screenshots

[Screenshots will be added here after deployment]

- Landing Page
- Dashboard with Career Score
- Interview Simulator
- Analytics Dashboard
- AI Chatbot
- Portfolio Generator

## 🔒 Security Features

- **Password Hashing**: Bcrypt with salt rounds
- **CSRF Protection**: Flask built-in CSRF tokens
- **SQL Injection Prevention**: SQLAlchemy ORM parameterized queries
- **Session Management**: Secure Flask-Login sessions
- **File Upload Validation**: PDF-only with size limits (16MB)
- **Environment Variables**: Sensitive data in .env files

## 🧪 Testing

### Manual Testing
```bash
python run.py
```
Visit http://localhost:5000 and test all features

### Database Reset
```bash
python reset_db.py
```

## 📝 Usage Guide

1. **Register**: Create account with username, email, password
2. **Login**: Access your personalized dashboard
3. **Upload Resume**: PDF upload for automatic skill extraction
4. **Add Skills**: Manually add additional skills
5. **Get Recommendations**: View top 3 internship matches
6. **Practice Interview**: Select role and answer 5 questions
7. **View Analytics**: Track skill growth and career progress
8. **Chat with AI**: Get personalized career guidance
9. **Generate Portfolio**: Create and download professional portfolio

## 🤝 Contributing

Contributions welcome! Please follow these steps:
1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

Built with ❤️ using Flask, Machine Learning, and Modern Web Technologies

## 🙏 Acknowledgments

- **Flask**: Micro web framework
- **scikit-learn**: Machine learning algorithms
- **spaCy**: Industrial-strength NLP
- **Bootstrap**: Responsive UI components
- **Chart.js**: Beautiful data visualizations
- **Font Awesome**: Icon library

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact: [Your Email]

---

**Note**: This is a fully functional, production-ready application with complete implementation of all features. No placeholder code or pseudo-logic.

**Version**: 1.0.0  
**Last Updated**: 2024
