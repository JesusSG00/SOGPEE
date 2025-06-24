import datetime
from flask import Flask,render_template,request, url_for,send_file
from werkzeug.utils import secure_filename
from sqlalchemy import text, create_engine, MetaData, Table
from conexion import engine
import os,fitz,re
from PIL import Image
from pathlib import Path
import pandas as pd

app = Flask(__name__)
CSV_PATH = 'data/foest07.csv'
EXCEL_PATH = 'data/foest07.xlsx'


#Pagina principal
@app.route('/')
def index():
    limpiar_temp()
    return render_template('index.html')
#Formulario de login del estudiante
@app.route('/loginEstudiante2')
def loginEstudiante2():
    return render_template('/login/loginEstudiante2.html')

@app.route('/loginEstudiante3',methods=['POST'])
def loginEstudiante3():
    return render_template('/login/loginEstudiante2.html')
#Formulario de login del asesor academico
@app.route('/loginAsesorAcademico2')
def loginAsesorAcademico2():
    return render_template('/login/loginAsesorAcademico2.html')
@app.route('/loginAsesorAcademico3',methods=['POST'])
def loginAsesorAcademico3():
    return render_template('/login/loginAsesorAcademico2.html')

#Formulario de login del coordinador
@app.route('/loginCoordinacion2')
def loginCoordinacion2():
    return render_template('login/loginCoordinacion2.html')

@app.route('/loginCoordinacionIni',methods=['POST'])
def loginCoordinacion():
    return render_template('perfiles/Coordinacion/perfil_coordinacion.html')

@app.route('/modificarPeriodo',methods=['POST'])
def modificarPeriodo():
    anio=aniobase()
    return render_template('perfiles/Coordinacion/modificar_periodo.html',anio=anio)

@app.route('/modificarPeriodoFun',methods=['POST'])
def modificarPeriodoFun():
    periodo = request.form['periodo']
    updateModificarPeriodo(periodo)
    obtener_anio_actual()
    return render_template('Cargas/periodo_modificado.html')

def updateModificarPeriodo(periodo):
    with engine.connect() as conn:
        try:
       # Desactivar todos los periodos primero
            query_desactivar = text("UPDATE periodos SET Estado = 'inactivo'")
            conn.execute(query_desactivar)

            # Activar el periodo seleccionado
            query_activar = text("""
                UPDATE periodos 
                SET Estado = 'activo' 
                WHERE PeriodoCuatrimestral = :periodo
            """)
            conn.execute(query_activar, {'periodo': periodo})

            # Confirmar la transacción
            conn.commit()

            

        except Exception as e:
            # En caso de error, hacer rollback y mostrar un mensaje de error
            conn.rollback()
            return f'ERROR AL MODIFICAR EL PERIODO: {str(e)}'
            

        except Exception as e:
            # En caso de error, hacer rollback y mostrar un mensaje de error
            conn.rollback()
            return f'ERROR AL MODIFICAR EL PERIODO: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)



@app.route('/loginCoordinacion3',methods=['POST'])
def loginCoordinacion3():
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

#Dirigir pagina para buscar expediente Asesor Empresarial
@app.route('/foest07')
def asesorEmpresarial():
    return render_template('login/asesorEmpresarial3.html')

#Dirigir pagina para buscar expediente Asesor Empresarial pero en el foest 02
@app.route('/foest02')
def asesorEmpresarial1():
    return render_template('login/asesorEmpresarialfoest02.html')

@app.route('/foest02',methods=['POST'])
def asesorEmpresarialpost():
    return render_template('login/asesorEmpresarialfoest02.html')

@app.route('/asesorEmpresarial2',methods=['POST'])
def asesorEmpresarial2():
    return render_template('login/asesorEmpresarial3.html')

#Función para buscar expediente Asesor Empresarial
@app.route('/buscarExpedienteAsesorEmpresarial', methods=['POST'])
def buscarExpedienteAsesorEmpresarial():
    anio = aniobase()
    ProyectoID= request.form['ProyectoID']
    equipo = int(cargarEquipo(ProyectoID))
    integrantes = listaEstudiantes(ProyectoID)
    periodo = periodoCuatrimestral() 
   
    Nombreproyecto = proyectoAsesorEmpr(ProyectoID)
    empresa=cargarEmpresaEquipo(ProyectoID)
 
    nombreoculto = NombreAsesorOculto(ProyectoID)

    try:
        query = text("SELECT * FROM proyecto WHERE ProyectoID = :ProyectoID")
        with engine.connect() as conn:
            proyecto = conn.execute(query, {'ProyectoID': ProyectoID}).fetchone()
            if proyecto:
                return render_template('perfiles/AsesorEmpresarial/evaluacion_empresa.html', proyecto=proyecto,Nombreproyecto=Nombreproyecto,empresa=empresa,nombre=nombreoculto,integrantes = integrantes,periodo=periodo,equipo=equipo,nombreoculto=nombreoculto,anio=anio)
            else:
                return render_template('Cargas/ProyectoNEncontrado.html')
            
    except Exception as e:
        return render_template('Cargas/ProyectoNEncontrado.html')
    
#Función para buscar expediente Asesor Empresarial
@app.route('/buscarExpedienteAsesorEmpresarial1', methods=['POST'])
def buscarExpedienteAsesorEmpresarial1():
    anio = aniobase()
    ProyectoID= request.form['ProyectoID']
    equipo = int(cargarEquipo(ProyectoID))
    integrantes = listaEstudiantes(ProyectoID)
    periodo = periodoCuatrimestral()
    carrera = cargarCarrera(ProyectoID)
    # etapa = cargarEtapa(ProyectoID)
   
    Nombreproyecto = proyectoAsesorEmpr(ProyectoID)
    empresa=cargarEmpresaEquipo(ProyectoID)
    nombre=NombreAsesor(ProyectoID)
    nombreoculto = NombreAsesorOculto(ProyectoID)

    try:
        query = text("SELECT * FROM proyecto WHERE ProyectoID = :ProyectoID")
        with engine.connect() as conn:
            proyecto = conn.execute(query, {'ProyectoID': ProyectoID}).fetchone()
            if proyecto:
                return render_template('Cuestionarios/cuestionario_foest02.html', anio=anio,proyecto=proyecto,Nombreproyecto=Nombreproyecto,empresa=empresa,nombre=nombre,integrantes = integrantes,periodo=periodo,carrera=carrera,equipo=equipo,nombreoculto=nombreoculto,ProyectoID=ProyectoID)
            else:
                return render_template('Cargas/ProyectoNEncontrado.html')
            
    except Exception as e:
        return render_template('Cargas/ProyectoNEncontrado.html')

#Evaluacion empresa
@app.route('/evaluacionEmpresa')
def evaluacionEmpresa():
    return render_template('evaluacion_empresa.html')

#Evaluacion empresa 02
@app.route('/cuestionario_foest02')
def cuestionario_foest02():
    return render_template('Cuestionarios/cuestionario_foest02.html')

#Evaluacion empresa 02 siguiente parte 
@app.route('/evaluacion_foest02',methods=['POST'])
def evaluacion_foest02():
    nombreasesor = request.form['nombreasesor']
    ProyectoID= request.form['ProyectoID']
    resultado = obtenerMatricula(ProyectoID)
    GradoEstudios = request.form['GradoEstudios']
    Carrera = request.form['Carrera']
    NombreEmpresa = request.form['NombreEmpresa']
    projectTitl = request.form['projectTitl']
    periodo = periodoCuatrimestral()
    anio = aniobase()

    return render_template('Cuestionarios/evaluacion_foest02.html',nombreasesor=nombreasesor,resultado=resultado,GradoEstudios=GradoEstudios,Carrera=Carrera,NombreEmpresa=NombreEmpresa,projectTitl=projectTitl,ProyectoID=ProyectoID,periodo=periodo,anio=anio)


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
    Procedimiento = request.form['Procedimiento']
    if Procedimiento == "0":
        return 'selecciona procedimiento'
    if numero == '1': #Se ejecuta si el equipo tiene 1 integrante
        matricula = request.form['estudiante-0-campo1']
        agregarproyectos(titulo,funcion) #Se agrega el proyecto a la base de datos
        ID = cargarIDProyecto(titulo) #Se obtiene el ID del proyecto que se acaba de agregar
        equipo = cargarEquipoMaximo() #Se obtiene el numero del ultimo equipo agregado +1
        ok = guardarEquipo(matricula,equipo,ID,Procedimiento) #Se guarda el equipo en la base de datos si todo es correcto
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
            ok= guardarEquipo2(matricula,matricula2,equipo,ID,Procedimiento)
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
        ok = guardarEquipo3(matricula,matricula2,matricula3,equipo,ID,Procedimiento)
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
        ok= guardarEquipo4(matricula,matricula2,matricula3,matricula4,equipo,ID,Procedimiento)
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
        ok= guardarEquipo5(matricula,matricula2,matricula3,matricula4,matricula5,equipo,ID,Procedimiento)
        guardarProyectoAsesores(ID,asesorE,asesorA)
        if ok != True:
            return render_template('Error/Error.html',ID=ok)
        return render_template('Cargas/cargaEquipo.html')

@app.route('/regresarasesoracademico',methods=['POST'])
def regresarasesor():
    ID = request.form['IDA']
    resultado = cargarProyectosAsesor(ID)
    return render_template('/perfiles/AsesorAcademico/revisar_expediente.html',resultado = resultado,ID = ID)
                

#Funcion para subir los documentos del estudiante
@app.route('/enviarDocumentos', methods=['POST'])
def enviarDocumentos():
    parcial = request.form['parcialR']
    nombre = request.form['nombre']
    proyectoN = request.form['proyectoR']
    cartas = request.files.get('cartas')
    proyecto = request.files.get('proyecto')
    
    matricula = request.form['matricula']
    correo = request.form['correo']
    if parcial != "":
        if proyecto is None: #Se valida si el proyecto y la evaluacion estan vacios
            validar = request.form['validar']
            if validar == "False":
                return render_template('error/errorValidar.html', matricula=matricula,correo=correo)
            else:
                ruta_carta = guardarCartas(cartas,parcial,nombre,matricula) #Se obtiene la ruta de la carta
                guardarCartass(matricula,ruta_carta,parcial)#Se guarda la ruta de la carta en la base de datos
        if cartas is None:#Se valida si la carta y la evaluacion estan vacios
            validar = request.form['validar']
            if validar == "False":
                return render_template('error/errorValidar.html', matricula=matricula,correo=correo)
            else:
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
@app.route('/iniciarsesionestudianteEncuesta',methods=['POST'])
def iniciarsesionEncuesta():
    matricula = request.form['Matricula']
    proyecto = cargarProyectoAlumno(matricula)
    asesor = cargarAsesorEmpresarial(proyecto)
    
    return render_template('/perfiles/evaluacionEstudiante.html',Matricula=matricula,proyecto = proyecto,asesor=asesor)
#Funcion para cargar la pagina de cuestionario de satisfaccion
@app.route('/encuestaSatisfaccion', methods=['POST'])
def encuestaSatisfaccion():
    Matricula = request.form['Matricula']
    Correo = request.form['correo']
    periodo = periodoCuatrimestral() 
    anio = aniobase()

    
    # Verificar si ya existe una encuesta
    try:
        query = text("SELECT COUNT(*) FROM foest08 WHERE Matricula = :Matricula")
        with engine.connect() as conn:
            result = conn.execute(query, {'Matricula': Matricula}).scalar()
            
            if result > 0:
                # Si ya existe, mostrar mensaje
                return render_template('Cargas/mensaje_encuesta_existente.html', 
                                    mensaje="Ya has completado la encuesta anteriormente.",Matricula = Matricula,Correo= Correo, periodo=periodo,anio=anio)
            else:
                # Si no existe, mostrar el formulario de la encuesta
                return render_template('Cuestionarios/evaluacion_cuestionario.html',
                                    Matricula=Matricula, correo=Correo, periodo=periodo,anio=anio)
                                    
    except Exception as e:
        # Manejar cualquier error de base de datos
        return f'Error al verificar la encuesta: {str(e)}'
    
