from flask import Flask, render_template, request, redirect, url_for, flash #importación de librerias
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route("/")
def principal():
    return render_template ('index.html')

@app.route("/servicios")
def servicos():
    return render_template ('servicios.html')

@app.route("/mantenimiento")
def mantenimiento():
    return render_template('servicio.html')

if __name__ == '__main__':
    app.run()
