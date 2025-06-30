from flask import render_template
from sqlalchemy import text
from conexion import engine


def obtenerPromedios02():
    query = text("""SELECT 
AVG(Puntualidad) AS Promedio1,
AVG(Responsabilidad) AS Promedio2,
AVG(Etica) AS Promedio3,
AVG(TomaDecisiones) AS Promedio4,
AVG(Liderazgo) AS Promedio5,
AVG(ExpresaIdeas) AS Promedio6,
AVG(ComunicacionAsertiva) AS Promedio7,
AVG(ResolucionSituaciones) AS Promedio8,
AVG(ActitudFavorable) AS Promedio9,
AVG(TrabajoEnEquipo) AS Promedio10,
AVG(PromedioActitud) AS PromedioActitud,
AVG(Estrategias) AS Promedio11,
AVG(AccionesMejora) AS Promedio12,
AVG(ProcesosOperacion) AS Promedio13,
AVG(PlanteaSoluciones) AS Promedio14,
AVG(RespondeNecesidades) AS Promedio15,
AVG(CumpleTiempo) AS Promedio16,
AVG(PromedioDesarrollo) AS PromedioDesarrollo
FROM foest02;""")
    
    with engine.connect() as conn:
        result = conn.execute(query).mappings().first()
        row = result
        if row:
            promedios = {
                "Promedio1": row["Promedio1"],
                "Promedio2": row["Promedio2"],
                "Promedio3": row["Promedio3"],
                "Promedio4": row["Promedio4"],
                "Promedio5": row["Promedio5"],
                "Promedio6": row["Promedio6"],
                "Promedio7": row["Promedio7"],
                "Promedio8": row["Promedio8"],
                "Promedio9": row["Promedio9"],
                "Promedio10": row["Promedio10"],
                "PromedioActitud": row["PromedioActitud"],
                "Promedio11": row["Promedio11"],
                "Promedio12": row["Promedio12"],
                "Promedio13": row["Promedio13"],
                "Promedio14": row["Promedio14"],
                "Promedio15": row["Promedio15"],
                "Promedio16": row["Promedio16"],
                "PromedioDesarrollo": row["PromedioDesarrollo"]
            }
            return promedios
        else:
            return None



def graficar02():
    row = obtenerPromedios02()
    promedios = [
    row["Promedio1"], row["Promedio2"], row["Promedio3"],
    row["Promedio4"], row["Promedio5"], row["Promedio6"],
    row["Promedio7"], row["Promedio8"], row["Promedio9"],
    row["Promedio10"], row["PromedioActitud"],row["Promedio11"],
    row["Promedio12"], row["Promedio13"], row["Promedio14"],
    row["Promedio15"], row["Promedio16"], row["PromedioDesarrollo"]
    
]
    
    
    if promedios:
        etiquetas = [
            "Puntualidad", "Responsabilidad", "Ética",
            "Toma de Decisiones", "Liderazgo", "Expresa Ideas",
            "Comunicación Asertiva", "Resolución de Situaciones",
            "Actitud Favorable", "Trabajo en Equipo", "Promedio Actitud",
            "Estrategias", "Acciones de Mejora", "Procesos de Operación",
            "Plantea Soluciones", "Responde Necesidades", "Cumple Tiempo",
            "Promedio Desarrollo"
        ]
        datos_promedios = promedios
        num_actividades = len(etiquetas)
        puntos_colores = [
        'rgba(54, 162, 235, 1)' if i not in [10, num_actividades-1] else 'rgba(255, 0, 0, 1)'
        for i in range(num_actividades)
        ]

    return render_template('/Grafica/GraficaFoest02.html',
                       etiquetas=etiquetas,
                       datos_promedios=datos_promedios,puntos_colores=puntos_colores)




from flask import render_template
from sqlalchemy import text
from conexion import engine


def obtenerPromedios08():
    query = text("""SELECT 
AVG(Pregunta01) AS Promedio1,
AVG(Pregunta02) AS Promedio2,
AVG(Pregunta03) AS Promedio3,
AVG(Pregunta04) AS Promedio4,
AVG(Pregunta05) AS Promedio5,
AVG(Pregunta06) AS Promedio6,
AVG(Pregunta07) AS Promedio7,
AVG(Pregunta08) AS Promedio8,
AVG(Pregunta09) AS Promedio9,
AVG(Promedio) AS Promedio,
FROM foest08;""")
    
    with engine.connect() as conn:
        result = conn.execute(query).mappings().first()
        row = result
        if row:
            promedios = {
                "Promedio1": row["Promedio1"],
                "Promedio2": row["Promedio2"],
                "Promedio3": row["Promedio3"],
                "Promedio4": row["Promedio4"],
                "Promedio5": row["Promedio5"],
                "Promedio6": row["Promedio6"],
                "Promedio7": row["Promedio7"],
                "Promedio8": row["Promedio8"],
                "Promedio9": row["Promedio9"],
                "Promedio": row["Promedio"],
              
            }
            return promedios
        else:
            return None



def graficar08():
    row = obtenerPromedios02()
    promedios = [
    row["Promedio1"], row["Promedio2"], row["Promedio3"],
    row["Promedio4"], row["Promedio5"], row["Promedio6"],
    row["Promedio7"], row["Promedio8"], row["Promedio9"],
    row["Promedio"]
    
]
    
    
    if promedios:
        etiquetas = [
            "Servicio de calidad", "Proporcionaron información útil", "Generaron cartas de forma eficiente y facil",
            "La gestion de la carta de presentacion fue oportuna", "La asignación del asesor fue oportuna", "La capacitación por el asesor fue adecuada",
            "El asesor asistio a las asesorias programadas", "El asesor aclaro dudas durante el desarrollo",
            "El asesor mantuvo contacto con el asesor empresarial para un adecuado desarrollo del proyecto"
        ]
        datos_promedios = promedios
        num_actividades = len(etiquetas)
        puntos_colores = [
        'rgba(54, 162, 235, 1)' if i not in [10, num_actividades-1] else 'rgba(255, 0, 0, 1)'
        for i in range(num_actividades)
        ]

    return render_template('/Grafica/GraficaFoest08.html',
                       etiquetas=etiquetas,
                       datos_promedios=datos_promedios,puntos_colores=puntos_colores)