#Funcion para obtener los datos del cuestionario de satisfaccion
@app.route('/EvalulacionEstudiante', methods=['POST'])
def enviarEvaluacionEstudiante():
    matricula = request.form['Matricula']
    periodo = periodoCuatrimestral() 
    anio = aniobase()

    # Verificar nuevamente antes de guardar
    if verificar_encuesta_existente(matricula):
        return render_template('Cargas/mensaje_encuesta_existente.html', 
                             mensaje="Ya has completado la encuesta anteriormente.")
    
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
    comentario = request.form.get('comentarios')
    if comentario == "":
        comentario = "Sin comentarios"
  
    prom = promedio(question11,question12,question13,question14,question15,
                   question16,question17,question18,question19)
    guardarForm08C(question11,question12,question13,question14,question15,question16,question17,question18,question19,prom,veracidad,comentario,matricula,periodo,anio)
    return render_template('Cargas/EnvioEvaluacionEstudiante.html',matricula=matricula, correo=correo, periodo=periodo,anio=anio)

@app.route('/loginAsesorAcademico',methods=['POST'])
def loginAsesorAcademico():
    correo = request.form['correo']
    password = request.form['password']
    resultado = inicioSesionAsesorA(correo,password)
    return resultado

#Funcion para cargar la pagina de revisar expediente
@app.route('/AbrirExpediente',methods=['POST'])
def AbrirExpediente():
    ID = request.form['ID']
    resultado = cargarProyectosAsesor(ID)
    return render_template('/perfiles/AsesorAcademico/revisar_expediente.html',resultado = resultado,ID = ID)


@app.route('/reseleccionar',methods=['POST'])
def reseleccion():
    ID = request.form['ID']
    resultado = cargarProyectosAsesor(ID)
    return render_template('perfiles/AsesorAcademico/revisar_expediente.html',resultado = resultado,ID = ID)

@app.route('/verArchivo',methods=['POST'])
def abrirExpediente():
    proyecto = request.form['proyecto']
    parcial = request.form['parcial']
    ID = request.form['ID']   
    if proyecto =="" or proyecto =="0":
        return render_template('Error/SeleccionInvalida2.html',ID = ID)
    ruta = obtenerRutaPDF(proyecto,parcial)  
    imagen = visualizarPDF(ruta)
    if imagen ==False:
        return render_template('Error/ArchivoNoEncontrado.html',ID = ID)
    else:
        return render_template('perfiles/AsesorAcademico/abrirExpediente-parcial.html',proyecto = proyecto,imagen = imagen,parcial= parcial,ID = ID)

@app.route('/calificarExpedienteParcial',methods=['POST'])
def abrirExpediente_parcials():
    proyecto = request.form['proyecto']
    parcial = request.form['parcial']
    IDAsesor = request.form['ID']
    ID = IDproyecto(proyecto)
    estudiantes = obtenerMatricula(ID)
    
    if parcial == "Parcial 1":
        return render_template('perfiles/AsesorAcademico/CalificarP1.html',proyecto = proyecto,numero= parcial,estudiantes = estudiantes,IDAsesor = IDAsesor)
    elif parcial == "Parcial 2":
        return render_template('perfiles/AsesorAcademico/CalificarP2.html',proyecto = proyecto,numero= parcial,estudiantes = estudiantes,IDAsesor = IDAsesor)
    else:
        return render_template('perfiles/AsesorAcademico/CalificarP3.html',proyecto = proyecto,numero= parcial,estudiantes = estudiantes,IDAsesor = IDAsesor)

@app.route('/abrirCalificaciones',methods=['POST'])
def verCalificaciones():
    matricula = request.form['matricula']
    correo = request.form['correo']
    proyecto = request.form['proyectoR']
    Calificaciones = Estudiante(matricula,proyecto,correo)
    return Calificaciones


@app.route('/calificarExpediente',methods=['POST'])
def calificarExpediente():
   
    proyecto = request.form['proyectoC']
    IDA = request.form['ID']
    if proyecto =="" or proyecto =="0":
        return render_template('Error/SeleccionInvalida.html',ID = IDA)
    else:
        ID = IDproyecto(proyecto)
        estudiantes = obtenerMatricula(ID)
        return render_template('perfiles/AsesorAcademico/calificar_expediente.html',proyecto= proyecto,estudiantes=estudiantes,IDA= IDA)

@app.route('/guardarCalificacionSer',methods=['POST'])
def guardarCalificacionSer():
    proyecto = request.form['proyecto']
    IDA = request.form['ID']
    ID = IDproyecto(proyecto)
    puntualidad = int(request.form['puntualidad'])
    responsabilidad = int(request.form['responsabilidad'])
    atencion = int(request.form['atencion'])
    etica = int(request.form['etica'])
    capacidad  = int(request.form['capacidad'])
    liderazgo = int(request.form['liderazgo'])
    matricula = request.form['estudiante']
    parcial = request.form['parcial']
    validado = validarSer(matricula)
    calificacion = (puntualidad+responsabilidad+atencion+etica+capacidad+liderazgo)/6
    redondeo = round(calificacion,1)
    calificacion = redondeo
    if validado == False:
        guardado = guardarCalificacion(puntualidad, responsabilidad, atencion, etica, capacidad, liderazgo, calificacion,matricula, parcial)
    else:
        return render_template('Cargas/SerCalificado.html',IDA = IDA,parcial = parcial,proyecto=proyecto,ID = ID)
    if guardado == True:
        return render_template('Cargas/EnvioCalificacion.html',calificacion = calificacion,proyecto = proyecto,parcial= parcial,IDA = IDA,ID = ID)
    else:
        return render_template('Error/Error.html')
        
def guardarCalificacion(puntualidad, responsabilidad, atencion, etica, capacidad, liderazgo, calificacion,matricula, parcial):
    try:
        query = text("INSERT INTO Ser (Puntualidad,Responsabilidad,Atencion,Etica,Capacidad,Liderazgo,Calificacion,Matricula,Parcial) VALUES (:puntualidad, :responsabilidad, :atencion, :etica, :capacidad, :liderazgo, :calificacion, :matricula, :parcial)")
        with engine.begin() as conn:
            conn.execute(query,{'puntualidad':puntualidad,'responsabilidad':responsabilidad,'atencion':atencion,'etica':etica,'capacidad':capacidad,'liderazgo':liderazgo,'calificacion':calificacion,'matricula':matricula,'parcial':parcial})
           
            return True
    except Exception as e:
        print('----',e)
        return f'----------------------------------------{e}'

@app.route('/calificarSer',methods=['POST'])
def calificarSer():
    IDA = request.form['ID']
    proyecto = request.form['proyecto']
    parcial = request.form['parcial']
    if proyecto =="" or proyecto =="0":
        ID = request.form['ID']
        return render_template('Error/SeleccionInvalida.html',ID = ID)
    ID = IDproyecto(proyecto)
    resultado = obtenerMatricula(ID)
    return render_template('perfiles/AsesorAcademico/calificar_ser.html',resultado = resultado,parcial = parcial,proyecto=proyecto,ID = ID,IDA = IDA)

def validarSer(matricula):
    try:
        query = text("SELECT COUNT(*) FROM ser WHERE Matricula = :matricula")
        with engine.connect() as conn:
            result = conn.execute(query, {'matricula': matricula}).scalar()
            if result > 0:
                return True
            else:
                return False
    except Exception as e:
        return f'error {e}'

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
    folio = folioproyecto(proyecto)
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
                
                return render_template('/perfiles/evaluacionEstudiante.html',Matricula=Matricula,Nombre1=Nombre1,Nombre2=Nombre2,ApellidoM=ApellidoM,ApellidoP=ApellidoP,Telefono=Telefono,Correo=Correo,proyecto = proyecto,asesor=asesor,validar= validar,folio = folio)
            else:
                return render_template('Error/EstudianteNoEncontrado.html')
    except Exception as e:
            return f'error {e}'
    

def folioproyecto(proyecto):
    try:
        query = text("SELECT ProyectoID FROM proyecto WHERE Nombre = :proyecto")
        with engine.connect() as conn:
            ok= conn.execute(query, {'proyecto': proyecto}).fetchone()
            if ok:
                folio = ok[0]
                return folio
            else:
                return "no encontrado"
    except Exception as e:
            return f'error {e}'

def Estudiante(matricula, proyecto,correo):
    try:
        with engine.connect() as conn:
            # Obtener datos del estudiante
            query = text("SELECT Nombre1, Nombre2, ApellidoP, ApellidoM FROM estudiante WHERE matricula = :matricula")
            estudiante = conn.execute(query, {'matricula': matricula}).fetchone()
            if not estudiante:
                return render_template('Error/EstudianteNoEncontrado.html')

            Nombre1, Nombre2, ApellidoP, ApellidoM = estudiante

            # Obtener calificación final
            calificacionF = calificacionfinal(proyecto)

            # Diccionario para almacenar calificaciones con valores por defecto
            datos = {
                "Antecedentes": "", "Planteamiento": "", "Justificacion": "", "Objetivos": "", "ObjetivosEspecificos": "", "Calificacion": "No calificado",
                "Marco": "", "Metodologia": "", "Cronograma": "", "Desarrollo": "", "CalificacionP2": "No calificado",
                "Resultados": "", "Conclusiones": "", "Referencias": "", "Anexos": "", "CalificacionP3": "No calificado",
                "Puntualidad": "", "Responsabilidad": "", "Atencion": "", "Etica": "", "Capacidad": "", "Liderazgo": ""
            }

            # Lista de consultas con sus llaves y parámetros
            consultas = [
                ("SELECT Antecedentes, Planteamiento, Justificacion, Objetivos, ObjetivosEspecificos, Calificacion FROM calificacionproyectop1 WHERE proyecto = :proyecto",
                 ["Antecedentes", "Planteamiento", "Justificacion", "Objetivos", "ObjetivosEspecificos", "Calificacion"],
                 {'proyecto': proyecto}),
                
                ("SELECT Marco, Metodologia, Cronograma, Desarrollo, Calificacion FROM calificacionproyectop2 WHERE proyecto = :proyecto",
                 ["Marco", "Metodologia", "Cronograma", "Desarrollo", "CalificacionP2"],
                 {'proyecto': proyecto}),
                
                ("SELECT Resultados, Conclusiones, Referencias, Anexos, Calificacion FROM calificacionproyectop3 WHERE proyecto = :proyecto",
                 ["Resultados", "Conclusiones", "Referencias", "Anexos", "CalificacionP3"],
                 {'proyecto': proyecto}),
                
                ("SELECT Puntualidad, Responsabilidad, Atencion, Etica, Capacidad, Liderazgo, Calificacion FROM ser WHERE Matricula = :matricula AND Parcial = 'Parcial 1'",
                 ["Puntualidad", "Responsabilidad", "Atencion", "Etica", "Capacidad", "Liderazgo", "Calificacion1"],
                 {'matricula': matricula}),

                ("SELECT Puntualidad, Responsabilidad, Atencion, Etica, Capacidad, Liderazgo, Calificacion FROM ser WHERE Matricula = :matricula AND Parcial = 'Parcial 2'",
                 ["Puntualidad2", "Responsabilidad2", "Atencion2", "Etica2", "Capacidad2", "Liderazgo2", "Calificacion2"],
                 {'matricula': matricula}),

                ("SELECT Puntualidad, Responsabilidad, Atencion, Etica, Capacidad, Liderazgo, Calificacion FROM ser WHERE Matricula = :matricula AND Parcial = 'Parcial 3'",
                 ["Puntualidad3", "Responsabilidad3", "Atencion3", "Etica3", "Capacidad3", "Liderazgo3", "Calificacion3"],
                 {'matricula': matricula})
            ]

            # Ejecutar consultas
            for query_text, keys, parametros in consultas:
                query = text(query_text)
                resultado = conn.execute(query, parametros).fetchone()
                if resultado:
                    for key, value in zip(keys, resultado):
                        datos[key] = value

        return render_template('/perfiles/calificaciones.html',
                               Nombre1=Nombre1, Nombre2=Nombre2, ApellidoP=ApellidoP, ApellidoM=ApellidoM,
                               calificacionF=calificacionF, **datos,correo = correo,matricula=matricula)
    except Exception as e:
        return f'error {e}'

            

