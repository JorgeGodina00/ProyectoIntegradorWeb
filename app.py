from flask import Flask, render_template, request, redirect, url_for, flash #importación de librerias
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWWORD']=""
app.config['MYSQL_DB']="bd_integrador"

app.secret_key='mysecretkey'

mysql = MySQL(app)


@app.route('/')
def index():
    return render_template ('index.html')
   
@app.route("/historia")
def historia():
    return render_template ('historia.html')

@app.route("/soporte")
def mantenimiento():
    return render_template('soporte.html')

@app.route("/servicios")
def servicios():
    return render_template("nuevoservicio.html")

@app.route("/ajustes")
def ajustes():
    return render_template("ajustes.html")

@app.route('/guardarservicio', methods=['POST'])
def guardar():
    if request.method == 'POST':
        Vcliente= request.form['txtid_cliente']
        Vserv= request.form['txtcve_serv']
        Vcorreo= request.form['txtemail']
        Vtel= request.form['txttel']
        Vfecha= request.form['txtfecha']
        Vcosto= request.form['txtcosto']
        
        
        CS = mysql.connection.cursor() #Variable de tipo cursor que contiene las herramientas paara realizar los querys
        CS.execute("INSERT INTO servicio_cliente(id_cliente, cve_serv, costo, numero, fecha, correo) VALUES (%s, %s, %s, %s, %s, %s)", (Vcliente, Vserv, Vcosto, Vtel, Vfecha, Vcorreo))
        mysql.connection.commit()
       
    return redirect(url_for('index'))

@app.route("/buscar")
def consultar():
    return render_template("buscar.html")

@app.route('/editarservicio/<id>')
def editar(id):  
    curEditar= mysql.connection.cursor()
    curEditar.execute('Select * from  Where id= %s ', (id,))
    consulId= curEditar.fetchone()
    return render_template('editarfruta.html',fruta= consulId)

if __name__ == '__main__':
    app.run(debug= True, port= 5900)