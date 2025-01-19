from flask import Flask,render_template,request, url_for,send_file
from werkzeug.utils import secure_filename
from sqlalchemy import text
from conexion import engine,Session
import os,fitz
from PIL import Image

app = Flask(__name__)
#Pagina principal
@app.route('/')
def index():
    return render_template('index.html')
#Formulario de login del estudiante
@app.route('/loginEstudiante2')
def loginEstudiante2():
    return render_template('/login/loginEstudiante2.html')
#Formulario de login del asesor academico
@app.route('/loginAsesorAcademico2')
def loginAsesorAcademico2():
    return render_template('/login/loginAsesorAcademico2.html')
#Formulario de login del coordinador
@app.route('/loginCoordinacion2')
def loginCoordinacion2():
    return render_template('login/loginCoordinacion2.html')
#Formulario de login del coordinador alternativo para uso de otra pagina
@app.route('/loginCoordinacionv2')
def loginCoordinacionv2():
    return render_template('login/loginCoordinacionv2.html')
#Validacion de login del estudiante
@app.route('/iniciarSesionEstudiante',methods=['POST'])
def loginEstudiante():
    matricula= request.form['matricula']
    correo= request.form['correo']
    resultado = inicioSesionEstudiante(matricula,correo) #Llamada a la funcion de inicio de sesion que nos reedirige a la pagina de principal del estudiante
    return resultado


#Editar el perfil del estudiante juasjuas
@app.route('/editarEstudiante', methods=['GET', 'POST'])
def editarEstudiante():
    return render_template('perfiles/EditarEstudiante/editarEstudiante.html')
    # try:
    #     query = text("SELECT Matricula, Nombre1, Nombre2, ApellidoP, ApellidoM, Telefono, Correo FROM estudiante WHERE Matricula = :matricula")
    #     with engine.connect() as conn:
    #         estudiante = conn.execute(query, {'matricula': matricula}).fetchone()
    #         if estudiante:
    #             return render_template(
    #                 'perfiles/EditarEstudiante/editarEstudiante.html',
    #                 Matricula=estudiante[0],
    #                 Nombre1=estudiante[1],
    #                 Nombre2=estudiante[2],
    #                 ApellidoP=estudiante[3],
    #                 ApellidoM=estudiante[4],
    #                 Telefono=estudiante[5],
    #                 Correo=estudiante[6]
    #             )
    #         else:
    #             # Mensaje de error al usuario
    #             return 'Estudiante no encontrado', 404
    # except Exception as e:
    #     # Mensaje de error al usuario
    #     return f'Error: {e}', 500


#Actualizar el perfil del estudiante
@app.route('/ActualizarEstudiante', methods=['POST'])
def actualizar_estudiante():
    try:
        data = {
            'matricula': request.form['matricula'],
            'nombre': request.form['nombre'],
            'apellidos': request.form['apellidos'],
            'telefono': request.form['telefono'],
            'correo': request.form['correo']
        }
        nombres = data['nombre'].split()
        apellidos = data['apellidos'].split()
        
        query = text("""
            UPDATE estudiante 
            SET Nombre1 = :nombre1, Nombre2 = :nombre2, ApellidoP = :apellidoP, ApellidoM = :apellidoM, 
                Telefono = :telefono, Correo = :correo 
            WHERE Matricula = :matricula
        """)
        with engine.connect() as conn:
            conn.execute(query, {
                'nombre1': nombres[0],
                'nombre2': nombres[1] if len(nombres) > 1 else '',
                'apellidoP': apellidos[0],
                'apellidoM': apellidos[1] if len(apellidos) > 1 else '',
                'telefono': data['telefono'],
                'correo': data['correo'],
                'matricula': data['matricula']
            })
            Flask('Datos actualizados exitosamente.', 'success')
            return (url_for('editar_estudiante', matricula=data['matricula']))
    except Exception as e:
        Flask(f'Error al actualizar los datos: {e}', 'danger')
        return ('/')


#Validacion del login de coordinacion
@app.route('/logincoordinacion',methods=['POST'])
def logincoordinacion():
    correo = request.form['correo']
    password = request.form['password']
    resultado = inicioSesionCoordinacion(correo,password) #Llamada a la funcion de inicio de sesion que nos reedirige a la pagina de principal del coordinador
    return resultado
#Validacion del login de coordinacion alternativo que usa otra pagina al login principal
@app.route('/logincoordinacion2',methods=['POST'])
def logincoordinacion2():
    correo = request.form['correo']
    password = request.form['password']
    resultado = inicioSesionCoordinacion2(correo,password)#Llamada a la funcion de inicio de sesion que nos reedirige a la pagina de principal del coordinador
    return resultado