def calificacionfinal(proyecto):
    try:
        query = text('''SELECT AVG(Calificacion) AS Promedio
FROM (
    SELECT Calificacion FROM calificacionproyectop1 WHERE Proyecto = :proyecto
    UNION ALL
    SELECT Calificacion FROM calificacionproyectop2 WHERE Proyecto = :proyecto
    UNION ALL
    SELECT Calificacion FROM calificacionproyectop3 WHERE Proyecto = :proyecto
) AS Calificaciones;
''')

        
        with engine.connect() as conn:
            ok = conn.execute(query, {'proyecto': proyecto}).fetchone()
            if ok:
                promedio = ok[0]
                return promedio
            else:
                return render_template('Error/EstudianteNoEncontrado.html')
    except Exception as e:
        return f'error {e}'


def cargarCalificacionesSer(matricula):
    try:
        query = text("SELECT Puntualidad,Responsabilidad,Atencion,Etica,Capacidad,Liderazgo FROM ser WHERE Matricula = :matricula")
        with engine.connect() as conn:
            ok= conn.execute(query, {'matricula': matricula}).fetchone()
            if ok:
                Puntualidad = ok[0]
                Responsabilidad = ok[1]
                Atencion = ok[2]
                Etica = ok[3]
                Capacidad = ok[4]
                Liderazgo = ok[5]
                return render_template('/perfiles/calificaciones.html',Puntualidad=Puntualidad,Responsabilidad=Responsabilidad,Atencion=Atencion,Etica=Etica,Capacidad=Capacidad,Liderazgo=Liderazgo)
            else:
                return render_template('Error/EstudianteNoEncontrado.html')
    except Exception as e:
            return f'error {e}'

@app.route('/EvEmpresasiguiente',methods=['POST'])  
def EvEmpresasiguiente():
    NombreAsesor = request.form['nombreasesor']
    giro = request.form['Giro']
    tipoempresa = request.form['tipoempresa']
    periodo = request.form['periodo']
    equipo = request.form['equipo']
    nombre_empresa = request.form['companyName']
    grado_estudios = request.form['advisorDegree']
    capital = request.form['capital']
    anios_operacion = request.form['aniosOperacion']
    tamanio_empresa = request.form['Tamaño']
    mercado_venta = request.form['Mercado']
    nombreProyecto = request.form['projectTitl']
    procedimiento,carrera = obtenerProcedimientoYCarrera(nombreProyecto)

    if procedimiento and carrera:
        if carrera == "IS":
            return render_template('Cuestionarios/cuestionario_salida_IS.html',procedimiento=procedimiento, nombreProyecto=nombreProyecto, periodo=periodo, nombre_empresa=nombre_empresa, grado_estudios=grado_estudios, capital=capital, anios_operacion=anios_operacion, tamanio_empresa=tamanio_empresa, mercado_venta=mercado_venta,equipo= equipo,tipoempresa = tipoempresa,Giro = giro,NombreAsesor=NombreAsesor)
        elif carrera == "IMA":
            return render_template('Cuestionarios/cuestionario_salida_IMA.html',procedimiento=procedimiento, nombreProyecto=nombreProyecto, periodo=periodo, nombre_empresa=nombre_empresa, grado_estudios=grado_estudios, capital=capital, anios_operacion=anios_operacion, tamanio_empresa=tamanio_empresa, mercado_venta=mercado_venta,equipo= equipo,tipoempresa = tipoempresa,Giro = giro,NombreAsesor=NombreAsesor)
        elif carrera == "IF":
            return render_template('Cuestionarios/cuestionario_salida_IF.html',procedimiento=procedimiento, nombreProyecto=nombreProyecto, periodo=periodo, nombre_empresa=nombre_empresa, grado_estudios=grado_estudios, capital=capital, anios_operacion=anios_operacion, tamanio_empresa=tamanio_empresa, mercado_venta=mercado_venta,equipo= equipo,tipoempresa = tipoempresa,Giro = giro,NombreAsesor=NombreAsesor)
        elif carrera == "ITM":
            return render_template('Cuestionarios/cuestionario_salida_ITM.html',procedimiento=procedimiento, nombreProyecto=nombreProyecto, periodo=periodo, nombre_empresa=nombre_empresa, grado_estudios=grado_estudios, capital=capital, anios_operacion=anios_operacion, tamanio_empresa=tamanio_empresa, mercado_venta=mercado_venta,equipo= equipo,tipoempresa = tipoempresa,Giro = giro,NombreAsesor=NombreAsesor)
        elif carrera == "LNI":
            return render_template('Cuestionarios/cuestionario_salida_LNI.html',procedimiento=procedimiento, nombreProyecto=nombreProyecto, periodo=periodo, nombre_empresa=nombre_empresa, grado_estudios=grado_estudios, capital=capital, anios_operacion=anios_operacion, tamanio_empresa=tamanio_empresa, mercado_venta=mercado_venta,equipo= equipo,tipoempresa = tipoempresa,Giro = giro,NombreAsesor=NombreAsesor)
    return 'no'

#Función para insertar los datos del cuestionario de salida
def obtenerProcedimientoYCarrera(nombreProyecto):
    query = text("""
    SELECT DISTINCT eq.Procedimiento, e.Carrera
    FROM equipos eq
    INNER JOIN estudiante e ON eq.Matricula = e.Matricula
    INNER JOIN proyecto p ON eq.Id_Proyecto = p.ProyectoID
    WHERE p.Nombre = :nombreProyecto;
    """)
    with engine.connect() as conn:
        resultado = conn.execute(query, {'nombreProyecto': nombreProyecto}).fetchone()
        if resultado:
            return resultado[0], resultado[1]  # Devuelve (procedimiento, carrera)
        else:
            return None, None  # Si no se encuentra el proyecto

@app.route('/vercalificacion02', methods=['POST'])
def vercalificacion02():
    resultado  = cargarCalificaciones02()

    return render_template('perfiles/Coordinacion/vercalificacion02.html', resultado=resultado)


@app.route('/calificacionCompleta08',methods=['POST'])
def calificacionCompleta08():
    try:
        matricula = request.form['Matricula']
        query = text("""
            SELECT * from foest08 where Matricula = :matricula
        """)

        with engine.connect() as conn:
            ok = conn.execute(query,{"matricula":matricula}).fetchall()

            
            if ok:
                for fila in ok:
                    Pregunta1 = fila[1]
                    Pregunta2 = fila[2]
                    Pregunta3 = fila[3]
                    Pregunta4 = fila[4]
                    Pregunta5 = fila[5]
                    Pregunta6 = fila[6]

                    Pregunta7 = fila[7]
                    Pregunta8 = fila[8]
                    Pregunta9 = fila[9]
                    Promedio= fila[10]
                    Veracidad = fila[11]

                    Comentarios = fila[12]
                    Matricula = fila[13]
                 
                   
    except Exception as e:
        return f'Error al cargar las calificaciones: {str(e)}'   
    return render_template('perfiles/Coordinacion/calificacionesCompletas08.html',Pregunta1 = Pregunta1,Pregunta2 = Pregunta2,Pregunta3 = Pregunta3,Pregunta4 = Pregunta4,Pregunta5 = Pregunta5,Pregunta6 = Pregunta6,Pregunta7 = Pregunta7,
                           Pregunta8 = Pregunta8,Pregunta9 = Pregunta9,Promedio = Promedio,Veracidad = Veracidad,Comentarios = Comentarios,Matricula = Matricula)


@app.route('/calificacionCompleta03',methods=['POST'])
def calificacionCompleta03():
    try:
        nombre = request.form['Nombre']
        query = text("""
            SELECT calificacionproyectop1.*,calificacionproyectop2.*,calificacionproyectop3.*
FROM proyecto
JOIN calificacionproyectop1 ON proyecto.Nombre = calificacionproyectop1.Proyecto
JOIN calificacionproyectop2 ON proyecto.Nombre = calificacionproyectop2.Proyecto
JOIN calificacionproyectop3 ON proyecto.Nombre = calificacionproyectop3.Proyecto
WHERE proyecto.Nombre = :Nombre;
        """)

        with engine.connect() as conn:
            ok = conn.execute(query,{"Nombre":nombre}).fetchall()

            
            if ok:
                for fila in ok:
                    Antecedentes = fila[2]
                    Planteamiento = fila[3]
                    Justificacion = fila[4]
                    Objetivos = fila[5]
                    ObjetivosEspecificos = fila[6]
                    PromedioP1 = fila[7]

                    Marco = fila[10]
                    Metodologia = fila[11]
                    Cronograma = fila[12]
                    Desarrollo= fila[13]
                    PromedioP2 = fila[14]

                    Resultados = fila[17]
                    Conclusiones = fila[18]
                    Referencias = fila[19]
                    Anexos = fila[20]
                    PromedioP3 = fila[21]
                   
    except Exception as e:
        return f'Error al cargar las calificaciones: {str(e)}'   
    return render_template('perfiles/Coordinacion/calificacionesCompletas03.html',Antecedentes=Antecedentes,Planteamiento=Planteamiento,Justificacion=Justificacion,
                           Objetivos = Objetivos,ObjetivosEspecificos=ObjetivosEspecificos,PromedioP1 = PromedioP1,Marco = Marco,Metodologia = Metodologia,Cronograma = Cronograma,
                           Desarrollo = Desarrollo,PromedioP2 = PromedioP2,Resultados = Resultados,Conclusiones = Conclusiones,Referencias = Referencias,Anexos = Anexos,PromedioP3 = PromedioP3)

@app.route('/verMasCalificaciones', methods=['POST'])
def verMasCalificaciones():
    return render_template('perfiles/Coordinacion/verCalificaciones.html')

@app.route('/vercalificacion03',methods=['POST'])
def verCalificacion03():
    resultado = cargarCalificaciones03()
    return render_template('perfiles/Coordinacion/vercalificacion03.html',resultado = resultado)

@app.route('/vercalificacion08',methods=['POST'])
def verCalificacion08():
    resultado = cargarCalificaciones08()
    return render_template('perfiles/Coordinacion/vercalificaciones08.html',resultado = resultado)

