import sys
import os

# Add the parent directory of 'website' to sys.path so Python can find it
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
# .\env\Scripts\Activate