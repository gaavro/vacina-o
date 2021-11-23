from flask import request, current_app, jsonify
from app.models.vacinacao import Vacinacao
from exceptions.exceptions import InvalidCPFError, InvalidKeyError, InvalidTypeError, InvalidUniqueKeyError

def register_card():
   
    data = request.get_json()
    
    try:
        Vacinacao.validate(data)
        formatted_data = {k: v.upper() for k,v in data.items()}
        valid_args = ["cpf", "name", "vaccine_name", "health_unit_name"]
        for i in list(formatted_data.keys()):
            if i not in valid_args:
                del formatted_data[i]
        
        vacina = Vacinacao(**formatted_data)
        current_app.db.session.add(vacina)
        current_app.db.session.commit()
        return {
            "cpf": vacina.cpf,
            "name": vacina.name,
            "first_shot_date": vacina.first_shot_date,
            "second_shot_date": vacina.second_shot_date,
            "vaccine_name": vacina.vaccine_name,
            "health_unit_name": vacina.health_unit_name
        }, 201
    except InvalidCPFError:
        return {"message": "CPF inválido. Insira apenas os 11 números."}, 400
    except InvalidKeyError:
        return {"message": "Campos inválidos ou inexistentes"}, 400
    except InvalidTypeError:
        return {"message": "Formato de dados inválido"}, 400
    except InvalidUniqueKeyError:
        return {"message": "O CPF já existe"}, 409


       
def get_all_users():
    return jsonify(Vacinacao.query.all()), 200