def cargarCalificaciones08():
    try:
        query = text("""
            SELECT Matricula,Promedio,Comentarios FROM foest08;
        """)
        with engine.connect() as conn:
            rows = conn.execute(query).fetchall()  
            
            if not rows:
                return '<div class="alert alert-warning text-center">No hay datos disponibles</div>'

            resultado = '''
            <div class="table-responsive">
            <table class="table table-bordered text-center align-middle">
                <thead class="table-light">
                    <tr>
                        <th>Matrícula</th>
                        <th>Promedio</th>
                        <th>Comentarios</th>

                   
                    </tr>
                </thead>
                <tbody>
            '''
            for fila in rows:
                resultado += f'''
                <tr>
                    <td>{fila[0]}</td>
                    <td>{fila[1]}</td>
                    <td>{fila[2]}</td>

                    <td>
                        <form action="/calificacionCompleta08" method="post">
                            <input type="hidden" name="Matricula" value="{fila[0]}">
                            <button type="submit" class="btn btn-success btn-sm">Ver calif. completas</button>
                        </form>
                    </td>
                </tr>
                '''
            resultado += '''
                </tbody>
            </table>
            </div>
            '''
            return resultado
    except Exception as e:
        return f'<div class="alert alert-danger text-center">Error al cargar las calificaciones: {str(e)}</div>'



def cargarCalificaciones02():
    try:
        query = text("""
            SELECT foest02.Miembro, estudiante.Nombre1, estudiante.Nombre2, estudiante.ApellidoP, estudiante.ApellidoM,
                   foest02.PromedioActitud, foest02.PromedioDesarrollo 
            FROM estudiante 
            JOIN foest02 ON estudiante.Matricula = foest02.miembro;
        """)
        with engine.connect() as conn:
            rows = conn.execute(query).fetchall()  
            
            if not rows:
                return '<div class="alert alert-warning text-center">No hay datos disponibles</div>'

            resultado = '''
            <div class="table-responsive">
            <table class="table table-bordered text-center align-middle">
                <thead class="table-light">
                    <tr>
                        <th>Matrícula</th>
                        <th>Nombre</th>
                        <th>Segundo Nombre</th>
                        <th>Apellido Paterno</th>
                        <th>Apellido Materno</th>
                        <th>Prom. Actitud</th>
                        <th>Prom. Desarrollo</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
            '''
            for fila in rows:
                resultado += f'''
                <tr>
                    <td>{fila[0]}</td>
                    <td>{fila[1]}</td>
                    <td>{fila[2]}</td>
                    <td>{fila[3]}</td>
                    <td>{fila[4]}</td>
                    <td>{int(fila[5])}</td>
                    <td>{int(fila[6])}</td>
                    <td>
                        <form action="/calificacionCompleta" method="post">
                            <input type="hidden" name="Miembro" value="{fila[0]}">
                            <button type="submit" class="btn btn-success btn-sm">Ver calif. completas</button>
                        </form>
                    </td>
                </tr>
                '''
            resultado += '''
                </tbody>
            </table>
            </div>
            '''
            return resultado
    except Exception as e:
        return f'<div class="alert alert-danger text-center">Error al cargar las calificaciones: {str(e)}</div>'

def cargarCalificaciones03():
    try:
        query = text("""
            SELECT proyecto.Nombre,calificacionproyectop1.Calificacion,calificacionproyectop2.Calificacion,calificacionproyectop3.Calificacion
FROM proyecto
JOIN calificacionproyectop1 ON proyecto.Nombre = calificacionproyectop1.Proyecto
JOIN calificacionproyectop2 ON proyecto.Nombre = calificacionproyectop2.Proyecto
JOIN calificacionproyectop3 ON proyecto.Nombre = calificacionproyectop3.Proyecto;
        """)
        with engine.connect() as conn:
            rows = conn.execute(query).fetchall()  
            
            if not rows:
                return '<div class="alert alert-warning text-center">No hay datos disponibles</div>'

            resultado = '''
            <div class="table-responsive">
            <table class="table table-bordered text-center align-middle">
                <thead class="table-light">
                    <tr>
                        <th>Proyecto</th>
                        <th>Parcial 1</th>
                        <th>Parcial 2</th>
                        <th>Parcial 3</th>
                    </tr>
                </thead>
                <tbody>
            '''
            for fila in rows:
                resultado += f'''
                <tr>
                    <td>{fila[0]}</td>
                    <td>{fila[1]}</td>
                    <td>{fila[2]}</td>
                    <td>{fila[3]}</td>
                 
                    <td>
                        <form action="/calificacionCompleta03" method="post">
                            <input type="hidden" name="Nombre" value="{fila[0]}">

                            <button type="submit" class="btn btn-success btn-sm">Ver calif. completas</button>
                        </form>
                    </td>
                </tr>
                '''
            resultado += '''
                </tbody>
            </table>
            </div>
            '''
            return resultado
    except Exception as e:
        return f'<div class="alert alert-danger text-center">Error al cargar las calificaciones: {str(e)}</div>'


@app.route('/calificacionCompleta', methods=['POST'])
def cargarCalificaciones02Completas():
    try:
        Miembro = request.form['Miembro']
        query = text("""
            SELECT estudiante.Nombre1, estudiante.Nombre2, estudiante.ApellidoP, estudiante.ApellidoM, foest02.*
            FROM estudiante 
            JOIN foest02 ON estudiante.Matricula = foest02.Miembro
            WHERE foest02.Miembro = :miembro
        """)

        with engine.connect() as conn:
            ok = conn.execute(query, {'miembro': Miembro}).fetchall()

            
            if ok:
                for fila in ok:
                    Nombre1 = fila[0]
                    Nombre2 = fila[1]
                    ApellidoP = fila[2]
                    ApellidoM = fila[3]
                    
                    Puntualidad = fila[11]
                    Responsabilidad = fila[12]
                    Etica = fila[13]
                    TomaDecisiones = fila[14]
                    Liderazgo = fila[15]
                    ExpresaIdeas= fila[16]
                    ComunicacionAsertiva = fila[17]
                    ResolucionSituaciones = fila[18]
                    ActitudFavorable = fila[19]
                    TrabajoEquipo = fila[20]
                    promedio_actitud = fila[21]
                    Estrategias = fila[22]
                    AccionesMejora = fila[23]
                    ProcesosOperacion = fila[24]
                    PlanteaSoluciones = fila[25]
                    RespondeNecesidades = fila[26]
                    CumpleTiempos = fila[27]
                    promedio_desarrollo = fila[28]
                    

                    promedio_actitud=int(promedio_actitud)
                    promedio_desarrollo=int(promedio_desarrollo)
    except Exception as e:
        return f'Error al cargar las calificaciones: {str(e)}'


                
    return render_template('perfiles/Coordinacion/calificacionCompleta.html',Puntualidad=Puntualidad, Responsabilidad=Responsabilidad, Etica=Etica, TomaDecisiones=TomaDecisiones, Liderazgo=Liderazgo,ExpresaIdeas=ExpresaIdeas,
                           ComunicacionAsertiva=ComunicacionAsertiva, ResolucionSituaciones=ResolucionSituaciones, ActitudFavorable=ActitudFavorable, TrabajoEquipo=TrabajoEquipo,Estrategias=Estrategias,
                           AccionesMejora=AccionesMejora, ProcesosOperacion=ProcesosOperacion, PlanteaSoluciones=PlanteaSoluciones, RespondeNecesidades=RespondeNecesidades, CumpleTiempos=CumpleTiempos,promedio_actitud=promedio_actitud,promedio_desarrollo=promedio_desarrollo)


@app.route('/AgregarProyectoDesdeAsesor', methods=['POST'])
def AgregarProyectoDesdeAsesor():
    carga = cargarAsesorEmp()
    nombre = request.form['nombre']
    ID = request.form['ID']
    return render_template('perfiles/AsesorAcademico/AgregarProyecto.html', nombre=nombre, ID=ID, cargar=carga)



def obtenerIntegrantes(nombreProyecto):
    query = text("""
        SELECT 
            e.Nombre1, e.Nombre2, e.ApellidoP, e.ApellidoM
        FROM 
            equipos eq
        JOIN 
            estudiante e ON eq.Matricula = e.Matricula
        JOIN 
            proyecto p ON eq.Id_Proyecto = p.ProyectoID
        WHERE 
            p.Nombre = :nombreProyecto;
    """)

    with engine.connect() as conn:
        result = conn.execute(query, {"nombreProyecto": nombreProyecto})
        integrantes = [
            {
                'Nombre1': row[0],
                'Nombre2': row[1],
                'ApellidoP': row[2],
                'ApellidoM': row[3]
            }
            for row in result
        ]
    return integrantes

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
                return render_template('/perfiles/Coordinacion/perfil_coordinacion.html',nombre = nombre,nombre2 = nombre2,apellidoP=apellidoP,apellidoM=apellidoM,correo=correo)
            else:
                return render_template('Error/CoordinacionNoEncontrado.html')
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
                return render_template('Error/CoordinacionNoEncontrado.html')
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
    base_folder = os.path.join('static/Documentos',matricula,parcial)
    UPLOAD_FOLDER = os.path.join(base_folder,'Proyecto')
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    nuevo_nombre = f'proyeto{nombre}{parcial}.pdf'
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

def guardarEquipo(matricula, NoEquipo, ID,Procedimiento):
    try:
        query = text("INSERT INTO equipos (Matricula, NoEquipo, Id_Proyecto,Procedimiento) VALUES (:Matricula,:NoEquipo,:Id_Proyecto,:Procedimiento)")
        with engine.connect() as conn:
            conn.execute(query,{'Matricula':matricula,'NoEquipo':NoEquipo,'Id_Proyecto':ID,'Procedimiento':Procedimiento})
            conn.commit()
            return True
    except Exception as e:
        return ID

def guardarEquipo2(matricula, matricula2, NoEquipo, ID,Procedimiento):
    try:
        query1 = text("INSERT INTO equipos (Matricula, NoEquipo, Id_Proyecto,Procedimiento) VALUES (:Matricula1, :NoEquipo, :Id_Proyecto,:Procedimiento)")
        query2 = text("INSERT INTO equipos (Matricula, NoEquipo, Id_Proyecto,Procedimiento) VALUES (:Matricula2, :NoEquipo, :Id_Proyecto,:Procedimiento)")

        with engine.connect() as conn:
            with conn.begin():  
                conn.execute(query1, {'Matricula1': matricula, 'NoEquipo': NoEquipo, 'Id_Proyecto': ID,'Procedimiento':Procedimiento})
                conn.execute(query2, {'Matricula2': matricula2, 'NoEquipo': NoEquipo, 'Id_Proyecto': ID,'Procedimiento':Procedimiento})
                return True
    except Exception as e:
        return ID

def guardarEquipo3(matricula,matricula2,matricula3, NoEquipo, ID,Procedimiento):
    try:
        query1 = text("INSERT INTO equipos (Matricula, NoEquipo, Id_Proyecto,Procedimiento) VALUES (:Matricula1, :NoEquipo, :Id_Proyecto,:Procedimiento)")
        query2 = text("INSERT INTO equipos (Matricula, NoEquipo, Id_Proyecto,Procedimiento) VALUES (:Matricula2, :NoEquipo, :Id_Proyecto,:Procedimiento)")
        query3 = text("INSERT INTO equipos (Matricula, NoEquipo, Id_Proyecto,Procedimiento) VALUES (:Matricula3, :NoEquipo, :Id_Proyecto,:Procedimiento)")

        with engine.connect() as conn:
            with conn.begin():  
                conn.execute(query1, {'Matricula1': matricula, 'NoEquipo': NoEquipo, 'Id_Proyecto': ID,'Procedimiento':Procedimiento})
                conn.execute(query2, {'Matricula2': matricula2, 'NoEquipo': NoEquipo, 'Id_Proyecto': ID,'Procedimiento':Procedimiento})
                conn.execute(query3, {'Matricula3': matricula3, 'NoEquipo': NoEquipo, 'Id_Proyecto': ID,'Procedimiento':Procedimiento})
                return True
    except Exception as e:
        return ID

