from paso import Paso
import json

f = open('datos.json')
datos = json.load(f)
mapa = datos['mapa']
posicion_inicial = datos['posicion_inicial']
posicion_caja = datos['posicion_caja']

g = 0
posicion_actual = Paso(g, posicion_inicial, [], posicion_caja, 0, mapa)

lista_abierta = [posicion_actual]
lista_cerrada = []

limite_intentos = 0 # Casilleros disponibles en 0 en todo el Mapa
for fila in mapa:
    for casilla in fila:
        if (casilla == 0):
            limite_intentos += 1

def quitar_elemento_lista(elemento, lista):
    new_lista = []
    for e in lista:
        if (e != elemento):
            new_lista.append(e)
    return new_lista

def get_mejor_paso(pasos_posibles):
    mejor_paso = None
    for paso in pasos_posibles:
        paso_f = paso.get_f()
        if mejor_paso == None:
            mejor_paso = paso
        else:
            if (paso_f < mejor_paso.get_f()):
                mejor_paso = paso
    return mejor_paso

def quitar_pasos_previos(pasos_posibles, pasos_previos):
    new_pasos_posibles = []
    for paso_posible in pasos_posibles:
        paso_dado = False
        for paso_previo in pasos_previos:
            if (paso_previo.get_pos_actual() == paso_posible.get_pos_actual()):
                paso_dado = True
        if (paso_dado == False):
            new_pasos_posibles.append(paso_posible)
    return new_pasos_posibles

nodos_expandidos = 0

while(posicion_actual.get_h() > 0 and limite_intentos > 0):
    limite_intentos -= 1
    nodos_expandidos += 1
    mejor_paso = get_mejor_paso(lista_abierta)
    lista_abierta = quitar_elemento_lista(mejor_paso, lista_abierta)
    lista_cerrada.append(mejor_paso)
    posicion_actual = mejor_paso
    lista_abierta += quitar_pasos_previos(posicion_actual.get_pasos_validos(), lista_cerrada)

ultimo_paso = lista_cerrada[len(lista_cerrada) - 1]

print("Ruta: ")
print(ultimo_paso.get_ruta())
print("Costo Acumulado: ")
print(ultimo_paso.get_costo_acumulado())
print("Nodos Expandidos: ")
print(nodos_expandidos)