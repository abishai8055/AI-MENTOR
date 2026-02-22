from app import create_app, db
from werkzeug.serving import run_simple

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    run_simple('127.0.0.1', 5000, app, use_reloader=False, use_debugger=False, threaded=True)
