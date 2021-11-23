from flask import Blueprint
from app.controllers.vacinacao_controllers import get_all_users, register_card

bp_vacina = Blueprint("bp_vacina", __name__)

bp_vacina.post("/vaccinations")(register_card)
bp_vacina.get("/vaccinations")(get_all_users)
