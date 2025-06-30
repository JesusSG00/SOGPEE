from flask import render_template
from sqlalchemy import text
from conexion import engine
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

