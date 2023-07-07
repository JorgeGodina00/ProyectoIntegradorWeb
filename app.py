from flask import Flask, render_template, request, redirect, url_for, flash #importación de librerias
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWWORD']=""
app.config['MYSQL_DB']=""

app.secret_key='mysecretkey'
mysql = MySQL(app)


@app.route('/')
def index():
    return render_template ('index.html')

app.route("/service")
def servicios():
    return render_template ('nuevoservicio.html')
   
@app.route("/historia")
def historia():
    return render_template ('historia.html')

@app.route("/soporte")
def mantenimiento():
    return render_template('soporte.html')

@app.route("/ajustes")
def ajustes():
    return render_template("ajustes.html")

if __name__ == '__main__':
    app.run(debug= True, port= 5900)