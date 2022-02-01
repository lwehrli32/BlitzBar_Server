from app import app


@app.route("/")
def add_db():
    print("Hello")
    return 'Hello'
