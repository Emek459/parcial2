import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

df = pd.read_csv('api_parcial2.csv')
datos = df.to_dict(orient='records')

@app.route('/datos', methods=['GET'])
def get_datos():
    pais = 'Panama'
    indicador = 'Indicator'

    datos_filtrados = df.loc[(df['Country Name'] == pais) & (df['Indicator'] == indicador)].to_dict(orient='records')

    return jsonify(datos_filtrados)

if __name__ == '__main__':
    app.run(debug=True)
