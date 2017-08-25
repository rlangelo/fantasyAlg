import urllib, json

urlMercado = "https://api.cartolafc.globo.com/atletas/mercado"
response = urllib.urlopen(urlMercado)
dataMercado = json.loads(response.read())

urlClubes = "https://api.cartolafc.globo.com/clubes"
responseClubes = urllib.urlopen(urlClubes)
dataClubes = json.loads(responseClubes.read())

urlPartidas = "https://api.cartolafc.globo.com/partidas/21"
responsePartidas = urllib.urlopen(urlPartidas)
dataPartidas = json.loads(responsePartidas.read())

def getJogadoresConfirmados(posicao):
    atletaConfirmado = []
    for i in dataMercado["atletas"]:
        jogador = []
        if i['status_id'] == 7 and i['posicao_id'] == posicao:
            jogador.append(i['apelido'])
            jogador.append(i['clube_id'])
            atletaConfirmado.append(jogador)
    return atletaConfirmado

def popularJogadoresConfirmados():
    listaDeConfirmados = []
    for i in range(0, 7):
        listaDeConfirmados.append(getJogadoresConfirmados(i))
    return listaDeConfirmados

def getPosicao(id):
    posicao = dataClubes[id]['posicao']
    return posicao

#Se time joga em casa, Return 1; Se fora, Return 0
def getCasaOuFora(id):
    for i in dataPartidas["partidas"]:
        if i['clube_casa_id'] == id:
            return 1
        elif i['clube_visitante_id'] == id:
            return 0

def getAproveitamento(id):
    for i in dataPartidas["partidas"]:
        if i['clube_casa_id'] == id:
            aproveitamento = i['aproveitamento_mandante']
            return aproveitamento
        elif i['clube_visitante_id'] == id:
            aproveitamento = i['aproveitamento_visitante']
            return aproveitamento

def getAproveitamentoMult(id):
    aproveitamento = []
    for i in dataPartidas["partidas"]:
        if i['clube_casa_id'] == id:
            aproveitamento = i['aproveitamento_mandante']
            return parseAproveitamento(aproveitamento)
        elif i['clube_visitante_id'] == id:
            aproveitamento = i['aproveitamento_visitante']
            return parseAproveitamento(aproveitamento)

def parseAproveitamento(aproveitamento):
    contador = 0
    for i in range(0, 5):
        if aproveitamento[i] == "v":
            contador = contador + 1
        elif aproveitamento[i] == "d":
            contador = contador - 1
    if contador < 0:
        contador = 0
    return contador