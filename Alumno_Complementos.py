from sqlalchemy import text
from conexion import engine

def cargarProyectoAlumno(Matricula):        #Cargar proyecto del alumno
    
    query = text("SELECT p.Nombre FROM estudiante est JOIN equipos e ON est.Matricula = e.Matricula JOIN proyecto p ON e.Id_Proyecto = p.ProyectoID WHERE est.Matricula = :Matricula")
    with engine.connect() as conn:
        resultado = conn.execute(query,{'Matricula':Matricula}).fetchone()
        if resultado:
            return resultado[0]
        else:
            return "No asignado"
        



def cargarAsesorEmpresarial(Proyecto):      #Asesor empresarial relacionado al proyecto del alumno
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


def folioproyecto(proyecto):    #Obtener folio del proyecto
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
    


def verificarAsignacionProyecto(Matricula):     #Verificar si existe algun proyecto(equipo) asignado a algun alumno
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