def guardarEquipo4(matricula,matricula2,matricula3,matricula4, NoEquipo, ID,Procedimiento):
    try:
        query1 = text("INSERT INTO equipos (Matricula, NoEquipo, Id_Proyecto,Procedimiento) VALUES (:Matricula1, :NoEquipo, :Id_Proyecto,:Procedimiento)")
        query2 = text("INSERT INTO equipos (Matricula, NoEquipo, Id_Proyecto,Procedimiento) VALUES (:Matricula2, :NoEquipo, :Id_Proyecto,:Procedimiento)")
        query3 = text("INSERT INTO equipos (Matricula, NoEquipo, Id_Proyecto,Procedimiento) VALUES (:Matricula3, :NoEquipo, :Id_Proyecto,:Procedimiento)")
        query4 = text("INSERT INTO equipos (Matricula, NoEquipo, Id_Proyecto,Procedimiento) VALUES (:Matricula4, :NoEquipo, :Id_Proyecto,:Procedimiento)")

        with engine.connect() as conn:
            with conn.begin():  
                conn.execute(query1, {'Matricula1': matricula, 'NoEquipo': NoEquipo, 'Id_Proyecto': ID,'Procedimiento':Procedimiento})
                conn.execute(query2, {'Matricula2': matricula2, 'NoEquipo': NoEquipo, 'Id_Proyecto': ID,'Procedimiento':Procedimiento})
                conn.execute(query3, {'Matricula3': matricula3, 'NoEquipo': NoEquipo, 'Id_Proyecto': ID,'Procedimiento':Procedimiento})
                conn.execute(query4, {'Matricula4': matricula4, 'NoEquipo': NoEquipo, 'Id_Proyecto': ID,'Procedimiento':Procedimiento})
                return True
    except Exception as e:
        return ID

def guardarEquipo5(matricula, matricula2, matricula3, matricula4, matricula5, NoEquipo, ID,Procedimiento):
    try:
        query1 = text("INSERT INTO equipos (Matricula, NoEquipo, Id_Proyecto,Procedimiento) VALUES (:Matricula1, :NoEquipo, :Id_Proyecto,:Procedimiento)")
        query2 = text("INSERT INTO equipos (Matricula, NoEquipo, Id_Proyecto,Procedimiento) VALUES (:Matricula2, :NoEquipo, :Id_Proyecto,:Procedimiento)")
        query3 = text("INSERT INTO equipos (Matricula, NoEquipo, Id_Proyecto,Procedimiento) VALUES (:Matricula3, :NoEquipo, :Id_Proyecto,:Procedimiento)")
        query4 = text("INSERT INTO equipos (Matricula, NoEquipo, Id_Proyecto,Procedimiento) VALUES (:Matricula4, :NoEquipo, :Id_Proyecto,:Procedimiento)")
        query5 = text("INSERT INTO equipos (Matricula, NoEquipo, Id_Proyecto,Procedimiento) VALUES (:Matricula5, :NoEquipo, :Id_Proyecto,:Procedimiento)")

        with engine.connect() as conn:
            with conn.begin():
                conn.execute(query1, {'Matricula1': matricula, 'NoEquipo': NoEquipo, 'Id_Proyecto': ID,'Procedimiento':Procedimiento})

                conn.execute(query2, {'Matricula2': matricula2, 'NoEquipo': NoEquipo, 'Id_Proyecto': ID,'Procedimiento':Procedimiento})

                conn.execute(query3, {'Matricula3': matricula3, 'NoEquipo': NoEquipo, 'Id_Proyecto': ID,'Procedimiento':Procedimiento})

                conn.execute(query4, {'Matricula4': matricula4, 'NoEquipo': NoEquipo, 'Id_Proyecto': ID,'Procedimiento':Procedimiento})

                conn.execute(query5, {'Matricula5': matricula5, 'NoEquipo': NoEquipo, 'Id_Proyecto': ID,'Procedimiento':Procedimiento})
                return True
    except Exception as e:
        return ID 


def cargarEquipo(Id_Proyecto):
    try:
        query = text("SELECT NoEquipo FROM equipos WHERE Id_Proyecto = :Id_Proyecto")
        with engine.connect() as conn:
            ok= conn.execute(query, {'Id_Proyecto': Id_Proyecto}).fetchone()
            if ok:
                ID = ok[0]
                return ID
            else:
                return 'no encontado'
    except Exception as e:
            return f'error {e}'

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
    IDAsesor = request.form['IDAsesor']
    proyecto = request.form['proyecto']
    validado = validarCalificado(proyecto)
    Antecedentes = int(request.form['Antecedentes'])
    Planteamiento = int(request.form['Planteamiento'])
    Justificacion = int(request.form['Justificacion'])
    Objetivo = int(request.form['Objetivo'])
    ObjetivoEspecifico = int(request.form['ObjetivoEspecifico'])

    Calificacion = (Antecedentes+Planteamiento+Justificacion+Objetivo+ObjetivoEspecifico)/5
    if validado:
        return render_template('cargas/calificacion.html',matricula = Matricula,Calificacion = Calificacion,proyecto=proyecto,Antecedentes = Antecedentes,Planteamiento = Planteamiento,Justificacion = Justificacion,Objetivo = Objetivo,ObjetivoEspecifico = ObjetivoEspecifico,IDAsesor = IDAsesor)
    else:
        calificado = calificar(proyecto,Antecedentes,Planteamiento,Justificacion,Objetivo,ObjetivoEspecifico,Calificacion)
        if calificado:
            return render_template('Cargas/calificacionAsignada.html',Calificacion = Calificacion,proyecto = proyecto,IDAsesor = IDAsesor)
            
        
@app.route('/calificarProyectoU2',methods=['POST'])
def calificarProyectoU2():
    Matricula = request.form['matriculau2']
    IDAsesor = request.form['IDAsesor']
    proyecto = request.form['proyecto']
    validado = validarCalificadoU2(proyecto)
    Marco = int(request.form['Marco'])
    Metodologia = int(request.form['Metodologia'])
    Cronograma = int(request.form['Cronograma'])
    DesarrolloProyecto = int(request.form['DesarrolloProyecto'])
    Calificacion = (Marco+Metodologia+Cronograma+DesarrolloProyecto)/4
    if validado:
        return render_template('cargas/calificacionp2.html',matricula = Matricula,proyecto = proyecto,Calificacion = Calificacion,Marco = Marco,Metodologia = Metodologia,Cronograma = Cronograma,DesarrolloProyecto = DesarrolloProyecto,IDAsesor = IDAsesor)
    else:
        calificado = calificarp2(proyecto,Marco,Metodologia,Cronograma,DesarrolloProyecto,Calificacion)
        if calificado:
            return render_template('Cargas/calificacionAsignada.html',Calificacion = Calificacion,proyecto = proyecto,IDAsesor = IDAsesor)
            
        
        

        

@app.route('/calificarProyectoU3',methods=['POST'])
def calificarProyectoU3():
    IDAsesor = request.form['IDAsesor']
    Matricula = request.form['matriculau3']
    proyecto = request.form['proyecto']
    validado = validarCalificadoU3(proyecto)
    Resultados = int(request.form['Resultados'])
    Conclusiones = int(request.form['Conclusiones'])
    Referencias = int(request.form['Referencias'])
    Anexos = int(request.form['Anexos'])
    Calificacion = (Resultados+Conclusiones+Referencias+Anexos)/4
    if validado:
        return render_template('cargas/calificacionp3.html',matricula = Matricula,proyecto = proyecto,Calificacion = Calificacion,Resultados = Resultados,Conclusiones = Conclusiones,Referencias = Referencias,Anexos = Anexos,IDAsesor = IDAsesor)
    else:
        calificado = calificarp3(proyecto,Resultados,Conclusiones,Referencias,Anexos,Calificacion)
        if calificado:
            return render_template('Cargas/calificacionAsignada.html',Calificacion=Calificacion,proyecto = proyecto,IDAsesor = IDAsesor)
    


def calificar(proyecto,antecedentes,planteamiento,justificacion,objetivos,especificos,calificacion):
    try:
        query = text("INSERT INTO calificacionproyectop1 (proyecto,antecedentes,planteamiento,justificacion,objetivos,objetivosEspecificos,Calificacion) VALUES (:proyecto,:antecedentes,:planteamiento,:justificacion,:objetivos,:objetivosEspecificos,:Calificacion)")
        with engine.connect() as conn:
            conn.execute(query,{"proyecto":proyecto,"antecedentes":antecedentes,"planteamiento":planteamiento,"justificacion":justificacion,"objetivos":objetivos,"objetivosEspecificos":especificos,"Calificacion":calificacion})
            conn.commit()
            return True
    except Exception as e:
        return f'error---------------->{e}'
    
def calificarp2(proeycto,marco,metodologia,cronograma,desarrollo,calificacion):
    try:
        query = text("INSERT INTO calificacionproyectop2 (proyecto,Marco,Metodologia,Cronograma,Desarrollo,Calificacion) VALUES (:proyecto,:Marco,:metodologia,:cronograma,:desarrollo,:Calificacion)")
        with engine.connect() as conn:
            conn.execute(query,{"proyecto":proeycto,"Marco":marco,"metodologia":metodologia,"cronograma":cronograma,"desarrollo":desarrollo,"Calificacion":calificacion})
            conn.commit()
            return True
    except Exception as e:
        return f'error---------------->{e}'
    

def calificarp3(proyecto,Resultados,Conclusiones,Referencias,Anexos,Calificacion):
    try:
        query = text("INSERT INTO calificacionproyectop3 (proyecto,Resultados,Conclusiones,Referencias,Anexos,Calificacion) VALUES (:proyecto,:Resultados,:Conclusiones,:Referencias,:Anexos,:Calificacion)")
        with engine.connect() as conn:
            conn.execute(query,{"proyecto":proyecto,"Resultados":Resultados,"Conclusiones":Conclusiones,"Referencias":Referencias,"Anexos":Anexos,"Calificacion":Calificacion})
            conn.commit()
            return True
    except Exception as e:
        return f'error---------------->{e}'
    

def validarCalificado(proyecto):
    try:
        query = text("SELECT proyecto FROM calificacionproyectop1 WHERE proyecto =:proyecto")
        with engine.connect() as conn:
            ok = conn.execute(query,{'proyecto':proyecto})
            ok = ok.fetchone()
            if ok:
                return True
            else:
                return False
    except Exception as e:
        return f'error---------------->{e}'  


def validarCalificadoU2(proyecto):
    try:
        query = text("SELECT proyecto FROM calificacionproyectop2 WHERE proyecto =:proyecto")
        with engine.connect() as conn:
            ok = conn.execute(query,{'proyecto':proyecto})
            ok = ok.fetchone()
            if ok:
                return True
            else:
                return False
    except Exception as e:
        return f'error---------------->{e}'   



@app.route('/regresarAsesorAcademico',methods=['POST'])
def regresarAsesorAcademico():
    ID = request.form['ID']
    resultado = cargarProyectosAsesor(ID)
    return render_template('/perfiles/AsesorAcademico/revisar_expediente.html',resultado = resultado,ID = ID) 



def validarCalificadoU3(proyecto):
    try:
        query = text("SELECT proyecto FROM calificacionproyectop3 WHERE proyecto =:proyecto")
        with engine.connect() as conn:
            ok = conn.execute(query,{'proyecto':proyecto})
            ok = ok.fetchone()
            if ok:
                return True
            else:
                return False
    except Exception as e:
        return f'error---------------->{e}'   
 
def verificar_encuesta_existente(matricula):
    try:
        query = text("SELECT COUNT(*) FROM foest08 WHERE Matricula = :Matricula")
        with engine.connect() as conn:
            result = conn.execute(query, {'Matricula': matricula}).scalar()
            return result > 0
    except Exception as e:
        return f'error---------------->{e}'
    
