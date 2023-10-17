# Primer Trabajo Practico de la materia Aspectos Legales y Profesionales

## Profesores 
- Consentino, Guillermo
- Zappellini, Bruno

## Carrera
Licenciatura en Sistemas

## Materia
Aspectos Legales y Profesionales

## Alumno
Morillo Meneses, Alen Misael 

## Universidad
Universidad Nacional de la Patagonia San Juan Bosco (UNPSJB)

## Localidad
Trelew

## Introduccion
En este primer trabajo practico se realizó una aplicacion web para la empresa John Doe S.A. mediante el uso del framework Flask. Esta aplicacion se trata de un registro de datos personales para aquellos pacientes de la empresa. Ademas de contar con un registro, tambien cuenta con un Login para ingresar el numero de documento y la contraseña y un apartado para poder leer los términos y condiciones de la pagina. Al momento de loguearse, se ingresará a una página que le dará la bienvenida al cliente y luego se permitirá cerrar sesion. 
  Todo lo expresado se hizo teniendo en cuenta la ley 25326 sobre Proteccion de Datos Personales, donde uno de los apartados indica que los datos a solicitar en el registro no sean datos sensibles (sobre religión, orientación sexual, partido politico, etc). 


## Programas necesarios para poder usar la aplicacion web
Para poder usar la aplicacion web se requerirá instalar lo siguiente: 
- Docker
- Python
- PostgreSQL 13
- pgAdmin4
- Visual Studio Code

## Como se usa
Para poder usar la aplicacion web se deben realizar los siguientes pasos:
1. Clonar el repositorio actual en la carpeta a su elección. Para ello se debe escribir en la consola de Visual Studio Code lo siguiente:
   '''
   git clone https://github.com/AlenMisael/Tarea-Formulario-Alta-Validacion
   '''
2. Iniciar el docker engine.
3. Ingresar a Trabajo Practico N°1 mediante la terminal y escribir en la consola:
   '''
   docker-compose up
   '''
4. Abrir un navegador e ingresar a localhost:5000.
5. En caso de que al momento de loguearse se produzca una excepción, ingresar al Docker Desktop, ingresar a la imagen que se llama db y dirigirse a la pestaña Terminal. Dentro de terminal ingresar lo siguiente:
   '''
   pg_restore -U postgres -d pacientesALyP < backup.sql
   '''
6. Probar la aplicación web.
  
  


