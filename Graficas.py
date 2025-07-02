from flask import render_template
from sqlalchemy import text
from conexion import engine



def obtenerPromedios02(Periodo):
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
FROM foest02
                 WHERE Periodo = :Periodo;""")
    
    with engine.connect() as conn:
        result = conn.execute(query,{'Periodo':Periodo}).mappings().first()
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
    PeriodoActivo = periodoCuatrimestral()
    anio = aniobase()
    Periodo = PeriodoActivo + "-" + anio
    row = obtenerPromedios02(Periodo)
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
                       datos_promedios=datos_promedios,puntos_colores=puntos_colores,Periodo=Periodo)




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
AVG(Promedio) AS Promedio
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
    row = obtenerPromedios08()
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
            "El asesor mantuvo contacto con el asesor empresarial para un adecuado desarrollo del proyecto","Promedio"
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



#Periodos y año
def periodoCuatrimestral():
    query= text("SELECT * FROM periodos WHERE Estado = 'activo'")
    with engine.connect() as conn:
        ok= conn.execute(query)
        ok = ok.fetchone()
        if ok:
            return ok[1]
        else:
            return 'No hay periodo activo'
        


def aniobase():
    sql = text("SELECT Anio FROM periodos")
    with engine.connect() as conn:
        result = conn.execute(sql)
        row = result.fetchone()
        return row[0]
    


#Foest07 conteo
def conteo():

    valores_validos = [
       
    # Estancia I
    "Analizar Recursos-Económicos",
    "Planificar de recursos para su uso de forma eficiente",
    "Diagnosticar el estado actual de la organización",
    "Diseñar estrategias financieras",
    "Formular alternativas optimas de administración",
    "Diagnosticar variables económicas",
    "Identificar elementos que afectan el desarrollo de la organización",
    "Analizar variables económicas",
    "Simular de escenarios para plan estratégico de acción",
    "Cuantificar impacto en organización",
    "Estudios técnicos económicos",
    "Gestionar recursos",

    # Estancia II
    "Construir estrategias financieras",
    "Desarrollar estrategias costo-beneficio",
    "Diseñar alternativas de negocio",
    "Gestionar proyectos de inversión",
    "Sistematizar procesos administrativos mediante las TIC´S",
    "Generar reportes ejecutivos y técnicos para la toma de decisiones",
    "Diseñar modelos financieras y económicos",
    "Transferir tecnología y conocimiento para la creación de negocios inteligentes",
    "Desarrollo de negocios inteligentes",
    "Análisis de tendencias y hábitos del mercado",

    # Estadía
    "Identificar variables económicas, contables, legales y administrativas",
    "Aplicar fundamentos matemáticos y estadísticos",
    "Diagnosticar aspectos financieros",
    "Diagnosticar variables del entorno económico",
    "Evaluar proyectos con base a variables del entorno económico",
    "Diseñar modelos financieros aplicando las TIC´s",
    "Construir proyectos de inversión",
    "Transferencia tecnológica en el sector",
    "Integración de estrategias financieras, bursátiles y empresariales",
    "Optimizar recursos"

    # Estancia I
    "Dimensionar de componentes Mecánicos",
    "Establecimiento de procedimientos de manufactura",
    "Aplicar herramientas de medición mediante las TIC´s",
    "Identificar características dimensionales y geométricas",
    "Aplicar herramientas mediante las TIC´s para generar planos de taller",
    "Implementar manual de mantenimiento",
    "Reestructuración de procesos",
    "Estrategias de desarrollo",
    "Mantenimiento mecánico",

    # Estancia II
    "Proponer procesos de manufactura de componentes mecánicos",
    "Establecer procedimientos de fabricación",
    "Establecer normas de calidad y seguridad",
    "Implementar procesos de manufactura convencional-CNC",
    "Implementar normas de la industria",
    "Definir componentes mecánicos",
    "Integrar sistemas mecánicos",
    "Simular modelos de componentes mecánicos mediante las TIC´s",
    "Mantenimiento mecánico",

    # Estadía
    "Establecer procedimientos de fabricación que cumplan con normas de calidad y seguridad",
    "Implementar procesos de Manufactura convencional y/o CNC mediante estándares",
    "Integración de sistemas mecánicos",
    "Simulación de Componentes por medio de herramientas computacionales para validar comportamiento dinámico",
    "Procedimientos de fabricación",
    "Determinar la implementación de normas de calidad nacional e internacional ",
    "Implementación de normas ambientales nacional e internacional",
    "Operación de industria 4.0",
    "Dirección de Recursos Humanos",
    "Establecer mantenimiento mecánico",
    "Implementación de procesos de manufactura por medio de tecnología",
    "Estrategias para el desarrollo de vehículos para el cuidado y protección del medio ambiente"

    # Estancia I
    "Estructurar sistemas de producción",
    "Control estadístico de calidad",
    "Aplicar software de diseño",
    "Implementación de normatividad para optimizar recursos",
    "Análisis de rentabilidad de productos",
    "Implementación de calidad en productos y servicios",

    # Estancia II
    "Gestión procesos de manufactura",
    "Gestionar estándares de calidad",
    "Estructurar mejoras en los procesos productivos",
    "Planear diagnostico de procesos de producción",
    "Controlar procesos de producción",
    "Eficientar el manejo de recursos (Humanos, materiales, financieros)",
    "Desarrollar sistemas de calidad",
    "Coordinar planes de mantenimiento de TPM, jidoka ",
    "Estimación de costo-beneficio",
    "Manejar software especializado",
    "Manejo de Equipo y maquinaria auxiliar en la organización",

    # Estadía
    "Evaluar proyectos productivos estratégicos e innovadores",
    "Aplicar software de simulación",
    "Aplicar herramientas de manufactura avanzada",
    "Gestionar propuestas tecnológicas innovadoras",
    "Diseñar productos utilizando paquetes CAD-CAM-CAE",
    "Validar proyectos productivos",
    "Toma de decisiones para mejora de competitividad",
    "Generar planos y especificaciones de producto",
    "Analizar procesos y productos",
    "Generar estrategias de productividad y competitividad"


    # funcion-estancia1[] y funcion-estancia2[]
    "Diseñar software",
    "Aplicación adecuada de técnicas de desarrollo software",
    "Diagnóstico de requerimientos",
    "Implementar metodologías de modelado",
    "Optimizar operaciones comerciales internacionales",
    "Estructurar datos",
    "Desarrollar interfaces para su validación",
    "Aplicar normatividad y estándares",
    "Representación técnica del software",
    "Estructurar diseños de software con base en requerimientos",
    "Aplicación de metodologías de diagnóstico",

    # funcion-estadia[]
    "Dirigir proyectos de software",
    "Gestionar proyectos de software",
    "Aplicación de la metodología de gestión de proyectos",
    "Determinar herramientas administrativas y financieras",
    "Coordinar el plan de pruebas de software",
    "Ejecución de pruebas de software",
    "Planes de mercadotecnia internacional",
    "Aplicación de estandares para aseguramiento de calidad de software",
    "Planear y coordinar mantenimiento de software",
    "Uso de metodologías de mantenimiento de software",
    "Implementar ingeniería inversa y reingeniería",
    "Aplicación de estándares y normatividad aplicación y mejora del software"

 


    "Diseñar estrategias organizadas",
    "Análisis de operaciones",
    "Identificación de mercados nacionales/internacionales",
    "Planeación estratégica de negocios",
    "Evaluación del entorno de mercado",
    "Análisis de proveedores, clientes y propiedades",
    "Identificación de oportunidad de negocios",
    "Mejoras administrativas",
    "Gestión de procesos administrativos",

   
    "Optimizar funciones comerciales internacionales",
    "Optimizar operaciones legales internacionales",
    "Optimizar operaciones financieras internacionales",
    "Optimizar operaciones comerciales internacionales",
    "Estrategia de negocio internacional",
    "Desarrollar procesos de exportación-importación",
    "Actividades de despacho aduanero",
    "Diversificación de mercado a nivel internacional",
    "Análisis de proveedores internacionales",
    "Mejoras a cadena de suministro-Logística",
    "Administrar sistemas de calidad",

    # funcion-estadia[]
    "Establecer relaciones comerciales",
    "Plan de negocios de exportación-importación",
    "Dirigir estrategias gerencias y de negociación internacional",
    "Asesorar estrategias gerencias y de negociación internacional",
    "Ejecutar estrategias gerencias y de negociación internacional",
    "Aplicación de herramientas administrativas en un entorno internacional",
    "Planes de mercadotecnia internacional",
    "Proyectos de Inversión",
    "Aplicación de normatividad internacional",
    "Estrategias de competitividad de productos y servicios"
]

    # Crear placeholders para cada valor
    placeholders = ', '.join([f":val{i}" for i in range(len(valores_validos))])

    query = text(f"""
        SELECT categoria, COUNT(*) AS cantidad
        FROM (
            SELECT 
                CASE 
                    WHEN FuncionesPrioritarias IN ({placeholders}) 
                        THEN FuncionesPrioritarias 
                    ELSE 'Otros' 
                END AS categoria
            FROM foest07

            UNION ALL

            SELECT 
                CASE 
                    WHEN FuncionesPrioritarias2 IN ({placeholders}) 
                        THEN FuncionesPrioritarias2 
                    ELSE 'Otros' 
                END
            FROM foest07

            UNION ALL

            SELECT 
                CASE 
                    WHEN FuncionesPrioritarias3 IN ({placeholders}) 
                        THEN FuncionesPrioritarias3 
                    ELSE 'Otros' 
                END
            FROM foest07
        ) AS funciones_clasificadas
        GROUP BY categoria
        ORDER BY cantidad DESC
    """)

    # Diccionario de parámetros
    parametros = {f"val{i}": valor for i, valor in enumerate(valores_validos)}

    # Ejecutar la consulta
    with engine.connect() as conn:
        resultado = conn.execute(query, parametros).fetchall()
        conteo_resultado = {row[0]: row[1] for row in resultado}
        # Asegurarse de que 'Otros' esté presente en el resultado
         
    return f'{conteo_resultado}'  # Convertir el diccionario a una cadena para mostrar en la plantilla
