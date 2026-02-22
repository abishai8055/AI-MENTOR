import os
import sys

# Delete old database files
db_files = ['instance/career_mentor.db', 'instance/career.db']
for db_file in db_files:
    if os.path.exists(db_file):
        try:
            os.remove(db_file)
            print(f"Deleted {db_file}")
        except Exception as e:
            print(f"Error deleting {db_file}: {e}")
            print("Please close the Flask server and run this script again.")
            sys.exit(1)

# Create new database
from app import create_app, db

app = create_app()
with app.app_context():
    db.create_all()
    print("Database created successfully with correct schema!")