#Funcion para guardar los datos del formulario de registro de proyecto, equipos etc
@app.route('/guardartodo',methods=['POST'])
def guardartodo():
    titulo = request.form['titulocuestionario']
    funcion = request.form['FuncionProyecto']
    numero = request.form['numintegrantes']
    asesorA = request.form['AsesorAcademico']
    asesorE = request.form['AsesorEmpresarial']
    if numero == '1': #Se ejecuta si el equipo tiene 1 integrante
        matricula = request.form['estudiante-0-campo1']
        agregarproyectos(titulo,funcion) #Se agrega el proyecto a la base de datos
        ID = cargarIDProyecto(titulo) #Se obtiene el ID del proyecto que se acaba de agregar
        equipo = cargarEquipoMaximo() #Se obtiene el numero del ultimo equipo agregado +1
        ok = guardarEquipo(matricula,equipo,ID) #Se guarda el equipo en la base de datos si todo es correcto
        guardarProyectoAsesores(ID,asesorE,asesorA) #Se asignan los asesores al proyecto
        if ok != True: #Si hay un error se redirige a la pagina de error
            return render_template('Error/Error.html',ID=ok) #Se redirige a la pagina de error con el ID del proyecto para identifcar el proyecto y se borre
        return render_template('Cargas/cargaEquipo.html') #Pagina de carga de error
    if numero == '2': #Se ejecuta si el equipo tiene 2 integrantes
            matricula = request.form['estudiante-0-campo1']
            matricula2 = request.form['estudiante-1-campo1']
            agregarproyectos(titulo,funcion)
            ID = cargarIDProyecto(titulo)
            equipo = cargarEquipoMaximo()
            ok= guardarEquipo2(matricula,matricula2,equipo,ID)
            guardarProyectoAsesores(ID,asesorE,asesorA)
            if ok != True:
                return render_template('Error/Error.html',ID=ok)
            return render_template('Cargas/cargaEquipo.html')
    elif numero == '3': #Se ejecuta si el equipo tiene 3 integrantes
        matricula = request.form['estudiante-0-campo1']
        matricula2 = request.form['estudiante-1-campo1']
        matricula3 = request.form['estudiante-2-campo1']
        agregarproyectos(titulo,funcion)
        ID = cargarIDProyecto(titulo)
        equipo = cargarEquipoMaximo()
        ok = guardarEquipo3(matricula,matricula2,matricula3,equipo,ID)
        guardarProyectoAsesores(ID,asesorE,asesorA)
        if ok != True:
            return render_template('Error/Error.html',ID=ok)
        return render_template('Cargas/cargaEquipo.html')
    elif numero == '4': #Se ejecuta si el equipo tiene 4 integrantes
        matricula = request.form['estudiante-0-campo1']
        matricula2 = request.form['estudiante-1-campo1']
        matricula3 = request.form['estudiante-2-campo1']
        matricula4 = request.form['estudiante-3-campo1']
        agregarproyectos(titulo,funcion)
        ID = cargarIDProyecto(titulo)
        equipo = cargarEquipoMaximo()
        ok= guardarEquipo4(matricula,matricula2,matricula3,matricula4,equipo,ID)
        guardarProyectoAsesores(ID,asesorE,asesorA)

        if ok != True:
            return render_template('Error/Error.html',ID=ok)
        return render_template('Cargas/cargaEquipo.html')
    elif numero == '5': #Se ejecuta si el equipo tiene 5 integrantes
        matricula = request.form['estudiante-0-campo1']
        matricula2 = request.form['estudiante-1-campo1']
        matricula3 = request.form['estudiante-2-campo1']
        matricula4 = request.form['estudiante-3-campo1']
        matricula5 = request.form['estudiante-4-campo1']
        agregarproyectos(titulo,funcion)
        ID = cargarIDProyecto(titulo)
        equipo = cargarEquipoMaximo()
        ok= guardarEquipo5(matricula,matricula2,matricula3,matricula4,matricula5,equipo,ID)
        guardarProyectoAsesores(ID,asesorE,asesorA)
        if ok != True:
            return render_template('Error/Error.html',ID=ok)
        return render_template('Cargas/cargaEquipo.html')
#Funcion para subir los documentos del estudiante
@app.route('/enviarDocumentos', methods=['POST'])
def enviarDocumentos():
    parcial = request.form['parcialR']
    nombre = request.form['nombre']
    proyectoN = request.form['proyectoR']
    cartas = request.files.get('cartas')
    proyecto = request.files.get('proyecto')
    evaluacion = request.files.get('evaluacion3')
    matricula = request.form['matricula']
    correo = request.form['correo']
    if parcial != "":
        if cartas is None and proyecto is None: #Se valida si la carta y el proyecto estan vacios
            validar = request.form['validar']
            if validar == "False":
                return render_template('error/errorValidar.html', matricula=matricula,correo=correo)
            ruta_03 = guardar03(evaluacion,parcial,nombre,matricula) #Se obtiene la ruta del archivo 03
            guardarRuta03(matricula,ruta_03,parcial) #Se guarda la ruta del archivo 03 en la base de datos
        if proyecto is None and evaluacion is None: #Se valida si el proyecto y la evaluacion estan vacios
            ruta_carta = guardarCartas(cartas,parcial,nombre,matricula) #Se obtiene la ruta de la carta
            guardarCartass(matricula,ruta_carta,parcial)#Se guarda la ruta de la carta en la base de datos
        if cartas is None and evaluacion is None:#Se valida si la carta y la evaluacion estan vacios
            validar = request.form['validar']
            if validar == "False":
                return render_template('error/errorValidar.html', matricula=matricula,correo=correo)
            ruta_proyecto = guardarProyectos(proyecto,parcial,nombre,matricula)#Se obtiene la ruta del proyecto
            guardarRutaDocumentos(matricula,ruta_proyecto,parcial,proyectoN)#Se guarda la ruta del proyecto en la base de datos
    else:
        return render_template('error/errorParcial.html', matricula=matricula,correo=correo) #Se redirige a la pagina de carga que luego nos redirige

    return render_template('cargas/carga.html', matricula=matricula,correo=correo) #Se redirige a la pagina de carga que luego nos redirige
#Funcion para cargar los asesores
@app.route('/agregar',methods=['POST'])
def agregar():
    opcion = cargarAsesorEmp()
    asesorAcademico = cargarAsesorAcademico()
    return render_template('/Agregar.html',cargar = opcion, asesorAcademic = asesorAcademico)

