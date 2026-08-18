# reportes.py

def generar_reporte_sudokus(tableros, intentos):
    contenido_html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Reporte 1: Resumen por Sudoku</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background-color: #f4f6f9; }
        h1 { color: #2c3e50; text-align: center; }
        table { width: 80%; margin: 20px auto; border-collapse: collapse; background: #fff; }
        th, td { border: 1px solid #ddd; padding: 12px; text-align: center; }
        th { background-color: #34495e; color: white; }
        tr:nth-child(even) { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h1>Resumen por Sudoku</h1>
    <table>
        <thead>
            <tr>
                <th>ID Sudoku</th>
                <th>Dificultad</th>
                <th>Intentos Recibidos</th>
                <th>Tiempo Promedio (s)</th>
                <th>Tasa de Éxito (%)</th>
            </tr>
        </thead>
        <tbody>
"""
    for t in tableros:
        intentos_sudoku = [i for i in intentos if i.id_Sudoku == t.id_Sudoku]
        cant_intentos = len(intentos_sudoku)
        
        if cant_intentos > 0:
            tiempo_prom = sum(i.tiempo_Segundos for i in intentos_sudoku) / cant_intentos
            correctos = sum(1 for i in intentos_sudoku if i.es_correcto)
            tasa_exito = (correctos / cant_intentos) * 100.0
        else:
            tiempo_prom = 0.0
            tasa_exito = 0.0

        contenido_html += f"""            <tr>
                <td>{t.id_Sudoku}</td>
                <td>{t.dificultad}</td>
                <td>{cant_intentos}</td>
                <td>{tiempo_prom:.2f}</td>
                <td>{tasa_exito:.2f}%</td>
            </tr>\n"""

    contenido_html += """        </tbody>
    </table>
</body>
</html>"""

    with open("reporte_sudokus.html", "w", encoding="utf-8") as f:
        f.write(contenido_html)
    print("[OK] Reporte 'Resumen por Sudoku' generado con éxito (reporte_sudokus.html).")


def generar_reporte_jugadores(jugadores, intentos):
    contenido_html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Reporte 2: Rendimiento por Jugador</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background-color: #f4f6f9; }
        h1 { color: #2c3e50; text-align: center; }
        table { width: 90%; margin: 20px auto; border-collapse: collapse; background: #fff; }
        th, td { border: 1px solid #ddd; padding: 12px; text-align: center; }
        th { background-color: #27ae60; color: white; }
        tr:nth-child(even) { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h1>Rendimiento por Jugador</h1>
    <table>
        <thead>
            <tr>
                <th>Carnet</th>
                <th>Nombre Completo</th>
                <th>Nivel</th>
                <th>Tableros Intentados</th>
                <th>Validez Promedio (%)</th>
                <th>Tiempo Promedio (s)</th>
                <th>Resueltos Perfectamente</th>
            </tr>
        </thead>
        <tbody>
"""
    for j in jugadores:
        intentos_jugador = [i for i in intentos if str(i.carnet) == str(j.carnet)]
        cant_intentos = len(intentos_jugador)

        if cant_intentos > 0:
            validez_prom = sum(i.porcentaje_validez for i in intentos_jugador) / cant_intentos
            tiempo_prom = sum(i.tiempo_Segundos for i in intentos_jugador) / cant_intentos
            perfectos = sum(1 for i in intentos_jugador if i.es_correcto)
        else:
            validez_prom = 0.0
            tiempo_prom = 0.0
            perfectos = 0

        contenido_html += f"""            <tr>
                <td>{j.carnet}</td>
                <td>{j.obtener_nombre_completo()}</td>
                <td>{j.nivelDificultad}</td>
                <td>{cant_intentos}</td>
                <td>{validez_prom:.2f}%</td>
                <td>{tiempo_prom:.2f}</td>
                <td>{perfectos}</td>
            </tr>\n"""

    contenido_html += """        </tbody>
    </table>
</body>
</html>"""

    with open("reporte_jugadores.html", "w", encoding="utf-8") as f:
        f.write(contenido_html)
    print("[OK] Reporte 'Rendimiento por Jugador' generado con éxito (reporte_jugadores.html).")


def generar_reporte_top10(jugadores, tableros, intentos):
    # Filtrar solo intentos válidos al 100%
    intentos_validos = [i for i in intentos if i.es_correcto]
    # Ordenar por tiempo ascendente
    intentos_ordenados = sorted(intentos_validos, key=lambda x: x.tiempo_Segundos)[:10]

    contenido_html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Reporte 3: Top 10 Mejores Tiempos</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background-color: #f4f6f9; }
        h1 { color: #8e44ad; text-align: center; }
        table { width: 85%; margin: 20px auto; border-collapse: collapse; background: #fff; }
        th, td { border: 1px solid #ddd; padding: 12px; text-align: center; }
        th { background-color: #8e44ad; color: white; }
        tr:nth-child(even) { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h1>Top 10 Mejores Tiempos (Sudokus Resueltos)</h1>
    <table>
        <thead>
            <tr>
                <th>Posición</th>
                <th>Carnet</th>
                <th>Nombre Completo</th>
                <th>ID Sudoku</th>
                <th>Dificultad</th>
                <th>Tiempo (s)</th>
            </tr>
        </thead>
        <tbody>
"""
    for pos, i in enumerate(intentos_ordenados, start=1):
        jugador = next((j for j in jugadores if str(j.carnet) == str(i.carnet)), None)
        tablero = next((t for t in tableros if t.id_Sudoku == i.id_Sudoku), None)

        nombre_jugador = jugador.obtener_nombre_completo() if jugador else "Desconocido"
        dificultad = tablero.dificultad if tablero else "N/A"

        contenido_html += f"""            <tr>
                <td><b>#{pos}</b></td>
                <td>{i.carnet}</td>
                <td>{nombre_jugador}</td>
                <td>{i.id_Sudoku}</td>
                <td>{dificultad}</td>
                <td>{i.tiempo_Segundos} s</td>
            </tr>\n"""

    contenido_html += """        </tbody>
    </table>
</body>
</html>"""

    with open("reporte_top10.html", "w", encoding="utf-8") as f:
        f.write(contenido_html)
    print("[OK] Reporte 'Top 10 Mejores Tiempos' generado con éxito (reporte_top10.html).")