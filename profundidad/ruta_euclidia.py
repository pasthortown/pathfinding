from paso import Paso
import json

archivo = open('datos.json')
datos = json.load(archivo)
mapa = datos['mapa']
posicion_inicial = datos['posicion_inicial']
posicion_caja = datos['posicion_caja']

def excluir_elementos_lista(lista, elementos_excluir):
    new_lista = []
    for e in lista:
        excluir = False
        for e_excluir in elementos_excluir:
            if (e_excluir.get_pos_actual() == e.get_pos_actual()):
                excluir = True
        if (excluir == False):
            new_lista.append(e)
    return new_lista

camino_encontrado = None
posicion_actual = Paso(posicion_inicial, [], posicion_caja, 0, mapa)
nodos_explorados = [posicion_actual]
nodos_por_explorar = posicion_actual.get_pasos_validos()
iteraciones = 0
nodos_expandidos = 0

def explorar_camino(nodo: Paso):
    global iteraciones
    global nodos_expandidos
    global camino_encontrado
    global nodos_explorados
    global nodos_por_explorar
    global posicion_caja
    iteraciones += 1
    nodos_expandidos += 1
    if (nodo.get_pos_actual() == posicion_caja and camino_encontrado == None):
        camino_encontrado = nodo
    if (camino_encontrado == None):
        nodos_posibles = nodo.get_pasos_validos()
        nodos_explorados.append(nodo)
        nodos_por_explorar += nodos_posibles
        nodos_por_explorar = excluir_elementos_lista(nodos_por_explorar, nodos_explorados)
        for nodo_posible in nodos_posibles:
            if (nodo_posible.get_pos_actual() == posicion_caja):
                camino_encontrado = nodo_posible
                nodos_explorados.append(nodo_posible)
                break
        if (len(nodos_por_explorar) > 0):
            explorar_camino(nodos_por_explorar[0])

explorar_camino(nodos_por_explorar[0])

print("Ruta: ")
print(camino_encontrado.get_ruta())
print("Costo Acumulado: ")
print(camino_encontrado.get_costo_acumulado())
print("Nodos Expandidos: ")
print(nodos_expandidos)