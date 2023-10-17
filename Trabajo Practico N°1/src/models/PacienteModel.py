from .entities.Paciente import Paciente 
from werkzeug.security import generate_password_hash

class PacienteModel():

    @classmethod
    def login(self, db, user):
        try:
            cursor = db.cursor()
            sql = '''SELECT id, dni, nombre, apellido, contrasenia, email, fecha_nacimiento, 
            telefono, obra_social, domicilio, sexo FROM pacientes WHERE 
            dni = %s'''
            cursor.execute(sql, (user.dni,))
            row = cursor.fetchone()
            if row != None: 
                paciente = Paciente(row[0], row[1], row[2], row[3], Paciente.check_password(row[4], user.contrasenia), row[5], row[6], row[7], row[8], row[9], row[10])
                return paciente
            else:
                return None
        except Exception as ex: 
            raise Exception(ex)


    @classmethod
    def buscar_paciente(self, db, dni):
        try:
            cursor = db.cursor()
            sql = '''SELECT id, dni, nombre, apellido, contrasenia, email, fecha_nacimiento, 
            telefono, obra_social, domicilio, sexo FROM pacientes WHERE 
            dni = %s'''
            cursor.execute(sql, (dni,))
            row = cursor.fetchone()
            if row != None: 
                return row
            else:
                return None
        except Exception as ex: 
            raise Exception(ex)



    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.cursor()
            sql = """SELECT id, dni, nombre, apellido, email, fecha_nacimiento, telefono, obra_social, domicilio, 
            sexo FROM pacientes WHERE 
            id = {}""".format(id)

            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None: 
                return Paciente(row[0], row[1], row[2], row[3], None, row[4], row[5], row[6], row[7], row[8], row[9])
            else:
                None
        except Exception as ex: 
            raise Exception(ex)


    @classmethod
    def agregar_paciente(self,db, paciente): 
        try:
            cursor = db.cursor()

            hashed_password = generate_password_hash(paciente.contrasenia)
            cursor.execute("""INSERT INTO pacientes ( dni, nombre, apellido, contrasenia, telefono, email, domicilio, 
                               obra_social, fecha_nacimiento, sexo) VALUES (%s,%s,%s,%s,%s,%s,%s, %s, %s, %s)""",
                    (paciente.dni, paciente.nombre, paciente.apellido, hashed_password, paciente.telefono, paciente.email, paciente.domicilio, paciente.obra_social, 
            paciente.fecha_nacimiento, paciente.sexo) )
            
               
            affected_rows = cursor.rowcount
            db.commit()
            return affected_rows
        except Exception as ex: 
            raise Exception(ex)


