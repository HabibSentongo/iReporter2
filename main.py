#this module runs the whole app
from app.views.view import app

if __name__ == "__main__":
    app.run(debug=True)