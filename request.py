import requests

link = 'https://minhaapi--giovanamerguizo.repl.co/pegarvendas'

requisicao = requests.get(link)

print(requisicao)
print(requisicao.json())

dicionario = requisicao.json()
print(dicionario['total_vendas'])