def encuestaSatisfaccion():
    Matricula = request.form['Matricula']
    Correo = request.form['correo']
    
    # Verificar si ya existe una encuesta
    if verificar_encuesta_existente(Matricula):
        return render_template('Cargas/mensaje_encuesta_existente.html', 
                             mensaje="Ya has completado la encuesta anteriormente.")
    
    return render_template('Cuestionarios/evaluacion_cuestionario.html',
                         Matricula=Matricula, correo=Correo)

def guardarForm08(question11,question12,question13,question14,question15,question16,question17,question18,question19,prom,veracidad,matricula):
    try:
        query = text("INSERT INTO foest08 (Pregunta01,Pregunta02,Pregunta03,Pregunta04,Pregunta05,Pregunta06,Pregunta07,Pregunta08,Pregunta09, Promedio, Veracidad, Matricula) VALUES (:Pregunta01, :Pregunta02, :Pregunta03,:Pregunta04,:Pregunta05,:Pregunta06,:Pregunta07,:Pregunta08,:Pregunta09, :Promedio,:Veracidad,:Matricula)")
        with engine.connect() as conn:
            conn.execute(query,{'Pregunta01':question11,'Pregunta02':question12,'Pregunta03':question13,'Pregunta04':question14,'Pregunta05':question15,'Pregunta06':question16,'Pregunta07':question17,'Pregunta08':question18,'Pregunta09':question19,'Promedio':prom,'Veracidad':veracidad,'Matricula':matricula})
            conn.commit()
            return True
    except Exception as e:
        return f'error---------------->{e}'


def guardarForm08C(question11,question12,question13,question14,question15,question16,question17,question18,question19,prom,veracidad,Comentarios,matricula,periodo,anio):
    try:
        query = text("INSERT INTO foest08 (Pregunta01,Pregunta02,Pregunta03,Pregunta04,Pregunta05,Pregunta06,Pregunta07,Pregunta08,Pregunta09, Promedio, Veracidad,Comentarios, Matricula, Periodo) VALUES (:Pregunta01, :Pregunta02, :Pregunta03,:Pregunta04,:Pregunta05,:Pregunta06,:Pregunta07,:Pregunta08,:Pregunta09, :Promedio,:Veracidad,:Comentarios,:Matricula,:Periodo)")
        with engine.connect() as conn:
            conn.execute(query,{'Pregunta01':question11,'Pregunta02':question12,'Pregunta03':question13,'Pregunta04':question14,'Pregunta05':question15,'Pregunta06':question16,'Pregunta07':question17,'Pregunta08':question18,'Pregunta09':question19,'Promedio':prom,'Veracidad':veracidad,'Comentarios':Comentarios,'Matricula':matricula, 'Periodo':periodo+ "-" +anio})
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
        query = text("SELECT Id,Nombre1,Nombre2,ApellidoP,ApellidoM FROM asesoracademico WHERE password = :password AND Correo =:correo")
        with engine.connect() as conn:
            ok= conn.execute(query, {'password': password,'correo':correo}).fetchone()
            if ok:
                
                ID = ok[0]
                nombre = ok[1]
                nombre2 = ok[2]
                apellidoP = ok[3]
                apellidoM = ok[4]


                
                resultado = cargarProyectosAsesor(ID)
                return render_template('/perfiles/AsesorAcademico/revisar_expediente.html',resultado = resultado,ID = ID, nombre=nombre,nombre2=nombre2,apellidoP=apellidoP,apellidoM=apellidoM,correo=correo)
                
            else:
                return render_template('Error/AsesorNoEncontrado.html')
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
    
def obtenerRutaPDF2(proyecto, parcial):
    try:
        query = text("SELECT Proyecto FROM documentos WHERE NombreProyecto = :NombreProyecto AND Parcial = :parcial")
        with engine.connect() as conn:
            ok = conn.execute(query, {'NombreProyecto': proyecto, 'parcial': parcial})
            ruta = ok.fetchone()
            if ruta:
                return ruta[0]
            else:
                return None  # No se encontró la ruta
    except Exception as e:
        return f'Error al obtener la ruta del PDF: {e}'
def verificarAsignacionProyecto(Matricula):
    try:
        query = text("SELECT matricula FROM Equipos WHERE Matricula = :Matricula")
        with engine.connect() as conn:
            ok= conn.execute(query,{'Matricula':Matricula})
            succ = ok.fetchone()
            if succ:
                return True
            else:
                return False
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
        
        return url_for('static', filename=f"temp/{image_filename}")
    except Exception as e:
        return False



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
    asignarContraseñaAcademico()
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
    
def listaEstudiantes(Proyecto):
    query = text("""SELECT estudiante.Nombre1, estudiante.Nombre2, estudiante.ApellidoP, estudiante.ApellidoM
                FROM estudiante
                JOIN equipos ON equipos.Matricula = estudiante.Matricula
                WHERE equipos.Id_Proyecto = :Proyecto;""")
    with engine.connect() as conn:
        ok= conn.execute(query,{'Proyecto':Proyecto})
        ok = ok.fetchall()
        
        opciones = ''.join([f'<li>{row[0]} {row[1]} {row[2]} {row[3]}</li>' for row in ok])      
        return opciones

def periodoCuatrimestral():
    query= text("SELECT * FROM periodos WHERE Estado = 'activo'")
    with engine.connect() as conn:
        ok= conn.execute(query)
        ok = ok.fetchone()
        if ok:
            return ok[1]
        else:
            return 'No hay periodo activo'

def cargarCarrera(ProyectoID):
    query = text("SELECT e.Carrera FROM estudiante e JOIN equipos eq ON e.Matricula = eq.Matricula WHERE eq.Id_Proyecto = :id")
    with engine.connect() as conn:
        ok = conn.execute(query, {"id": ProyectoID})
        ok = ok.fetchone()
        if ok:
            return ok[0]
        else:
            return 'El estudiante no cuenta con una carrera asignada'

# def cargarEtapa(ProyectoID):
#     query = text("SELECT DISTINCT p.Procedimiento AS Etapa FROM proyectoasesores pa JOIN equipos eq ON pa.Id_proyecto = eq.Id_Proyecto JOIN procedimientos p ON eq.Procedimiento = p.idProcedimiento WHERE pa.Id_asesorE = :id")
#     with engine.connect() as conn:
#         ok = conn.execute(query, {"id": ProyectoID})
#         ok = ok.fetchone()
#         if ok:
#             return ok[0]
#         else:
#             return 'No cuenta con una etapa asignada'
    

@app.route('/asignarContraseñas',methods=['POST'])
def asignarContraseñaAcademico():
    query = text("UPDATE asesoracademico SET password = Correo WHERE password = ' '")
    with engine.connect() as conn:
        conn.execute(query)
        conn.commit()

def limpiar_temp():
    carpeta_temp = 'static/temp'
    if not os.path.exists(carpeta_temp):
        os.makedirs(carpeta_temp)
    for archivo in os.listdir(carpeta_temp):
        ruta_archivo = os.path.join(carpeta_temp, archivo)
        if os.path.isfile(ruta_archivo):
            os.remove(ruta_archivo)

def proyectoAsesorEmpr(equipo):
    query = text("""SELECT pro.Nombre
FROM asesorempresarial ase
JOIN proyectoasesores p ON p.Id_asesorE = ase.AsesorID
JOIN proyecto pro ON pro.ProyectoID = p.Id_proyecto
WHERE pro.ProyectoID = :equipo;""")
    with engine.connect() as conn:
        ok= conn.execute(query,{'equipo':equipo})
        ok = ok.fetchone()
        if ok:
            return ok[0]
        else:
            return 'No asignado'
    
def cargarEmpresaEquipo(equipo):
    query = text("""SELECT ase.Empresa
FROM asesorempresarial ase
JOIN proyectoasesores p ON p.Id_asesorE = ase.AsesorID
JOIN proyecto pro ON pro.ProyectoID = p.Id_proyecto
WHERE pro.ProyectoID = :equipo;""")
    with engine.connect() as conn:
        ok= conn.execute(query,{'equipo':equipo})
        ok = ok.fetchone()
        if ok:
            return ok[0]
        else:
            return 'No asignado'
    
def NombreAsesor(equipo):
    query = text("""SELECT ase.Nombre1, Nombre2, ApellidoP, ApellidoM
FROM asesorempresarial ase
JOIN proyectoasesores p ON p.Id_asesorE = ase.AsesorID
JOIN proyecto pro ON pro.ProyectoID = p.Id_proyecto
WHERE pro.ProyectoID = :equipo;""")
    
    with engine.connect() as conn:
        ok = conn.execute(query, {'equipo': equipo}).fetchone()        
        if not ok:
            return '<p>No se encontró información del asesor</p>'
        
        nombre, nombre2, apellidoP, apellidoM = ok
        opciones = f'<input type="text" value="{nombre} {nombre2} {apellidoP} {apellidoM}" disabled />'
        
        return opciones

def NombreAsesorOculto(equipo):
    query = text("""SELECT ase.Nombre1, Nombre2, ApellidoP, ApellidoM
FROM asesorempresarial ase
JOIN proyectoasesores p ON p.Id_asesorE = ase.AsesorID
JOIN proyecto pro ON pro.ProyectoID = p.Id_proyecto
WHERE pro.ProyectoID = :equipo;""")
    
    with engine.connect() as conn:
        ok = conn.execute(query, {'equipo': equipo}).fetchone()        
        if not ok:
            return '<p>No se encontró información del asesor</p>'
        
        nombre, nombre2, apellidoP, apellidoM = ok
        opciones = f'{nombre} {nombre2} {apellidoP} {apellidoM}'
        
        return opciones

def obtenerMatriculas(nombreP):
    query = text("""
    SELECT 
    e.Carrera AS CarreraAlumno
    FROM estudiante e
    INNER JOIN equipos eq ON e.Matricula = eq.Matricula
    INNER JOIN proyecto p ON eq.Id_Proyecto = p.ProyectoID
    WHERE p.Nombre = :nombreP;""")
    with engine.connect() as conn:
        ok = conn.execute(query, {'nombreP': nombreP})
        rows = ok.fetchall()
        carreras = [row[0] for row in rows]  # Extraer solo el valor de la columna CarreraAlumno
        return carreras if carreras else []
        


@app.route('/correccionNo',methods=['POST'])
def correccionNo():
    ID = request.form['IDAsesor']
    resultado = cargarProyectosAsesor(ID)
    return render_template('/perfiles/AsesorAcademico/revisar_expediente.html',resultado = resultado,ID = ID)

    

@app.route('/correccionSi',methods=['POST'])
def correccion():
    proyecto = request.form['proyecto']
    IDAsesor = request.form['IDAsesor']
    calificacionN = request.form['Calificacion']
    antecedentes = request.form['Antecedentes']
    planteamiento = request.form['Planteamiento']
    justificacion = request.form['Justificacion']
    objetivos = request.form['Objetivo']
    objetivosEspecificos = request.form['ObjetivoEspecifico']
    
    correccion = correccionSiP1(antecedentes,planteamiento,justificacion,objetivos,objetivosEspecificos,calificacionN,proyecto)
    if correccion:
        return render_template('Cargas/corregido.html',Calificacion = calificacionN,IDAsesor = IDAsesor)
    else:
        return f'no se pudo corregir {calificacionN}'
    

@app.route('/correccionSiP2',methods=['POST'])
def correccionP2():
    proyecto = request.form['proyecto']
    IDAsesor = request.form['IDAsesor']
    calificacionN = request.form['Calificacion']
    Marco = request.form['Marco']
    Metodologia = request.form['Metodologia']
    Cronograma = request.form['Cronograma']
    DesarrolloProyecto = request.form['DesarrolloProyecto']

   
    correccion = correccionSiP2(Marco,Metodologia,Cronograma,DesarrolloProyecto,calificacionN,proyecto)
    if correccion:
        return render_template('Cargas/corregido.html',Calificacion = calificacionN,IDAsesor = IDAsesor)
    else:
        return f'no se pudo corregir {calificacionN}'


