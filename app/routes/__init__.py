from app.routes.vacinacao_blueprint import bp_vacina
from flask import Flask

def init_app(app: Flask):
    app.register_blueprint(bp_vacina)