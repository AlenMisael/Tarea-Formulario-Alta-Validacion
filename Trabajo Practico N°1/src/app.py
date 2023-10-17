from flask import Flask, render_template, request, redirect, url_for, flash
from config import config
from models.PacienteModel import PacienteModel
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_wtf.csrf import CSRFProtect 
from flask_mail import Mail, Message
from database import db
from models.entities.Paciente import Paciente
import logging

from smtplib import SMTPException
from threading import Thread

from flask import current_app

logger = logging.getLogger(__name__)


app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'alenmisaelmorillomeneses@gmail.com'
app.config['MAIL_PASSWORD'] = 'ctop jtww eqzf bhuo'
app.config['DONT_REPLY_FROM_EMAIL'] = '(John Doe, johndoe@jdoe.com)'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

csrf = CSRFProtect()

basedatos = db.get_connection()

login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
   return PacienteModel.get_by_id(basedatos, id)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
       dni = request.form['dni']
       if not dni.isdigit():
          flash("El DNI debe ser un numero entero.", "error")
          return redirect(url_for('login'))
       paciente = Paciente(0, request.form ['dni'], 0, 0, request.form ['password'], 0, 0, 0, 0, 0, 0)
       logged_user = PacienteModel.login(basedatos, paciente)
       if logged_user != None: 
          if logged_user.contrasenia:
             login_user(logged_user)
             return redirect(url_for('home'))
          else: 
             flash ("Contraseña invalida..", "error")
             return render_template('login.html')
       else: 
        flash ("DNI no encontrado...", "error")
        return render_template('login.html')
    else: 
        return render_template('login.html')


def crear_registro():
   paciente = Paciente(0, request.form['dni'], request.form['nombre'], request.form['apellido'], request.form['password'], 
                       request.form['telefono'], request.form['email'], request.form['domicilio'], 
                       request.form['obraSocial'], request.form['fecha_nacimiento'], request.form['sexo'])
   paciente_registry = PacienteModel.agregar_paciente(basedatos, paciente)
   if paciente_registry == 1: 
      flash("Paciente registrado exitosamente.", "success")
      send_email(subject = 'Bienvenido al centro medico John Doe S.A.', sender = app.config['DONT_REPLY_FROM_EMAIL'],
                    recipients=[paciente.email, ], text_body = f'Hola {paciente.nombre}, bienvenid@ a Flask',
                    html_body=f'<p> Hola <strong> {paciente.nombre}, {paciente.apellido}, </strong>, bienvenid@ a Flask </p>')
   else: 
      flash("Hubo un error al registrar al paciente.", "error")


@app.route('/registro', methods = ['GET', 'POST'])
def registro():
   if request.method == 'POST':
      dni = request.form['dni']
      pacienteExiste = PacienteModel.buscar_paciente(basedatos,dni)
      if (pacienteExiste != None): 
         flash("Paciente con el DNI ingresado ya existe.", "error")
         return render_template('registro.html')
      if not dni.isdigit():
          flash("El DNI debe ser un numero entero.", "error")
          return render_template('registro.html')
      telefono = request.form['telefono']
      if not telefono.isdigit():
          flash("El telefono debe ser un numero entero.", "error")
          return render_template('registro.html')
      password = request.form['password']
      confirm_password = request.form['password2']
      if password != confirm_password:
         flash ("Las contraseñas no coinciden.", "error")
         return render_template('registro.html')
      crear_registro()
      return render_template('registro.html')
   else: 
      return render_template('registro.html')


@app.route('/terminos')
def terminos():
   return render_template('terminos.html')


def _send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except SMTPException:
            logger.exception("Ocurrió un error al enviar el email")



def send_email(subject, sender, recipients, text_body,
               cc=None, bcc=None, html_body=None):
    msg = Message(subject, sender=sender, recipients=recipients, cc=cc, bcc=bcc)
    msg.body = text_body
    if html_body:
        msg.html = html_body
    Thread(target=_send_async_email, args=(current_app._get_current_object(), msg)).start()

@app.route ('/logout')
def logout(): 
   logout_user()
   return redirect (url_for('login'))




@app.route('/home')
@login_required
def home(): 
   return render_template('home.html')


def status_401(error):
   return redirect (url_for('login'))

def status_404(error):
   return "<h1> Pagina no encontrada </h1>", 404


#pg_restore -U postgres -d pacientesALyP < backup.sql Restaurar la base de datos en otro sistema


if  __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)

    app.run(host= '0.0.0.0', port = 5000)