@app.route('/correccionSiP3',methods=['POST'])
def correccionP3():
    proyecto = request.form['proyecto']
    IDAsesor = request.form['IDAsesor']
    calificacionN = request.form['Calificacion']
    Resultados = request.form['Resultados']
    Conclusiones = request.form['Conclusiones']
    Referencias = request.form['Referencias']
    Anexos = request.form['Anexos']

    matricula = request.form['matricula']
    correccion = correccionSiP3(Resultados,Conclusiones,Referencias,Anexos,calificacionN,proyecto)
    if correccion:
        return render_template('Cargas/corregido.html',Calificacion = calificacionN,IDAsesor = IDAsesor)
    else:
        return f'no se pudo corregir {calificacionN}'

def correccionSiP1(antecedentes,planteamiento,justificacion,objetivos,objetivosEspecificos,calificacion,proyecto):
    query = text("UPDATE calificacionproyectop1 SET Antecedentes = :antecedentes,Planteamiento = :planteamiento,Justificacion = :justificacion,Objetivos = :objetivos,ObjetivosEspecificos = :objetivosEspecificos,Calificacion = :calificacion WHERE proyecto = :proyecto")
    try:
        with engine.connect() as conn:
            with conn.begin():
                conn.execute(query,{"antecedentes":antecedentes,"planteamiento":planteamiento,"justificacion":justificacion,"objetivos":objetivos,"objetivosEspecificos":objetivosEspecificos,"calificacion":calificacion,"proyecto":proyecto})    
            return True
    except Exception as e:
        return False
    
def correccionSiP2(Marco,Metodologia,Cronograma,DesarrolloProyecto,calificacion,proyecto):
    query = text("UPDATE calificacionproyectop2 SET Marco = :Marco,Metodologia = :Metodologia,Cronograma = :Cronograma,Desarrollo = :DesarrolloProyecto,Calificacion = :calificacion WHERE proyecto = :proyecto")
    try:
        with engine.connect() as conn:
            with conn.begin():
                conn.execute(query,{"Marco":Marco,"Metodologia":Metodologia,"Cronograma":Cronograma,"DesarrolloProyecto":DesarrolloProyecto,"calificacion":calificacion,"proyecto":proyecto})    
            return True
    except Exception as e:
        return False
    
def correccionSiP3(Resultados,Conclusiones,Referencias,Anexos,calificacion,proyecto):
    query = text("UPDATE calificacionproyectop3 SET Resultados = :Resultados,Conclusiones = :Conclusiones,Referencias = :Referencias,Anexos = :Anexos,Calificacion = :calificacion WHERE proyecto = :proyecto")
    try:
        with engine.connect() as conn:
            with conn.begin():
                conn.execute(query,{"Resultados":Resultados,"Conclusiones":Conclusiones,"Referencias":Referencias,"Anexos":Anexos,"calificacion":calificacion,"proyecto":proyecto})    
            return True
    except Exception as e:
        return False

@app.route('/redireccionMenu',methods=['POST'])
def redireccion():
    ID = request.form['IDAsesor']
    resultado = cargarProyectosAsesor(ID)
    return render_template('/perfiles/AsesorAcademico/revisar_expediente.html',resultado = resultado,ID = ID)


@app.route('/estancia1',methods=['POST'])
def estancia1():
    modalidad = request.form['modalidad']
    giro = request.form['Giro']
    NombreAsesor = request.form['NombreAsesor']
    carrera = request.form['carrera']
    tipoempresa = request.form['tipoempresa']
    equipo = request.form['equipo']
    procedimiento = request.form['procedimiento']
    periodo = request.form['periodo']
    funcionestancia1_otros = request.form.get("funcion-estancia1_otros")
    Nombreproyecto = request.form['nombreProyecto']
    empresa= request.form['nombre_empresa']
    gradoEstudios = request.form['grado_estudios']
    
    capital = request.form['capital']
    anios_operacion = request.form['anios_operacion']
    tamanio_empresa = request.form['tamanio_empresa']
    mercado = request.form['mercado_venta']
    funcionEstancia = request.form.getlist('funcion-estancia1[]')
   
    if len(funcionEstancia) !=3:
        return "Error: deben de ser 3 funciones"
    funcionEstancia1 = funcionEstancia[0]
    funcionEstancia2 = funcionEstancia[1]
    funcionEstancia3 = funcionEstancia[2]

    if funcionEstancia3 == "Otras funciones":
        funcionEstancia3 = funcionestancia1_otros


    resolvio = request.form['resolvio_necesidad']
    interes = request.form['interes_participar']
    investigacion = request.form['investigacion_desarrollo']
    contratar_egresados = request.form['contratar_egresados']
    porque = request.form['porque_contratar']
    aprueba = request.form['Aprueba']
    clausula_especial = request.form.get('clausula_especial')
   
    
    

    #comprobar si no se ha contestado antes
    sql = text("SELECT TituloProyecto,Procedimiento FROM foest07")
    with engine.connect() as conn:
        result = conn.execute(sql)
        rows = result.fetchall()
        for row in rows:
            if row[0] == Nombreproyecto and row[1] == procedimiento:
                return f'Error: ya se ha registrado el proyecto {Nombreproyecto} con el procedimiento {procedimiento}'

    fo07 = guardarFOEST07(periodo,Nombreproyecto,equipo,procedimiento,empresa,modalidad,gradoEstudios,NombreAsesor,tipoempresa,giro,capital,anios_operacion,tamanio_empresa,mercado,carrera,funcionEstancia1,funcionEstancia2,funcionEstancia3)
    if fo07:
        return render_template('login/asesorEmpresarial3.html')

     
    
@app.route('/estancia2',methods=['POST'])
def estancia2():
    modalidad = request.form['modalidad']
    giro = request.form['Giro']
    NombreAsesor = request.form['NombreAsesor']
    carrera = request.form['carrera']
    tipoempresa = request.form['tipoempresa']
    equipo = request.form['equipo']
    procedimiento = request.form['procedimiento']
    periodo = request.form['periodo']
    Nombreproyecto = request.form['nombreProyecto']
    empresa= request.form['nombre_empresa']
    gradoEstudios = request.form['grado_estudios']
    
    capital = request.form['capital']
    anios_operacion = request.form['anios_operacion']
    tamanio_empresa = request.form['tamanio_empresa']
    mercado = request.form['mercado_venta']
    funcionEstancia = request.form.getlist('funcion-estancia2[]')
    if len(funcionEstancia) !=3:
        return "Error: deben de ser 3 funciones"
    funcionEstancia1 = funcionEstancia[0]
    funcionEstancia2 = funcionEstancia[1]
    funcionEstancia3 = funcionEstancia[2]
    
    resolvio = request.form['resolvio_necesidad']
    interes = request.form['interes_participar']
    investigacion = request.form['investigacion_desarrollo']
    contratar_egresados = request.form['contratar_egresados']
    porque = request.form['porque_contratar']
    aprueba = request.form['Aprueba']
    clausula_especial = request.form.get('clausula_especial')
    if aprueba == "No":
        funcionEstancia3 = clausula_especial
  

    fo07 = guardarFOEST07(periodo,Nombreproyecto,equipo,procedimiento,empresa,modalidad,gradoEstudios,NombreAsesor,tipoempresa,giro,capital,anios_operacion,tamanio_empresa,mercado,carrera,funcionEstancia1,funcionEstancia2,funcionEstancia3)
    if fo07:
        return render_template('login/asesorEmpresarial3.html')

    


@app.route('/estadia',methods=['POST'])
def estadia():
    modalidad = request.form['modalidad']
    giro = request.form['Giro']
    NombreAsesor = request.form['NombreAsesor']
    carrera = request.form['carrera']
    tipoempresa = request.form['tipoempresa']
    equipo = request.form['equipo']
    procedimiento = request.form['procedimiento']
    periodo = request.form['periodo']
    Nombreproyecto = request.form['nombreProyecto']
    empresa= request.form['nombre_empresa']
    gradoEstudios = request.form['grado_estudios']
    
    capital = request.form['capital']
    anios_operacion = request.form['anios_operacion']
    tamanio_empresa = request.form['tamanio_empresa']
    mercado = request.form['mercado_venta']
    funcionEstancia = request.form.getlist('funcion-estadia[]')
    if len(funcionEstancia) !=3:
        return f"Error: deben de ser 3 funciones"
    funcionEstancia1 = funcionEstancia[0]
    funcionEstancia2 = funcionEstancia[1]
    funcionEstancia3 = funcionEstancia[2]
    
    resolvio = request.form['resolvio_necesidad']
    interes = request.form['interes_participar']
    investigacion = request.form['investigacion_desarrollo']
    contratar_egresados = request.form['contratar_egresados']
    porque = request.form['porque_contratar']
    aprueba = request.form['Aprueba']
    clausula_especial = request.form.get('clausula_especial')
    if aprueba == "No":
        funcionEstancia3 = clausula_especial
  

    fo07 = guardarFOEST07(periodo,Nombreproyecto,equipo,procedimiento,empresa,modalidad,gradoEstudios,NombreAsesor,tipoempresa,giro,capital,anios_operacion,tamanio_empresa,mercado,carrera,funcionEstancia1,funcionEstancia2,funcionEstancia3)
    if fo07:
        return render_template('login/asesorEmpresarial3.html')

    

def guardarFOEST07(Periodo, TituloProyecto, NoEquipo, Procedimiento, NombreEmpresa, Modalidad, GradoEstudiosAsesorEmp, NombreAsesorEmp, TipoEmpresa, GiroEmpresa, Capital, AniosOperacion, TamanioEmpresa, MercadoVenta, Carrera, funcionEstancia1, funcionEstancia2, funcionEstancia3):
    query = text("""
        INSERT INTO foest07 
        (Periodo, TituloProyecto, NoEquipo, Procedimiento, NombreEmpresa, Modalidad, GradoEstudiosAsesorEmp, NombreAsesorEmp, TipoEmpresa, GiroEmpresa, Capital, AniosOperacion, TamanioEmpresa, MercadoVenta, Carrera, FuncionesPrioritarias, FuncionesPrioritarias2, FuncionesPrioritarias3)
        VALUES 
        (:Periodo, :TituloProyecto, :NoEquipo, :Procedimiento, :NombreEmpresa, :Modalidad, :GradoEstudiosAsesorEmp, :NombreAsesorEmp, :TipoEmpresa, :GiroEmpresa, :Capital, :AniosOperacion, :TamanioEmpresa, :MercadoVenta, :Carrera, :funcionEstancia1, :funcionEstancia2, :funcionEstancia3)
    """)

    try:
        with engine.connect() as conn:
            with conn.begin():
                conn.execute(query, {
                    "Periodo": Periodo,
                    "TituloProyecto": TituloProyecto,
                    "NoEquipo": NoEquipo,
                    "Procedimiento": Procedimiento,
                    "NombreEmpresa": NombreEmpresa,
                    "Modalidad": Modalidad,
                    "GradoEstudiosAsesorEmp": GradoEstudiosAsesorEmp,
                    "NombreAsesorEmp": NombreAsesorEmp,
                    "TipoEmpresa": TipoEmpresa,
                    "GiroEmpresa": GiroEmpresa,
                    "Capital": Capital,
                    "AniosOperacion": AniosOperacion,
                    "TamanioEmpresa": TamanioEmpresa,
                    "MercadoVenta": MercadoVenta,
                    "Carrera": Carrera,
                    "funcionEstancia1": funcionEstancia1,
                    "funcionEstancia2": funcionEstancia2,
                    "funcionEstancia3": funcionEstancia3
                })
                
        return True  
    except Exception as e:
        return f"Error al insertar en foest07: {e}"
         