@app.route('/asignarEquipo',methods=['POST'])
def asignarEquipo():
    opcion = cargarAsesorEmp()
    asesorAcademico = cargarAsesorAcademico()
    return render_template('/Agregar.html',cargar = opcion, asesorAcademic = asesorAcademico)

@app.route('/borrarID',methods=['POST'])
def borrarID():
    ID = request.form['ID']
    borrarIDproyecto(ID)
    opcion = cargarAsesorEmp()
    asesorAcademico = cargarAsesorAcademico()
    return render_template('/Agregar.html',cargar = opcion, asesorAcademic = asesorAcademico) 
#Funcion para cargar la pagina de cuestionario de satisfaccion
@app.route('/encuestaSatisfaccion',methods=['POST'])
def encuestaSatisfaccion():
    Matricula = request.form['Matricula']
    Correo = request.form['correo']
    return render_template('Cuestionarios/evaluacion_cuestionario.html',Matricula = Matricula,correo = Correo)
#Funcion para obtener los datos del cuestionario de satisfaccion
@app.route('/EvalulacionEstudiante',methods=['POST'])
def enviarEvaluacionEstudiante():
    matricula = request.form['Matricula']
    correo = request.form['correo']
    question11 = int(request.form['question11'])
    question12 = int(request.form['question12'])
    question13 = int(request.form['question13'])
    question14 = int(request.form['question14'])
    question15 = int(request.form['question15'])
    question16 = int(request.form['question16'])
    question17 = int(request.form['question17'])
    question18 = int(request.form['question18'])
    question19 = int(request.form['question19'])
    veracidad = request.form['veracidad']  
    prom = promedio(question11,question12,question13,question14,question15,question16,question17,question18,question19)
    guardarForm08(prom,veracidad,matricula)
    return render_template('Cargas/EnvioEvaluacionEstudiante.html',matricula = matricula,correo = correo)

@app.route('/loginAsesorAcademico',methods=['POST'])
def loginAsesorAcademico():
    correo = request.form['correo']
    password = request.form['password']
    resultado = inicioSesionAsesorA(correo,password)
    return resultado
#Funcion para cargar la pagina de revisar expediente
@app.route('/AbrirExpediente',methods=['POST'])
def AbrirExpediente():
    nombre_completo = request.form['nombre']
    telefono = request.form['telefono']
    correo = request.form['correo']
    ID = request.form['ID']
    partes = nombre_completo.split()
    nombre1,nombre2,apellidop,apellidom = partes
    resultado = cargarProyectosAsesor(ID)
    return render_template('/perfiles/AsesorAcademico/revisar_expediente.html',Nombre1 = nombre1,Nombre2 = nombre2,ApellidoP = apellidop,ApellidoM = apellidom,Telefono = telefono,Correo = correo,resultado = resultado)

@app.route('/verArchivo',methods=['POST'])
def abrirExpediente():
    parcial = request.form['parcialB']
    proyecto = request.form['proyecto']
    ruta = obtenerRutaPDF(proyecto,parcial)    
    imagen = visualizarPDF(ruta)
   
    return render_template('perfiles/AsesorAcademico/abrirExpediente.html',parcial = parcial,proyecto = proyecto,imagen = imagen)

@app.route('/calificarExpediente',methods=['POST'])
def calificarExpediente():
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    correo = request.form['correo']
    proyecto = request.form['proyectoC']
    ID = IDproyecto(proyecto)
    estudiantes = obtenerMatricula(ID)
    return render_template('perfiles/AsesorAcademico/calificar_expediente.html',nombre = nombre,telefono = telefono,correo = correo,proyecto= proyecto,estudiantes=estudiantes)


@app.route('/calificarSer',methods=['POST'])
def calificarSer():
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    correo = request.form['correo']
    return render_template('perfiles/AsesorAcademico/calificar_ser.html',nombre = nombre,telefono = telefono,correo = correo)

@app.route('/descargarPdf',methods=['POST'])
def descargaPdf():
    proyecto = request.form['proyecto']
    parcial = request.form['parcial']
    ruta = obtenerRutaPDF(proyecto,parcial)
    return descargarPDF(ruta)

@app.route('/Regresar',methods=['POST'])
def regresar():
    matricula = request.form['matricula']
    correo = request.form['correo']
    return inicioSesionEstudiante(matricula,correo)

def inicioSesionEstudiante(matricula,correo):
    proyecto = cargarProyectoAlumno(matricula)
    asesor = cargarAsesorEmpresarial(proyecto)
    try:
        query = text("SELECT Matricula,Nombre1,Nombre2,ApellidoP,ApellidoM,Telefono,Correo FROM estudiante WHERE matricula = :matricula AND correo =:correo")
        with engine.connect() as conn:
            ok= conn.execute(query, {'matricula': matricula,'correo':correo}).fetchone()
            if ok:
                Matricula = ok[0]
                Nombre1 = ok[1]
                Nombre2 = ok[2]
                ApellidoP = ok[3]
                ApellidoM = ok[4]
                Telefono = ok[5]
                Correo = ok[6]
                validar = verificarAsignacionProyecto(matricula)
                return render_template('/perfiles/evaluacionEstudiante.html',Matricula=Matricula,Nombre1=Nombre1,Nombre2=Nombre2,ApellidoM=ApellidoM,ApellidoP=ApellidoP,Telefono=Telefono,Correo=Correo,proyecto = proyecto,asesor=asesor,validar= validar)
            else:
                return 'no encontado'
    except Exception as e:
            return f'error {e}'
    
