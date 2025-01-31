from app import *
"""
Calls create_app() function and sets environment variables
"""

app = create_app()
if __name__ == '__main__':
    app.run(debug=True)