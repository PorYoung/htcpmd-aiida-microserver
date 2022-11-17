from config import app, api, nacos
from app import hello, endpoint, aiida, system

api.init_app(app=app)

if __name__ == "__main__":
    app.run()