def inicioSesionCoordinacion(correo,password):
    try:
        query = text("SELECT Nombre,Nombre2,ApellidoP,ApellidoM,Correo,password FROM coordinacion WHERE correo = :correo AND password =:password")
        with engine.connect() as conn:
            ok= conn.execute(query, {'correo': correo,'password':password}).fetchone()
            if ok:
                nombre=ok[0]
                nombre2=ok[1]
                apellidoP=ok[2]
                apellidoM=ok[3]
                return render_template('/perfil_coordinacion.html',nombre = nombre,nombre2 = nombre2,apellidoP=apellidoP,apellidoM=apellidoM,correo=correo)
            else:
                return 'no encontado'
    except Exception as e:
            return f'{e}'
    
def inicioSesionCoordinacion2(correo,password):
    opcion = cargarAsesorEmp()
    asesorAcademico = cargarAsesorAcademico()
    try:
        query = text("SELECT Nombre,Nombre2,ApellidoP,ApellidoM,Correo,password FROM coordinacion WHERE correo = :correo AND password =:password")
        with engine.connect() as conn:
            ok= conn.execute(query, {'correo': correo,'password':password}).fetchone()
            if ok:
                return render_template('/Agregar.html',cargar = opcion, asesorAcademic = asesorAcademico)
            else:
                return 'no encontado'
    except Exception as e:
            return f'{e}'

def agregarproyectos(titulo,funcion):
    try:
        query = text("INSERT INTO proyecto (Nombre,Funcion) VALUES (:Nombre,:Funcion)")
        with engine.connect() as conn:
            conn.execute(query,{'Nombre' :titulo,'Funcion':funcion})
            conn.commit()
    except Exception as e:
        return str(e),400

def guardarCartas(archivo,parcial,nombre,matricula):
    base_folder = os.path.join('Documentos',matricula,parcial)
    UPLOAD_FOLDER = os.path.join(base_folder,'Cartas')
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    nuevo_nombre = f'cartas{nombre}{parcial}.pdf'
    if archivo.filename == '':
        return 'No se selecciono ningun archivo'
    if not archivo.filename.endswith('.pdf'):
        return 'debe ser un archivo pdf'
    ruta_guardado = os.path.join(UPLOAD_FOLDER,secure_filename(nuevo_nombre))
    archivo.save(ruta_guardado)
    return ruta_guardado

def guardarProyectos(archivo,parcial,nombre,matricula):
    base_folder = os.path.join('Documentos',matricula,parcial)
    UPLOAD_FOLDER = os.path.join(base_folder,'Proyecto')
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    nuevo_nombre = f'proyeto{nombre}{parcial}.pdf'
    ruta_guardado = os.path.join(UPLOAD_FOLDER,secure_filename(nuevo_nombre))
    archivo.save(ruta_guardado)
    return ruta_guardado
    
def guardar03(archivo,parcial,nombre,matricula):
    base_folder = os.path.join('Documentos',matricula,parcial)
    UPLOAD_FOLDER = os.path.join(base_folder,'FO03')
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    nuevo_nombre = f'proyeto{nombre}{parcial}.pdf'
    if archivo.filename == '':
        return 'No se selecciono ningun archivo'
    if not archivo.filename.endswith('.pdf'):
        return 'debe ser un archivo pdf'
    ruta_guardado = os.path.join(UPLOAD_FOLDER,secure_filename(nuevo_nombre))
    archivo.save(ruta_guardado)
    return ruta_guardado

def cargarAsesorEmp():
    query = text("SELECT AsesorID,Nombre1,Nombre2,ApellidoP,ApellidoM,Empresa from asesorempresarial ORDER BY Empresa")
    with engine.connect() as conn:
        ok= conn.execute(query)
        if ok:
            opciones = ''.join([f'<option value="{row[0]}">{row[5]} - {row[3]} {row[4]} {row[1]} {row[2]}</option>' for row in ok])
            return opciones

def cargarAsesorAcademico():
    query = text("SELECT Id,Nombre1,Nombre2,ApellidoP,ApellidoM from asesoracademico ORDER BY ApellidoP")
    with engine.connect() as conn:
        ok= conn.execute(query)
        if ok:
            opciones = ''.join([f'<option value="{row[0]}">{row[3]} {row[4]} {row[1]} {row[2]} </option>' for row in ok])
            return opciones

def guardarEquipo(matricula, NoEquipo, ID):
    try:
        query = text("INSERT INTO equipos (Matricula, NoEquipo, Id_Proyecto) VALUES (:Matricula,:NoEquipo,:Id_Proyecto)")
        with engine.connect() as conn:
            conn.execute(query,{'Matricula':matricula,'NoEquipo':NoEquipo,'Id_Proyecto':ID})
            conn.commit()
            return True
    except Exception as e:
        return ID

def guardarEquipo2(matricula, matricula2, NoEquipo, ID):
    try:
        query1 = text("INSERT INTO equipos (Matricula, NoEquipo, Id_Proyecto) VALUES (:Matricula1, :NoEquipo, :Id_Proyecto)")
        query2 = text("INSERT INTO equipos (Matricula, NoEquipo, Id_Proyecto) VALUES (:Matricula2, :NoEquipo, :Id_Proyecto)")

        with engine.connect() as conn:
            with conn.begin():  
                conn.execute(query1, {'Matricula1': matricula, 'NoEquipo': NoEquipo, 'Id_Proyecto': ID})
                conn.execute(query2, {'Matricula2': matricula2, 'NoEquipo': NoEquipo, 'Id_Proyecto': ID})
                return True
    except Exception as e:
        return ID

