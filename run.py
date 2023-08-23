from app import app
from app.routes import bp

app.register_blueprint(bp,url_prefix="/api/v1")

if __name__ == '__main__':
    app.run(debug=True)