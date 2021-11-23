from flask import Flask
from flask_migrate import Migrate

def init_app(app: Flask):
  from app.models.vacinacao import Vacinacao
  Migrate(app, app.db)
      