def guardarEquipo3(matricula,matricula2,matricula3, NoEquipo, ID):
    try:
        query1 = text("INSERT INTO equipos (Matricula, NoEquipo, Id_Proyecto) VALUES (:Matricula1, :NoEquipo, :Id_Proyecto)")
        query2 = text("INSERT INTO equipos (Matricula, NoEquipo, Id_Proyecto) VALUES (:Matricula2, :NoEquipo, :Id_Proyecto)")
        query3 = text("INSERT INTO equipos (Matricula, NoEquipo, Id_Proyecto) VALUES (:Matricula3, :NoEquipo, :Id_Proyecto)")

        with engine.connect() as conn:
            with conn.begin():  
                conn.execute(query1, {'Matricula1': matricula, 'NoEquipo': NoEquipo, 'Id_Proyecto': ID})
                conn.execute(query2, {'Matricula2': matricula2, 'NoEquipo': NoEquipo, 'Id_Proyecto': ID})
                conn.execute(query3, {'Matricula3': matricula3, 'NoEquipo': NoEquipo, 'Id_Proyecto': ID})
                return True
    except Exception as e:
        return ID

def guardarEquipo4(matricula,matricula2,matricula3,matricula4, NoEquipo, ID):
    try:
        query1 = text("INSERT INTO equipos (Matricula, NoEquipo, Id_Proyecto) VALUES (:Matricula1, :NoEquipo, :Id_Proyecto)")
        query2 = text("INSERT INTO equipos (Matricula, NoEquipo, Id_Proyecto) VALUES (:Matricula2, :NoEquipo, :Id_Proyecto)")
        query3 = text("INSERT INTO equipos (Matricula, NoEquipo, Id_Proyecto) VALUES (:Matricula3, :NoEquipo, :Id_Proyecto)")
        query4 = text("INSERT INTO equipos (Matricula, NoEquipo, Id_Proyecto) VALUES (:Matricula4, :NoEquipo, :Id_Proyecto)")

        with engine.connect() as conn:
            with conn.begin():  
                conn.execute(query1, {'Matricula1': matricula, 'NoEquipo': NoEquipo, 'Id_Proyecto': ID})
                conn.execute(query2, {'Matricula2': matricula2, 'NoEquipo': NoEquipo, 'Id_Proyecto': ID})
                conn.execute(query3, {'Matricula3': matricula3, 'NoEquipo': NoEquipo, 'Id_Proyecto': ID})
                conn.execute(query4, {'Matricula4': matricula4, 'NoEquipo': NoEquipo, 'Id_Proyecto': ID})
                return True
    except Exception as e:
        return ID

def guardarEquipo5(matricula, matricula2, matricula3, matricula4, matricula5, NoEquipo, ID):
    try:
        query1 = text("INSERT INTO equipos (Matricula, NoEquipo, Id_Proyecto) VALUES (:Matricula1, :NoEquipo, :Id_Proyecto)")
        query2 = text("INSERT INTO equipos (Matricula, NoEquipo, Id_Proyecto) VALUES (:Matricula2, :NoEquipo, :Id_Proyecto)")
        query3 = text("INSERT INTO equipos (Matricula, NoEquipo, Id_Proyecto) VALUES (:Matricula3, :NoEquipo, :Id_Proyecto)")
        query4 = text("INSERT INTO equipos (Matricula, NoEquipo, Id_Proyecto) VALUES (:Matricula4, :NoEquipo, :Id_Proyecto)")
        query5 = text("INSERT INTO equipos (Matricula, NoEquipo, Id_Proyecto) VALUES (:Matricula5, :NoEquipo, :Id_Proyecto)")

        with engine.connect() as conn:
            with conn.begin():
                conn.execute(query1, {'Matricula1': matricula, 'NoEquipo': NoEquipo, 'Id_Proyecto': ID})

                conn.execute(query2, {'Matricula2': matricula2, 'NoEquipo': NoEquipo, 'Id_Proyecto': ID})

                conn.execute(query3, {'Matricula3': matricula3, 'NoEquipo': NoEquipo, 'Id_Proyecto': ID})

                conn.execute(query4, {'Matricula4': matricula4, 'NoEquipo': NoEquipo, 'Id_Proyecto': ID})

                conn.execute(query5, {'Matricula5': matricula5, 'NoEquipo': NoEquipo, 'Id_Proyecto': ID})
                return True
    except Exception as e:
        return ID 

def cargarIDProyecto(nombre):
    try:
        query = text("SELECT ProyectoID FROM proyecto WHERE Nombre = :Nombre")
        with engine.connect() as conn:
            ok= conn.execute(query, {'Nombre': nombre}).fetchone()
            if ok:
                ID = ok[0]
                return ID
            else:
                return 'no encontado'
    except Exception as e:
            return f'error {e}'

def cargarEquipoMaximo():
    query = text("SELECT MAX(NoEquipo) FROM equipos")
    with engine.connect() as conn:
        resultado = conn.execute(query).fetchone()
        max_equipos = resultado[0] if resultado[0] is not None else 0
        return max_equipos + 1

def borrarIDproyecto(ID):
    try:
        query1 = text("DELETE FROM proyecto WHERE ProyectoID = :ID")        
        with engine.connect() as conn:
            with conn.begin():  
                conn.execute(query1, {'ID': ID})
            return True 
    except Exception as e:
        print(f"Error: {e}") 
        return False

