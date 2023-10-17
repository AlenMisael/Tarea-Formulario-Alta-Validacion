#from utils.DateFormat import DateFormat
from werkzeug.security import check_password_hash
from flask_login import UserMixin

class Paciente( UserMixin ): 

    def __init__(self, id, dni, nombre, apellido, contrasenia, telefono, email, domicilio, obra_social, fecha_nacimiento, sexo) -> None: 
        self.id = id
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.contrasenia = contrasenia
        self.telefono = telefono
        self.domicilio = domicilio
        self.obra_social = obra_social
        self.fecha_nacimiento = fecha_nacimiento
        self.email = email
        self.sexo = sexo

    
    @classmethod
    def check_password (self, hashed_password, password):
        return check_password_hash(hashed_password, password)
    

    