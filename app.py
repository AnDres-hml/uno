from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        try:
            nota1 = float(request.form['nota1'])
            nota2 = float(request.form['nota2'])
            nota3 = float(request.form['nota3'])
            asistencia = float(request.form['asistencia'])

            promedio = (nota1 + nota2 + nota3) / 3
            if promedio >= 50 and asistencia >= 75:
                resultado = "APROBADO"
            else:
                resultado = "REPROBADO"

            return render_template('ejercicio1.html', promedio=promedio, resultado=resultado)
        except Exception as e:
            return render_template('ejercicio1.html', error=str(e))
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        try:
            nombre1 = request.form['nombre1']
            nombre2 = request.form['nombre2']
            nombre3 = request.form['nombre3']

            nombres = [nombre1, nombre2, nombre3]
            nombre_mas_largo = max(nombres, key=len)
            longitud = len(nombre_mas_largo)

            return render_template('ejercicio2.html', nombre_mas_largo=nombre_mas_largo, longitud=longitud)
        except Exception as e:
            return render_template('ejercicio2.html', error=str(e))
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)