def cargarProyectoAlumno(Matricula):
    
    query = text("SELECT p.Nombre FROM estudiante est JOIN equipos e ON est.Matricula = e.Matricula JOIN proyecto p ON e.Id_Proyecto = p.ProyectoID WHERE est.Matricula = :Matricula")
    with engine.connect() as conn:
        resultado = conn.execute(query,{'Matricula':Matricula}).fetchone()
        if resultado:
            return resultado[0]
        else:
            return "No asignado"
    
def guardarRutaDocumentos(matricula,ruta_proyecto,parcial,NombreProyecto):
    docExiste = documentoExiste(matricula,parcial)
    if docExiste != True:
        try:
            query = text("INSERT INTO documentos (Matricula,Proyecto,Parcial,NombreProyecto) VALUES (:Matricula,:ruta_proyecto,:parcial,:NombreProyecto)")
            with engine.connect() as conn:
                conn.execute(query,{'Matricula':matricula,'ruta_proyecto':ruta_proyecto,'parcial':parcial,'NombreProyecto':NombreProyecto})
                conn.commit()
                return True
        except Exception as e:
            return f'-------------Error {e}'
    else:
        return False

def guardarRuta03(matricula,ruta_03,parcial):
    formatoExiste = formato03Existe(matricula,parcial)
    if formatoExiste != True:
        try:
            query = text("INSERT INTO Formato03 (Matricula,Formato03,Parcial) VALUES (:Matricula,:ruta_03,:parcial)")
            with engine.connect() as conn:
                conn.execute(query,{'Matricula':matricula,'ruta_03':ruta_03,'parcial':parcial})
                conn.commit()
                return True
        except Exception as e:
            return f'-------------Error {e}'
    else:
        return False

def guardarCartass(matricula,ruta_cartas,parcial):
    cartaExiste = cartasExiste(matricula,parcial)
    if cartaExiste != True:
        try:
            query = text("INSERT INTO Cartas (Matricula,Cartas,Parcial) VALUES (:Matricula,:ruta_cartas,:parcial)")
            with engine.connect() as conn:
                conn.execute(query,{'Matricula':matricula,'ruta_cartas':ruta_cartas,'parcial':parcial})
                conn.commit()
                return True
        except Exception as e:
            return f'-------------Error {e}'
    else:
        return False

def promedio(question11,question12,question13,question14,question15,question16,question17,question18,question19):
    promedio = (question11+question12+question13+question14+question15+question16+question17+question18+question19)/9
    promedio = round(promedio,2)
    return promedio


@app.route('/calificarProyectoU1',methods=['POST'])
def calificarProyectoU1():
    Matricula = request.form['matricula']
    validado = validarCalificado(Matricula)
    if validado:
        return render_template('cargas/calificacion.html')
    else:
        Antecedentes = int(request.form['Antecedentes'])
        Planteamiento = int(request.form['Planteamiento'])
        Justificacion = int(request.form['Justificacion'])
        Objetivo = int(request.form['Objetivo'])
        ObjetivoEspecifico = int(request.form['ObjetivoEspecifico'])
        Calificacion = (Antecedentes+Planteamiento+Justificacion+Objetivo+ObjetivoEspecifico)/5
        calificado = calificar(Matricula,Calificacion)
        if calificado:
            return "Cy"
        else:
            return "Ño"
        
@app.route('/calificarProyectoP1',methods=['POST'])
def calificarProyectoP1():
    Matricula = request.form['matricula']
    validado = validarCalificado(Matricula)
    if validado:
        return render_template('cargas/calificacion.html')
    else:
        Antecedentes = int(request.form['Antecedentes'])
        Planteamiento = int(request.form['Planteamiento'])
        Justificacion = int(request.form['Justificacion'])
        Objetivo = int(request.form['Objetivo'])
        ObjetivoEspecifico = int(request.form['ObjetivoEspecifico'])
        Calificacion = (Antecedentes+Planteamiento+Justificacion+Objetivo+ObjetivoEspecifico)/5
        calificado = calificar(Matricula,Calificacion)
        if calificado:
            return "Cy"
        else:
            return "Ño"
        

@app.route('/calificarProyectoU3',methods=['POST'])
def calificarProyectoU3():
    Matricula = request.form['matricula']
    validado = validarCalificado(Matricula)
    if validado:
        return render_template('cargas/calificacion.html')
    else:
        Antecedentes = int(request.form['Antecedentes'])
        Planteamiento = int(request.form['Planteamiento'])
        Justificacion = int(request.form['Justificacion'])
        Objetivo = int(request.form['Objetivo'])
        ObjetivoEspecifico = int(request.form['ObjetivoEspecifico'])
        Calificacion = (Antecedentes+Planteamiento+Justificacion+Objetivo+ObjetivoEspecifico)/5
        calificado = calificar(Matricula,Calificacion)
        if calificado:
            return "Cy"
        else:
            return "Ño"
    


def calificar(matricula,calificacion):
    try:
        query = text("INSERT INTO calificacionproyecto (Alumno, Calificacion,Parcial) VALUES (:Alumno,:Calificacion,'Parcial 1')")
        with engine.connect() as conn:
            conn.execute(query,{'Alumno':matricula,'Calificacion':calificacion})
            conn.commit()
            return True
    except Exception as e:
        return f'error---------------->{e}'
    
def calificarP2(matricula,calificacion):
    try:
        query = text("INSERT INTO calificacionproyecto (Alumno, Calificacion,Parcial) VALUES (:Alumno,:Calificacion,'Parcial 2')")
        with engine.connect() as conn:
            conn.execute(query,{'Alumno':matricula,'Calificacion':calificacion})
            conn.commit()
            return True
    except Exception as e:
        return f'error---------------->{e}'

