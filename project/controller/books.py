from project.controller import app


@app.route('/api/v1/books/')
def books():
    return 'Hello, World!'
