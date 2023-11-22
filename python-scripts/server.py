from flask import Flask, request, jsonify
from flask_cors import CORS
import biseccion
import reglaFalsa
import puntoFijoCS
import puntoFijoDC
import newtonCS
import newtonCD
import secante
import raicesMultiplesCS
import raicesMultiplesCD

app = Flask(__name__)
CORS(app)

@app.route('/biseccion', methods=['POST'])
def handle_script1():
    data = request.json
    result = biseccion.biseccion(data['funcion'], float(data['x_inferior']), float(data['x_superior']), float(data['tolerancia']), int(data['iteraciones']))
    return jsonify(result)


@app.route('/reglaFalsa', methods=['POST'])
def handle_script2():
    data = request.json
    result = reglaFalsa.reglaFalsa(data['funcion'], float(data['x_inferior']), float(data['x_superior']), float(data['tolerancia']), int(data['iteraciones']))
    print(result)
    return jsonify(result)

@app.route('/puntoFijoCS', methods=['POST'])
def handle_script3():
    data = request.json
    result = puntoFijoCS.puntoFijoCS(data['funcionF'], data['funcionG'], float(data['x_inferior']), float(data['tolerancia']), int(data['iteraciones']))
    print(result)
    return jsonify(result)

@app.route('/puntoFijoDC', methods=['POST'])
def handle_script4():
    data = request.json
    result = puntoFijoDC.PuntoFijoDecimalesCorrectos(data['funcionF'], data['funcionG'], float(data['x_inferior']), float(data['tolerancia']), int(data['iteraciones']))
    print(result)
    return jsonify(result)

@app.route('/newtonCS', methods=['POST'])
def handle_script5():
    data = request.json
    result = newtonCS.NewtonCifrasSignificativas(data['funcionF'], data['funcionG'], float(data['x_inferior']), float(data['tolerancia']), int(data['iteraciones']))
    print(result)
    return jsonify(result)

@app.route('/newtonCD', methods=['POST'])
def handle_script6():
    data = request.json
    result = newtonCD.NewtonDecimalesCorrectos(data['funcionF'], data['funcionG'], float(data['x_inferior']), float(data['tolerancia']), int(data['iteraciones']))
    print(result)
    return jsonify(result)

@app.route('/secante', methods=['POST'])
def handle_script7():
    data = request.json
    result = secante.Secante(data['funcionF'], float(data['x0']), float(data['x1']), float(data['tolerancia']), int(data['iteraciones']))
    print(result)
    return jsonify(result)

@app.route('/raicesMultiplesCS', methods=['POST'])
def handle_script8():
    data = request.json
    result = raicesMultiplesCS.RaicesMultiplesCifrasSignificativas(data['funcionF'], data['funcionF1'], float(data['x0']), float(data['tolerancia']), int(data['iteraciones']))
    print(result)
    return jsonify(result)

@app.route('/raicesMultiplesCD', methods=['POST'])
def handle_script9():
    data = request.json
    result = raicesMultiplesCD.RaicesMultiplesDecimalesCorrectos(0, data['funcionF'], data['funcionF1'], float(data['x0']), float(data['tolerancia']), int(data['iteraciones']))
    print(result)
    return jsonify(result)

@app.route('/vandermonde', methods=['POST'])
def handle_script10():
    data = request.json
    result = raicesMultiplesCD.RaicesMultiplesDecimalesCorrectos(0, data['funcionF'], data['funcionF1'], float(data['x0']), float(data['tolerancia']), int(data['iteraciones']))
    print(result)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
