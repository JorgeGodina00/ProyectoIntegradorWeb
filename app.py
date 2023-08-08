from flask import Flask, render_template, request, redirect, url_for, flash #importación de librerias
from flask_mysqldb import MySQL

app = Flask(__name__)

#BD
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWWORD']=""
app.config['MYSQL_DB']="proyecto"

app.secret_key='mysecretkey'

mysql = MySQL(app)

#Rutas

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/servicio')
def servicio():
    return render_template('servicio.html')

@app.route('/acerca')
def acerca():
    return render_template('acerca.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')
if __name__ == '__main__':
    app.run(debug= True, port= 5900)