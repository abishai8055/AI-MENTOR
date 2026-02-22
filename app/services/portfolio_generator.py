class PortfolioGenerator:
    @staticmethod
    def generate_html(user_data):
        skills_html = ''.join([f'<span class="skill-tag">{skill}</span>' for skill in user_data['skills']])
        
        html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{user_data['username']} - Portfolio</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: #fff; }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 2rem; }}
        .hero {{ text-align: center; padding: 4rem 0; }}
        .hero h1 {{ font-size: 3rem; margin-bottom: 1rem; }}
        .hero p {{ font-size: 1.5rem; opacity: 0.9; }}
        .section {{ background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); border-radius: 20px; padding: 2rem; margin: 2rem 0; }}
        .section h2 {{ font-size: 2rem; margin-bottom: 1rem; border-bottom: 2px solid rgba(255,255,255,0.3); padding-bottom: 0.5rem; }}
        .skills {{ display: flex; flex-wrap: wrap; gap: 1rem; margin-top: 1rem; }}
        .skill-tag {{ background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 20px; font-weight: 600; }}
        .contact {{ text-align: center; }}
        .contact a {{ color: #fff; text-decoration: none; font-size: 1.2rem; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="hero">
            <h1>{user_data['username']}</h1>
            <p>Aspiring Professional | Tech Enthusiast</p>
        </div>
        
        <div class="section">
            <h2>About Me</h2>
            <p>Passionate about technology and continuous learning. Building skills to excel in the tech industry.</p>
        </div>
        
        <div class="section">
            <h2>Skills</h2>
            <div class="skills">
                {skills_html}
            </div>
        </div>
        
        <div class="section">
            <h2>Career Stats</h2>
            <p><strong>Career Readiness Score:</strong> {user_data['career_score']}%</p>
            <p><strong>Total Skills:</strong> {len(user_data['skills'])}</p>
            <p><strong>Interview Score:</strong> {user_data['interview_score']}%</p>
        </div>
        
        <div class="section contact">
            <h2>Contact</h2>
            <p><a href="mailto:{user_data['email']}">{user_data['email']}</a></p>
        </div>
    </div>
</body>
</html>"""
        return html_template
