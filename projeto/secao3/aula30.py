'''
Constantes = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
   <- Contagem de complexidade (ruim)
'''
velocidade = 61 # Velocidade atual do carro
localCarro = 101 # Local em que o carro está na estrada

RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

velocidadeCarroPassouRadar1 = velocidade > RADAR_1

carroPassouRadar1 = localCarro >= (LOCAL_1 - RADAR_RANGE) and localCarro <= (LOCAL_1 + RADAR_RANGE) 

carroMultadoRadar1 = velocidadeCarroPassouRadar1 and carroPassouRadar1

if velocidadeCarroPassouRadar1:
    print("Velocidade carro passou do radar 1")

if carroPassouRadar1:
    print("Carro passou do radar 1")

if carroMultadoRadar1:
    print("Carro foi multado no radar 1")