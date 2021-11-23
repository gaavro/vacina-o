from datetime import datetime, timedelta
from app.configs.database import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import ( NULLTYPE, String, DateTime)
from dataclasses import dataclass

from exceptions.exceptions import InvalidCPFError, InvalidKeyError, InvalidTypeError, InvalidUniqueKeyError, MissingOneKey, anotherKeyError


a = timedelta(days=90 )
b = datetime.now()


@dataclass
class Vacinacao(db.Model):
    cpf: str
    name: str
    vaccine_name:str
    health_unit_name:str
    first_shot_date:int
    second_shot_date:int

    __tablename__ = "vaccine_cards"

    cpf = Column(String, primary_key=True)

    name = Column(String, nullable=False)
    first_shot_date = Column(db.DateTime, default=datetime.utcnow)
    second_shot_date = Column(db.DateTime, default=a+b)
    vaccine_name = Column(String, nullable=False )
    health_unit_name = Column(String, nullable=False)   


    @staticmethod
    def validate(data):
        required_keys= ["cpf", "name", "vaccine_name", "health_unit_name"]
        for item in required_keys:
            if item not in data.keys():
                raise InvalidKeyError
        for item in data:
            if type(item) is not str:
                raise InvalidTypeError
            
        if len(data["cpf"]) != 11:
            raise InvalidCPFError
        unique_key = (
            Vacinacao
            .query
            .filter(Vacinacao.cpf==data["cpf"])
            .one_or_none()
        )
        if unique_key is not None:
            raise InvalidUniqueKeyError
    
    
        
      