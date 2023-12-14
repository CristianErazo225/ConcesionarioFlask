from flask import Flask
from flask import render_template, request, redirect,Response, session, url_for # Importamos flask y los metodos
from db import obtener_conexion
from datetime import datetime # Para colocar tiempo deal a las imagenes
from flask import send_from_directory #Para obtener informacion de una imagen
import os
from flask_paginate import Pagination
import logging
from flask_login import current_user


app=Flask(__name__)
app.secret_key="develoteca"


#------Conexion a la DB
#mysql = MySQL(app)

# app.config['MYSQL_DATABASE_HOST']='localhost'
# app.config['MYSQL_DATABASE_USER']='root'
# app.config['MYSQL_DATABASE_PASSWORD']=''
# app.config['MYSQL_DATABASE_DB']='sitio'
# mysql.init_app(app)

#----Sitio raiz
@app.route('/')
def inicio():
    return render_template('sitio/index.html')

@app.route('/img/<imagen>')
def imagenes(imagen):
    print(imagen)
    return send_from_directory(os.path.join('templates/sitio/img/'), imagen)

#----automoviles ruta view
@app.route('/autos')
def autos():
    conexion=obtener_conexion() #conectarme con la DB
    cursor=conexion.cursor()
    
    #cursor.execute("SELECT * FROM `autos`")
    #autos=cursor.fetchall()
    #conexion.commit()

    # Contar el número total de registros
    # cursor.execute("SELECT COUNT(id) FROM autos ")
    # count = cursor.fetchone()
    
    count = 12

    # Obtener el número de página actual y la cantidad de resultados por página
    page_num = request.args.get('page', 1, type=int)
    per_page = 4

    # Calcular el índice del primer registro y limitar la consulta a un rango de registros
    start_index = (page_num - 1) * per_page + 1

    querySQL = (f"SELECT id, marca, nombre, imagen "
                f"FROM autos WHERE id >= 1 "
                f"ORDER BY id DESC LIMIT {per_page} OFFSET {start_index - 1}")
    cursor.execute(querySQL)
    autos = cursor.fetchall()

    # Calcular el índice del último registro
    print(type(start_index))
    print(type(per_page))
    print(type(count))
    print(count)

    #end_index = min(int(start_index) + int(per_page), int(count))

    end_index = min(start_index + per_page, count)
    # end_index = start_index + per_page - 1
    if end_index > count:
        end_index = count

    # Crear objeto paginable
    pagination = Pagination(page=page_num, total=count, per_page=per_page,
                            display_msg=f"Mostrando registros {start_index} - {end_index} de un total de <strong>({count})</strong>")
    conexion.commit()


    return render_template('sitio/autos.html', autos=autos, pagination=pagination)

#----Nosotros ruta view
@app.route('/nosotros')
def nosotros():
    return render_template('sitio/nosotros.html')


#----ruta para el admin
@app.route('/admin')
def admin():
    return render_template('admin/index.html')

#---------------------------Login---------------------------------
@app.route('/admin/login2')
def admin_login2():
    return render_template('admin/login2.html')

@app.route('/admin/login2',methods=["GET","POST"])
def admin_login_post2():

    if request.method == 'POST' and 'txtUsuarios' in request.form and 'txtPasswords':
        _usuarios = request.form['txtUsuarios']
        _password = request.form['txtPasswords']

        if _usuarios=="admin" and _password=="123":
            session["login"]=True
            session["usuario"]="Administrador"
            return redirect("/admin")

        conexion=obtener_conexion()
        cursor=conexion.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario = %s AND password = %s", (_usuarios,_password,))
        account = cursor.fetchone()

        if account:
            session["login"]=True
            #session['id'] = account['1']
            session['usuario'] = _usuarios
            # session['usuario'] = account[password]
            logging.info("Usuario: ", session['usuario'], "ha iniciado sesion")
            return redirect("/")
        else:
            return render_template('admin/login2.html', mensaje="Campo Incorrecto")

    return render_template('admin/login2.html')
#---------------------------Login---------------------------------

#---------------------------Registro---------------------------------
@app.route('/admin/register')
def admin_register():
    conexion=obtener_conexion() #conectarme con la DB
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `usuarios`")
    usuarios=cursor.fetchall()
    conexion.commit()

    return render_template('admin/register.html', usuarios=usuarios)

@app.route('/admin/register/guardar', methods=['POST'])
def admin_register_guardar():
    _usuario=request.form['txtUsuarioRegistro']
    _contraseña=request.form['txtPasswordRegistro']
   
    sql="INSERT INTO `usuarios` (`id`, `usuario`, `password`) VALUES (NULL, %s, %s);"
    datos=(_usuario, _contraseña)

    conexion=obtener_conexion() #conectarme con la DB
    cursor=conexion.cursor()
    cursor.execute(sql, datos)
    conexion.commit()
    
    
    return render_template('admin/login2.html')
#--------------------------------------------------------------------

#----ruta para cerrar el admin
@app.route('/admin/cerrar')
def admin_login_cerrar():
    session.clear()
    return redirect('/')

