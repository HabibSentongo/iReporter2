#this module runs the whole app
from api.views.view import app

if __name__ == "__main__":
    app.run(debug=False)