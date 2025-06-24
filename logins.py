from flask import render_template
from conexion import engine
from sqlalchemy import text
from Alumno_Complementos import * 

def validarLogin(correo, password):
    estudiante = boolloginEstudiante(correo,password)
    if estudiante:
        Resultado = inicioEstudiante(correo,password)
        return Resultado
    asesorAcademico = boolloginAsesorAcademico(correo,password)
    if asesorAcademico:
        Resultado = AsesorA(correo, password)
        return Resultado
    coordinacion = boollogincoordinacion(correo,password)
    if coordinacion:
        Resultado = SesionCoordinacion(correo,password)
        return Resultado
    if not estudiante and not asesorAcademico and not coordinacion:
        return render_template('/Error/EstudianteNoEncontrado.html')


#Funciones de retorno booleana

def boolloginAsesorAcademico(correo, password):
    resultado = inicioSesionAsesorA(correo,password)
    return resultado

def boollogincoordinacion(correo, password):
    resultado = inicioSesionCoordinacion(correo,password) 
    return resultado

def boolloginEstudiante(correo,password):
    resultado = inicioSesionEstudiante(correo,password) 
    return resultado


#Funcion de validacion de correo y contraseña

def inicioSesionCoordinacion(correo,password):
    try:
        query = text("SELECT Correo FROM coordinacion WHERE correo = :correo AND password =:password")
        with engine.connect() as conn:
            ok= conn.execute(query, {'correo': correo,'password':password}).fetchone()
            if ok:
                return True
            else:
                return False
    except Exception as e:
            return f'{e}'
    

def inicioSesionEstudiante(correo,matricula):
 
    try:
        query = text("SELECT Matricula,Nombre1,Nombre2,ApellidoP,ApellidoM,Telefono,Correo FROM estudiante WHERE  correo =:correo AND matricula = :matricula ")
        with engine.connect() as conn:
            ok= conn.execute(query, {'correo':correo,'matricula': matricula}).fetchone()
            if ok:
                return True
            else:
                return False
    except Exception as e:
            return f'error {e}'


def inicioSesionAsesorA(correo,password):
    try:
        query = text("SELECT Nombre1 FROM asesoracademico WHERE password = :password AND Correo =:correo")
        with engine.connect() as conn:
            ok= conn.execute(query, {'password': password,'correo':correo}).fetchone()
            if ok:
               return True
                
            else:
                return False
    except Exception as e:
            return f'error {e}'
    




#Funciones necesarias para cargar datos
def AsesorA(correo,password):
    try:
        query = text("SELECT Id,Nombre1,Nombre2,ApellidoP,ApellidoM FROM asesoracademico WHERE password = :password AND Correo =:correo")
        with engine.connect() as conn:
            ok= conn.execute(query, {'password': password,'correo':correo}).fetchone()
            if ok:
                asesor = {
                    'Id': ok[0],
                    'Nombre1': ok[1],
                    'Nombre2': ok[2],
                    'ApellidoP': ok[3],
                    'ApellidoM': ok[4]
                }
               
                resultado = cargarProyectosAsesor(asesor['Id'])
                return render_template('/perfiles/AsesorAcademico/revisar_expediente.html',resultado = resultado,ID = asesor['Id'], nombre=asesor['Nombre1'],nombre2=asesor['Nombre2'],apellidoP=asesor['ApellidoP'],apellidoM=asesor['ApellidoM'],correo=correo)
            else:
                return False
    except Exception as e:
            return f'error {e}'
    


def SesionCoordinacion(correo,password):
    try:
        query = text("SELECT Nombre,Nombre2,ApellidoP,ApellidoM,Correo FROM coordinacion WHERE correo = :correo AND password =:password")
        with engine.connect() as conn:
            ok= conn.execute(query, {'correo': correo,'password':password}).fetchone()
            if ok:
                resultado = {
                    'Nombre': ok[0],
                    'Nombre2': ok[1], 
                    'ApellidoP': ok[2], 
                    'ApellidoM': ok[3], 
                    'Correo': ok[4]
                }
                return render_template('/perfiles/Coordinacion/perfil_coordinacion.html',nombre = resultado['Nombre'],nombre2 =resultado['Nombre2'] ,apellidoP=resultado['ApellidoP'],apellidoM=resultado['ApellidoM'],correo=resultado['Correo'])
            else:
                return render_template('Error/CoordinacionNoEncontrado.html')
    except Exception as e:
            return f'{e}'


def inicioEstudiante(correo,matricula):
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