#----ruta para el admin
@app.route('/admin/autos')
def admin_autos():
    conexion=obtener_conexion() #conectarme con la DB
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `autos`")
    autos=cursor.fetchall()
    conexion.commit()
    print(autos)

    return render_template('admin/autos.html', autos=autos)

#----ruta para recepcionar los datos del /admin/autos.html  -----------------------
@app.route('/admin/autos/guardar', methods=['POST'])
def admin_autos_guardar():
    _nombre=request.form['txtNombre']
    _marca=request.form['txtMarca']
    _archivo=request.files['txtImagen']

    #para cargar las imagenes con la hora actual
    tiempo=datetime.now()
    horaActual=tiempo.strftime('%Y%H%M%S')

    if _archivo.filename!="":
        nuevoNombre=horaActual+"_"+_archivo.filename #le pone fecha al archivo cargado
        _archivo.save("templates/sitio/img/"+nuevoNombre) #le pone nombre al archivo cargado

    sql="INSERT INTO `autos` (`id`, `marca`, `nombre`, `imagen`) VALUES (NULL, %s, %s, %s);"
    datos=(_marca,_nombre, nuevoNombre)

    conexion=obtener_conexion() #conectarme con la DB
    cursor=conexion.cursor()
    cursor.execute(sql, datos)
    conexion.commit()

    print(_marca)
    print(_nombre)
    print(_archivo)
    return redirect('/admin/autos')

@app.route('/admin/autos/borrar', methods=['POST'])
def admin_autos_borrar():
    _id=request.form['txtID']
    print(_id)

    conexion=obtener_conexion() #conectarme con la DB
    cursor=conexion.cursor()
    cursor.execute("SELECT imagen FROM `autos` WHERE id=%s",(_id)) #para selecionar un registro y busca la imagen
    auto=cursor.fetchall()# guarda la imagen en auto
    conexion.commit()
    print(auto)

    if os.path.exists("templates/sitio/img"+str(auto[0][0])):# si la imagen existe la borra
        os.unlink("templates/sitio/img"+str(auto[0][0]))

    conexion=obtener_conexion() #conectarme con la DB
    cursor= conexion.cursor()
    cursor.execute("DELETE FROM autos WHERE id=%s",(_id))
    conexion.commit()

    return redirect('/admin/autos')


#---------------------------------------------------Carrito de compras--------------------------------
#----carrito ruta view
@app.route('/carrito')
def carrito():
    conexion=obtener_conexion() #conectarme con la DB
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `productos`")
    productos=cursor.fetchall()
    conexion.commit()
    return render_template('sitio/carrito.html', productos=productos)

#--------------Carrito de compras---------------

@app.route('/guardar_card', methods=['POST'])
def guardar_card():
    if request.method == 'POST':
        # Recupera la información de la card desde el formulario
        id2 = request.form['id2']
        marca = request.form['marca']
        nombre = request.form['nombre']
        imagen = request.form['imagen']

        # Recupera otros campos según sea necesario

        # tiempo=datetime.now()
        # horaActual=tiempo.strftime('%Y%H%M%S')

        # if imagen.filename!="":
        #     nuevoNombre=horaActual+"_"+imagen.filename #le pone fecha al archivo cargado
        #     imagen.save("templates/sitio/img/"+nuevoNombre) #le pone nombre al archivo cargado

        # Obtiene la conexión desde db.py
        conexion = obtener_conexion()

        # Crea un cursor para ejecutar consultas SQL
        with conexion.cursor() as cursor:
            # Ejecuta una consulta SQL para insertar la información en la base de datos
            sql = "INSERT INTO productos (id2, marca, nombre, imagen) VALUES (%s, %s, %s, %s)"
            val = (id, marca, nombre, imagen)
            cursor.execute(sql, val)

        # Guarda los cambios en la base de datos
        conexion.commit()

        # Cierra el cursor y la conexión
        conexion.close()

        # Redirecciona a la página principal después de guardar
       # return redirect(url_for('sitio/autos.html'))
        return redirect('/autos')
    
#--------------Eliminar producto en carrito de compras------------
@app.route('/carrito/borrar', methods=['POST'])
def corrito_borrar():
    _id2=request.form['txtid2']
    print(_id2)

    conexion=obtener_conexion() #conectarme con la DB
    cursor=conexion.cursor()
    cursor.execute("SELECT imagen FROM `productos` WHERE id2=%s",(_id2)) #para selecionar un registro y busca la imagen
    producto=cursor.fetchall()# guarda la imagen en auto
    conexion.commit()

    conexion=obtener_conexion() #conectarme con la DB
    cursor= conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE id2=%s",(_id2))
    conexion.commit()

    return redirect('/carrito')


#----------ERRORES--------
@app.errorhandler(404)
def not_found_endpoint(error):
    return render_template('/errores/404.html',error=error)
    
#----------Logs------------
#DEBUG
#INFO
#WARNING
#ERROR
#CRITICAL
    
# Configuración básica del sistema de registro
logging.basicConfig(filename='app.log', filemode='a', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


 
 


if __name__ =='__main__':
    app.run(debug=True)