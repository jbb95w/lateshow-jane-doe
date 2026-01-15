from .config import app
from .models import Episode, Guest, Appearance



@app.route('/')
def home():
    return {"message": "Late Show API running"}

if __name__ == '__main__':
    app.run(port=5555, debug=True)
