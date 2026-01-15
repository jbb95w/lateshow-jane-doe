from .config import app


@app.route('/')
def home():
    return {"message": "Late Show API running"}

if __name__ == '__main__':
    app.run(port=5555, debug=True)
