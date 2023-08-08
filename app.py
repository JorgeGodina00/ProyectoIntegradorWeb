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

@app.route('/servicio')
def servicio():
    return render_template('servicio.html')

@app.route('/acerca')
def acerca():
    return render_template('acerca.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')



@app.route('/infocliente', methods=['POST'])
def newmedico():
    if request.method == 'POST':
        Vnombre= request.form['nametxt']
        Vapellidop= request.form['aptxt']
        Vapellidom= request.form['amtxt']
        Vtelefono= request.form['teltxt']
        Vemail= request.form['emailtxt']
        Vdesc= request.form['desctxt']   
        CS = mysql.connection.cursor() 
        CS.execute("INSERT INTO formulario1 (Nombre, Apellido1, Apellido2, Email, Telefono, Descripcion) VALUES (%s, %s, %s, %s, %s, %s)", (Vnombre, Vapellidop, Vapellidom, Vtelefono, Vemail, Vdesc))
        mysql.connection.commit()
    flash('Se ha hecho el registro correctamente')    
    return redirect(url_for('index'))




if __name__ == '__main__':
    app.run(debug= True, port= 5900)