from paso import Paso
import json

def excluir_elementos_lista(lista, elementos_excluir):
    new_lista = []
    for e in lista:
        excluir = False
        for e_excluir in elementos_excluir:
            if (e_excluir.pos_actual == e.pos_actual):
                excluir = True
        if (excluir == False):
            new_lista.append(e)
    return new_lista

archivo = open('datos.json')
datos = json.load(archivo)
mapa = datos['mapa']
posicion_inicial = datos['posicion_inicial']
posicion_caja = datos['posicion_caja']

n = 0
posicion_actual = Paso(n, posicion_inicial, [], posicion_caja, 0, mapa)
arbol_exploracion = [[posicion_actual]]
nodos_explorados = [posicion_actual]
camino_encontrado = None

limite_intentos = 0 # Casilleros disponibles en 0 en todo el Mapa
for fila in mapa:
    for casilla in fila:
        if (casilla == 0):
            limite_intentos += 1

nodos_expandidos = 0

while(camino_encontrado == None and limite_intentos > 0):
    limite_intentos -= 1
    nodos_posibles = []
    for nodo in arbol_exploracion[n]:
        nodos_explorados.append(nodo)
        nodos_posibles += nodo.get_pasos_validos()
        nodos_nuevos = excluir_elementos_lista(nodos_posibles, nodos_explorados)
        nodos_expandidos += 1
    n += 1
    arbol_exploracion.append(nodos_nuevos)
    for nodo in nodos_nuevos:
        if (nodo.get_pos_actual() == posicion_caja):
            camino_encontrado = nodo

print("Ruta: ")
print(camino_encontrado.get_ruta())
print("Costo Acumulado: ")
print(camino_encontrado.get_costo_acumulado())
print("Nodos Expandidos: ")
print(nodos_expandidos)

