from ...main import app


@app.route("<int>:post_id")
def index(post_id):
    ...