def validarCalificado(matricula):
    try:
        query = text("SELECT Alumno FROM calificacionproyecto WHERE Alumno =:Matricula")
        with engine.connect() as conn:
            ok = conn.execute(query,{'Matricula':matricula})
            ok = ok.fetchone()
            if ok:
                return True
            else:
                return False
    except Exception as e:
        return f'error---------------->{e}'   


def calificarP2(matricula,calificacion):
    try:
        query = text("INSERT INTO calificacionproyecto (Alumno, Calificacion,Parcial) VALUES (:Alumno,:Calificacion,'Parcial 2')")
        with engine.connect() as conn:
            conn.execute(query,{'Alumno':matricula,'Calificacion':calificacion})
            conn.commit()
            return True
    except Exception as e:
        return f'error---------------->{e}'

def validarCalificadoP2(matricula):
    try:
        query = text("SELECT Alumno FROM calificacionproyecto WHERE Alumno =:Matricula")
        with engine.connect() as conn:
            ok = conn.execute(query,{'Matricula':matricula})
            ok = ok.fetchone()
            if ok:
                return True
            else:
                return False
    except Exception as e:
        return f'error---------------->{e}'   
 

def guardarForm08(promedio,veracidad,matricula):
    try:
        query = text("INSERT INTO encuesta08 (Promedio, Veracidad, Matricula) VALUES (:Promedio,:Veracidad,:Matricula)")
        with engine.connect() as conn:
            conn.execute(query,{'Promedio':promedio,'Veracidad':veracidad,'Matricula':matricula})
            conn.commit()
            return True
    except Exception as e:
        return f'error---------------->{e}'

def guardarProyectoAsesores(ID,asesorE,asesorA):
    try:
        query = text("INSERT INTO proyectoasesores (Id_asesorE, Id_asesorA, Id_proyecto) VALUES (:asesorE,:asesorA,:ID)")
        with engine.connect() as conn:
            conn.execute(query,{'asesorE':asesorE,'asesorA':asesorA,'ID':ID})
            conn.commit()
            return True
    except Exception as e:
        return f'error---------------->{e}'    

def inicioSesionAsesorA(correo,password):
    try:
        query = text("SELECT Nombre1,Nombre2,ApellidoP,ApellidoM,Telefono,Correo,Id FROM asesoracademico WHERE password = :password AND Correo =:correo")
        with engine.connect() as conn:
            ok= conn.execute(query, {'password': password,'correo':correo}).fetchone()
            if ok:
                Nombre1 = ok[0]
                Nombre2 = ok[1]
                ApellidoP = ok[2]
                ApellidoM = ok[3]
                Telefono = ok[4]
                Correo = ok[5]
                ID = ok[6]
                return render_template('/perfiles/AsesorAcademico/asesor.html',Nombre1=Nombre1,Nombre2=Nombre2,ApellidoM=ApellidoM,ApellidoP=ApellidoP,Telefono=Telefono,Correo=Correo,ID = ID)
            else:
                return 'no encontado'
    except Exception as e:
            return f'error {e}'

def cargarProyectosAsesor(ID):
    try:
        query = text('''SELECT 
        p.Nombre AS NombreProyecto
        FROM 
        asesoracademico a
        JOIN 
        proyectoasesores pa
        ON 
        a.Id = pa.Id_asesorA
        JOIN 
        proyecto p
        ON 
        pa.Id_proyecto = p.ProyectoID
        WHERE a.Id = :ID;''')
        with engine.connect() as conn:
            ok= conn.execute(query, {'ID': ID}).fetchall()
            if ok:
                opciones_html = "".join(f'<option value="{resultado[0]}">{resultado[0]}</option>' for resultado in ok)
            else:
                opciones_html ='<option value="">Nada por mostrar</option>'
            return opciones_html
    except Exception as e:
        return None

def cargarAsesorEmpresarial(Proyecto):
    query = text('''SELECT 
    CONCAT(ae.Nombre1, ' ', ae.Nombre2, ' ', ae.ApellidoP, ' ', ae.ApellidoM) AS AsesorEmpresarial,
    p.ProyectoID,
    p.Nombre AS NombreProyecto
FROM 
    proyectoasesores pa
JOIN 
    asesorempresarial ae ON pa.Id_asesorE = ae.AsesorID
JOIN 
    proyecto p ON pa.Id_proyecto = p.ProyectoID
    WHERE p.Nombre = :NombreProyecto''')
    with engine.connect() as conn:
        resultado = conn.execute(query,{'NombreProyecto':Proyecto}).fetchone()
        if resultado:
            return resultado[0]
        else:
            return 'No asignado'

def documentoExiste(matricula,parcial):
    query = text("SELECT Proyecto FROM documentos WHERE Matricula = :Matricula AND Parcial = :Parcial")
    with engine.connect() as conn:
        resultado = conn.execute(query,{'Matricula':matricula,'Parcial':parcial}).fetchone()
        if resultado:
            return True
        else:
            return False
        

def formato03Existe(matricula,parcial):
    query = text("SELECT Formato03 FROM Formato03 WHERE Matricula = :Matricula AND Parcial = :Parcial")
    with engine.connect() as conn:
        resultado = conn.execute(query,{'Matricula':matricula,'Parcial':parcial}).fetchone()
        if resultado:
            return True
        else:
            return False

def cartasExiste(matricula,parcial):
    query = text("SELECT Cartas FROM Cartas WHERE Matricula = :Matricula AND Parcial = :Parcial")
    with engine.connect() as conn:
        resultado = conn.execute(query,{'Matricula':matricula,'Parcial':parcial}).fetchone()
        if resultado:
            return True
        else:
            return False
        
