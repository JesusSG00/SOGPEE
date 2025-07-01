from flask import render_template
from conexion import engine
from sqlalchemy import text

#Calificaciones de los formatos 2, 3 y 8

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
                        <th><div>
                        <form action="/graficas08" method="post">
                            <button type="submit" class="btn btn-primary">Graficar todo</button>
                        </form>
                    </div></th>
                   
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

def cargarCalificaciones02(Periodo):
    try:
        query = text("""
            SELECT foest02.Miembro, estudiante.Nombre1, estudiante.Nombre2, estudiante.ApellidoP, estudiante.ApellidoM,
                   foest02.PromedioActitud, foest02.PromedioDesarrollo, Periodo
            FROM estudiante 
            JOIN foest02 ON estudiante.Matricula = foest02.miembro
                     WHERE Periodo = :Periodo;
        """)
        with engine.connect() as conn:
            rows = conn.execute(query,{'Periodo':Periodo}).fetchall()  
            
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
                        <th>Periodo</th>
                        <th><div>
                        <form action="/graficas" method="post">
                            <button type="submit" class="btn btn-primary">Graficar</button>
                        </form>
                    </div></th>
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
                    <td>{fila[7]}</td>
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
                        <th><div>
                        <form action="" method="post">
                            <button type="button" class="btn btn-primary">Graficar todo</button>
                        </form>
                    </div></th>
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



#Calificaciones completas de los formatos 2, 3 y 8

def Completa08(matricula):
    try:
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

def Completa03(nombre):
    
    try:
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

def Completa02(Miembro):
    try:
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


# Cargar proyectos de coordinación para el parcial 3
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

            sobrantes = (3 - (total % 3)) % 3  

            for _ in range(sobrantes):
                tarjetas += '''
                <div class="col-md-4 col-sm-6 col-10 mb-4 d-flex justify-content-center">
                    <div class="proyecto-card invisible"></div>
                </div>
                '''

            return tarjetas
        else:
            return '<div class="alert alert-warning text-center">NADA POR MOSTRAR</div>'