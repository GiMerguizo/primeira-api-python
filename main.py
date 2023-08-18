import pandas as pd
from flask import Flask, jsonify

# Inicializando o Flask
app = Flask(__name__)

# Construir as funcionalidades
# Disponibilizando a Homepage 
@app.route('/')
def homepage():
  return 'A API está no ar'

@app.route('/pegarvendas')
def pegarvendas():
  tabela = pd.read_csv('12-18 - Criando API no Python.csv')
  total_vendas = tabela['Vendas'].sum() 
  # print(total_vendas)  
  resposta = {'total_vendas': total_vendas}
  return jsonify(resposta)

# Rodar
app.run(host='0.0.0.0')
