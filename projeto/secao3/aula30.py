'''
Constantes = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
   <- Contagem de complexidade (ruim)
'''
velocidade = 61 # Velocidade atual do carro
local_carro = 101 # Local em que o carro está na estrada

RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

velocidade_carro_passou_radar1 = velocidade > RADAR_1

carro_passou_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) 

carroMultadoRadar1 = velocidade_carro_passou_radar1 and carro_passou_radar1

if velocidade_carro_passou_radar1:
    print("Velocidade carro passou do radar 1")

if carro_passou_radar1:
    print("Carro passou do radar 1")

if carroMultadoRadar1:
    print("Carro foi multado no radar 1")