@app.route('/verproyectos',methods=['POST'])
def verproyectos():
    proyectos = cargarproyectoscoordinacion()
    return render_template('perfiles/Coordinacion/proyectos.html', proyectos = proyectos)

def cargarproyectoscoordinacion():
    query = text("SELECT NombreProyecto FROM documentos WHERE Parcial = 'Parcial 3'")
    with engine.connect() as conn:
        ok = conn.execute(query)
        rows = ok.fetchall()

        if rows:
            tarjetas = ''
            total = len(rows)

            for row in rows:
                nombre = row[0]
                tarjetas += f'''
                <div class="col-md-4 col-sm-6 col-10 mb-4 d-flex justify-content-center">
                    <div class="card text-center shadow-sm proyecto-card">
                        <div class="card-body d-flex flex-column justify-content-between">
                            <h5 class="card-title fw-bold">{nombre}</h5>
                            <form action="/abrirproyectoruta" method="post">
                                <input type="hidden" name="nombre" value="{nombre}">
                                <button type="submit" class="btn btn-success mt-3">Abrir</button>
                            </form>
                        </div>
                    </div>
                </div>
                '''

            # Calcular cuántas tarjetas vacías se necesitan para completar la fila
            sobrantes = (3 - (total % 3)) % 3  # Para evitar 3 si ya es múltiplo

            for _ in range(sobrantes):
                tarjetas += '''
                <div class="col-md-4 col-sm-6 col-10 mb-4 d-flex justify-content-center">
                    <div class="proyecto-card invisible"></div>
                </div>
                '''

            return tarjetas
        else:
            return '<div class="alert alert-warning text-center">NADA POR MOSTRAR</div>'

@app.route('/abrirproyectoruta',methods=['POST'])
def abrirproyectoruta():
    nombre = request.form['nombre']
    ruta = obtenerRutaPDF2(nombre,'Parcial 3')
    
    return render_template('perfiles/coordinacion/verproyecto.html',ruta = ruta)


@app.route('/verproyectos2',methods=['POST'])
def verproyectos2():
    nombre = request.form['busqueda']
    ciclo = request.form.get('ciclo')
    if ciclo !="0":
        proyecto = cargarproyectoselect(nombre,ciclo)
        return render_template('perfiles/Coordinacion/proyectosbusqueda.html', proyectos = proyecto)
    else:
        proyecto = cargarproyectolike(nombre)
        return render_template('perfiles/Coordinacion/proyectosbusqueda.html', proyectos = proyecto)
        
@app.route('/refresh',methods=['POST'])
def refresh_proyectos():
    proyectos = refresh()
    return render_template('perfiles/Coordinacion/proyectosbusqueda.html', proyectos = proyectos) 
def cargarproyectolike(proyecto):
    query = text("SELECT NombreProyecto FROM documentos WHERE Parcial = 'Parcial 3' AND NombreProyecto LIKE :proyecto")
    with engine.connect() as conn:
        ok = conn.execute(query, {'proyecto': f'%{proyecto}%'})
        rows = ok.fetchall()
        if rows:
            opciones = ''.join([f'''
            <div class="proyecto">
                <form action="/abrirproyectoruta" method="post">
                    <label for="">{row[0]}</label><br>
                    <input type="hidden" name="nombre" value="{row[0]}">
                    <button class="button-elegante">Abrir</button>
                </form>
            </div>
            ''' for row in rows])
            return opciones
        else:
            return '<div class="proyecto">NADA POR MOSTRAR</div>'


def refresh():
    query = text("SELECT NombreProyecto FROM documentos WHERE Parcial = 'Parcial 3'")
    with engine.connect() as conn:
        ok = conn.execute(query)
        rows = ok.fetchall()
        if rows:
            opciones = ''.join([f'''
            <div class="proyecto">
                <form action="/abrirproyectoruta" method="post">
                    <label for="">{row[0]}</label><br>
                    <input type="hidden" name="nombre" value="{row[0]}">
                    <button class="button-elegante">Abrir</button>
                </form>
            </div>
            ''' for row in rows])
            return opciones
        else:
            return '<div class="proyecto">NADA POR MOSTRAR</div>'
        


def cargarproyectoselect(proyecto, procedimiento=None):
    base_query = """
    SELECT DISTINCT d.NombreProyecto 
    FROM documentos d
    JOIN equipos e ON d.Matricula = e.Matricula
    JOIN procedimientos p ON e.Procedimiento = p.idProcedimiento
    WHERE d.Parcial = 'Parcial 3' AND d.NombreProyecto LIKE :proyecto
    """
    
    if procedimiento:
        base_query += " AND p.idProcedimiento = :procedimiento"

    query = text(base_query)

    with engine.connect() as conn:
        params = {'proyecto': f'%{proyecto}%'}
        if procedimiento:
            params['procedimiento'] = procedimiento
        result = conn.execute(query, params)
        rows = result.fetchall()

        if rows:
            opciones = ''.join([f'''
            <div class="proyecto">
                <form action="/abrirproyectoruta" method="post">
                    <label for="">{row[0]}</label><br>
                    <input type="hidden" name="nombre" value="{row[0]}">
                    <button class="button-elegante">Abrir</button>
                </form>
            </div>
            ''' for row in rows])
            return opciones
        else:
            return '<div class="proyecto">NADA POR MOSTRAR</div>'



def obtener_anio_actual():
    anio = datetime.datetime.now().year
    sql = text("SELECT Anio FROM periodos")
    with engine.connect() as conn:
        result = conn.execute(sql)
        row = result.fetchone()
    if row:
        if int(row[0]) < anio:
            sql2 = text("UPDATE periodos set Anio = :anio")
            with engine.connect() as conn:
                conn.execute(sql2, {'anio': anio})
                conn.commit()
    
def aniobase():
    sql = text("SELECT Anio FROM periodos")
    with engine.connect() as conn:
        result = conn.execute(sql)
        row = result.fetchone()
        return row[0]

    
@app.route('/foest02Evaluar', methods=['POST'])
def foest02Evaluar():
    Asesor = request.form.get('nombreasesor')
    Periodo = request.form.get('Periodo')
    Proyecto = request.form.get('Proyecto')
    Miembro = request.form.get('Miembro')
    Empresa = request.form.get('NombreEmpresa')
    Grado  = request.form.get('Grado')
    
   
    puntualidad = int(request.form['question1'])
    Responsabilidad = int(request.form['question2'])
    Etica = int(request.form['question3'])
    TomaDecisiones = int(request.form['question4'])
    Liderazgo = int(request.form['question5'])
    ExpresaIdeas = int(request.form['question6'])
    ComunicacionAsertiva = int(request.form['question7'])
    ResolucionSituaciones = int(request.form['question8'])
    ActitudFavorable = int(request.form['question9'])
    TrabajoEnEquipo = int(request.form['question10'])
    PromedioActitud = puntualidad + Responsabilidad + Etica + TomaDecisiones + Liderazgo + ExpresaIdeas + ComunicacionAsertiva + ResolucionSituaciones +ActitudFavorable + TrabajoEnEquipo
    PromedioActitud = PromedioActitud / 10
    Estrategias = int(request.form['question11'])
    AccionesMejora = int(request.form['question12'])
    ProcesosOperacion = int(request.form['question13'])
    PlanteaSoluciones = int(request.form['question14'])
    RespondeNecesidades = int(request.form['question15'])
    CumpleTiempo = int(request.form['question16'])
    PromedioDesarrollo = Estrategias + AccionesMejora + ProcesosOperacion + PlanteaSoluciones + RespondeNecesidades + CumpleTiempo
    PromedioDesarrollo = PromedioDesarrollo / 6
    guardado =guardarFOEST02(Periodo, Proyecto, Miembro, Empresa, Grado, Asesor, puntualidad, Responsabilidad, Etica, TomaDecisiones, Liderazgo, ExpresaIdeas, ComunicacionAsertiva, ResolucionSituaciones, ActitudFavorable, TrabajoEnEquipo, PromedioActitud, Estrategias, AccionesMejora, ProcesosOperacion, PlanteaSoluciones, RespondeNecesidades, CumpleTiempo, PromedioDesarrollo)
    if guardado:
        return render_template('Cargas/foest02.html')
    else:
        return 'Error al guardar los datos en la base de datos'
    
def guardarFOEST02(Periodo,Proyecto,Miembro,Empresa,GradoEstudios,AsesorEmpresarial,puntualidad, Responsabilidad, Etica, TomaDecisiones, Liderazgo, ExpresaIdeas, ComunicacionAsertiva, ResolucionSituaciones, ActitudFavorable, TrabajoEnEquipo, PromedioActitud, Estrategias, AccionesMejora, ProcesosOperacion, PlanteaSoluciones, RespondeNecesidades, CumpleTiempo, PromedioDesarrollo):
    anio = aniobase()
    query = text("INSERT INTO foest02 (Periodo,Proyecto, Miembro, Empresa, GradoEstudios, AsesorEmpresarial, puntualidad, Responsabilidad, Etica, TomaDecisiones, Liderazgo, ExpresaIdeas, ComunicacionAsertiva, ResolucionSituaciones, ActitudFavorable, TrabajoEnEquipo, PromedioActitud, Estrategias, AccionesMejora, ProcesosOperacion, PlanteaSoluciones, RespondeNecesidades, CumpleTiempo, PromedioDesarrollo) VALUES (:Periodo,:Proyecto,:Miembro,:Empresa,:GradoEstudios,:AsesorEmpresarial,:puntualidad,:Responsabilidad,:Etica,:TomaDecisiones,:Liderazgo,:ExpresaIdeas,:ComunicacionAsertiva,:ResolucionSituaciones,:ActitudFavorable,:TrabajoEnEquipo,:PromedioActitud,:Estrategias,:AccionesMejora,:ProcesosOperacion,:PlanteaSoluciones,:RespondeNecesidades,:CumpleTiempo,:PromedioDesarrollo)")
    # Asegúrate de que los parámetros coincidan con los nombres de las columnas en tu tabla foest02
    try:
        with engine.connect() as conn:
            with conn.begin():
                conn.execute(query,  {
                    'Periodo': Periodo+'-'+anio,
                    'Proyecto': Proyecto,
                    'Miembro': Miembro,
                    'Empresa': Empresa,
                    'GradoEstudios': GradoEstudios,
                    'AsesorEmpresarial': AsesorEmpresarial,
                    'puntualidad': puntualidad,
                    'Responsabilidad': Responsabilidad,
                    'Etica': Etica,
                    'TomaDecisiones': TomaDecisiones,
                    'Liderazgo': Liderazgo,
                    'ExpresaIdeas': ExpresaIdeas,
                    'ComunicacionAsertiva': ComunicacionAsertiva,
                    'ResolucionSituaciones': ResolucionSituaciones,
                    'ActitudFavorable': ActitudFavorable,
                    'TrabajoEnEquipo': TrabajoEnEquipo,
                    'PromedioActitud': PromedioActitud,
                    'Estrategias': Estrategias,
                    'AccionesMejora': AccionesMejora,
                    'ProcesosOperacion': ProcesosOperacion,
                    'PlanteaSoluciones': PlanteaSoluciones,
                    'RespondeNecesidades': RespondeNecesidades,
                    'CumpleTiempo': CumpleTiempo,
                    'PromedioDesarrollo': PromedioDesarrollo
                })
        return True
    except Exception as e:
        print(f"------------------------------------------Error al insertar en foest02: {e}")
        return False