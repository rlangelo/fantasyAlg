import urllib, json

urlMercado = "https://api.cartolafc.globo.com/atletas/mercado"
response = urllib.urlopen(urlMercado)
dataMercado = json.loads(response.read())

def getJogadoresConfirmados(posicao):
    atletaConfirmado = []
    for i in dataMercado["atletas"]:
        if i['status_id'] == 7 and i['posicao_id'] == posicao:
            atletaConfirmado.append(i['apelido'])
    return atletaConfirmado

def popularJogadoresConfirmados():
    listaDeConfirmados = []
    for i in range(0, 7):
        listaDeConfirmados.append(getJogadoresConfirmados(i))
    return listaDeConfirmados
