from flask import Flask


def create_app():
  app = Flask(__name__)


  @app.route("/")
  def index():
    return "<h1/>HELLO BITCH</h1>"

  with app.app_context():

    app.config.from_object('config.Config')
    return app