def descargarPDF(ruta):
    pdf_ruta = ruta
    try:
        return send_file(pdf_ruta,as_attachment=True)
    except Exception as e:
        return f"Error {e}"
    
def obtenerRutaPDF(proyecto,parcial):
    try:
        query = text("SELECT Proyecto FROM documentos WHERE NombreProyecto = :NombreProyecto AND Parcial = :parcial")
        with engine.connect() as conn:
            ok= conn.execute(query,{'NombreProyecto':proyecto,'parcial':parcial})
            ruta = ok.fetchone()
            if ruta:
                rutaR = ruta[0]
            return rutaR
        
    
    except Exception as e:
        return f'error--------aqui-------->{e}'
    

def verificarAsignacionProyecto(Matricula):
    try:
        query = text("SELECT matricula FROM Proyecto Matricula = :Matricula")
        with engine.connect() as conn:
            ok= conn.execute(query,{'Matricula':Matricula})
            succ = ok.fetchone()
            if succ:
                return True 
    except Exception as e:
        return False

def visualizarPDF(ruta):
    pdf_path = ruta
    try:
        # Abrir el PDF y extraer la primera página
        pdf_document = fitz.open(pdf_path)
        page = pdf_document[0]
        
        # Renderizar la página como imagen
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        
        # Guardar la imagen en una carpeta temporal
        temp_folder = os.path.join("static", "temp")
        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)
        image_filename = f"preview_{os.path.basename(ruta).replace('.pdf', '.png')}"
        image_path = os.path.join(temp_folder, image_filename)
        img.save(image_path, format="PNG")
        
        # Cerrar el documento PDF
        pdf_document.close()
        
        # Retornar la URL relativa de la imagen y ningún error
        return url_for('static', filename=f"temp/{image_filename}")
    except Exception as e:
        # Retornar None como URL y el mensaje de error
        return None, str(e)



@app.route('/registrar_academico', methods=['POST'])
def registrar_academico():
    nombre1 = request.form['nombre1']
    nombre2 = request.form['nombre2']
    apellidoP = request.form['apellidoP']
    apellidoM = request.form['apellidoM']
    telefono = request.form['telefono']
    correo = request.form['correo']
    
    try:
        query = text("""
            INSERT INTO asesoracademico (Nombre1, Nombre2, ApellidoP, ApellidoM, Telefono, Correo)
            VALUES (:nombre1, :nombre2, :apellidoP, :apellidoM, :telefono, :correo)
        """)
        with engine.connect() as conn:
            conn.execute(query, {
                'nombre1': nombre1,
                'nombre2': nombre2,
                'apellidoP': apellidoP,
                'apellidoM': apellidoM,
                'telefono': telefono,
                'correo': correo     
            })
            conn.commit()
        return render_template('Cargas/agregar_asesores.html')
    except Exception as e:
        return f'Error al registrar: {e}'
    

@app.route('/registrar_empresarial', methods=['POST'])
def registrar_empresarial():
    nombre1 = request.form['nombre1']
    nombre2 = request.form['nombre2']
    apellidoP = request.form['apellidoP']
    apellidoM = request.form['apellidoM']
    telefono = request.form['telefono']
    correo = request.form['correo']
    empresa = request.form['empresa']
    try:
        query = text("""
            INSERT INTO asesorempresarial (Nombre1, Nombre2, ApellidoP, ApellidoM, Telefono, Correo,Empresa)
            VALUES (:nombre1, :nombre2, :apellidoP, :apellidoM, :telefono, :correo, :empresa)
        """)
        with engine.connect() as conn:
            conn.execute(query, {
                'nombre1': nombre1,
                'nombre2': nombre2,
                'apellidoP': apellidoP,
                'apellidoM': apellidoM,
                'telefono': telefono,
                'correo': correo,
                'empresa': empresa   
            })
            conn.commit()
        return render_template('Cargas/agregar_asesores.html')
    except Exception as e:
        return f'Error al registrar: {e}'



@app.route('/registro_asesor',methods=['POST'])
def registro_asesor():
    opcion = cargarsesorEmp()
    return render_template('/registro_asesor.html',cargar98975 = opcion)

@app.route('/registrarAsesor', methods=['POST'])
def cambiaraqui():
    opcion = cargarsesorEmp()
    return render_template('registro_asesor.html',cargar98975 = opcion)

def cargarsesorEmp():
    query = text("SELECT Nombre from Empresa")
    with engine.connect() as conn:
        ok= conn.execute(query)
        if ok:
            opciones = ''.join([f'<option value="{row[0]}">{row[0]}</option>' for row in ok])
            return opciones
        
def IDproyecto(Proyecto):
    query = text("SELECT ProyectoID FROM proyecto WHERE Nombre = :Proyecto")
    with engine.connect() as conn:
        ok= conn.execute(query,{'Proyecto':Proyecto})
        ok = ok.fetchone()
        return ok[0]
    
def obtenerMatricula(Proyecto):
    query = text("""SELECT estudiante.Matricula, estudiante.Nombre1, estudiante.Nombre2, estudiante.ApellidoP, estudiante.ApellidoM
                FROM estudiante
                JOIN equipos ON equipos.Matricula = estudiante.Matricula
                WHERE equipos.Id_Proyecto = :Proyecto;""")
    with engine.connect() as conn:
        ok= conn.execute(query,{'Proyecto':Proyecto})
        ok = ok.fetchall()
        opciones = ''.join([f'<option value="{row[0]}">{row[1]} {row[2]} {row[3]} {row[4]}</option>' for row in ok])      
        return opciones