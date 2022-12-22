import math

class Paso:
    def __init__(self, n, pos_actual, ruta, pos_meta, costo_acumulado, mapa):
        self.n = n
        self.costo_acumulado = costo_acumulado
        self.pos_actual = pos_actual
        self.ruta = ruta
        self.pos_meta = pos_meta
        self.mapa = mapa
    
    def get_n(self):
        return self.n
    
    def get_costo_acumulado(self):
        return self.costo_acumulado

    def get_ruta(self):
        self.ruta.append(self.pos_actual)
        return self.ruta

    def get_pos_actual(self):
        return self.pos_actual
    
    def get_pos_meta(self):
        return self.pos_meta

    def get_pasos_validos_Manhattan(self):
        casillas_validas = []
        # Distancia de Manhattan
        costo = 1
        # norte
        if (self.pos_actual[0] - 1 >= 0):
            if (self.mapa[self.pos_actual[0] - 1][self.pos_actual[1]] == 0):
                casillas_validas.append([self.pos_actual[0] - 1, self.pos_actual[1]])
        # sur
        if (self.pos_actual[0] + 1 <= len(self.mapa) - 1):
            if (self.mapa[self.pos_actual[0] + 1][self.pos_actual[1]] == 0):
                casillas_validas.append([self.pos_actual[0] + 1, self.pos_actual[1]])
        # este
        if (self.pos_actual[1] - 1 >= 0):
            if (self.mapa[self.pos_actual[0]][self.pos_actual[1] - 1] == 0):
                casillas_validas.append([self.pos_actual[0], self.pos_actual[1] - 1])
        # oeste
        if (self.pos_actual[1] + 1 <= len(self.mapa[self.pos_actual[0]]) - 1):
            if (self.mapa[self.pos_actual[0]][self.pos_actual[1] + 1] == 0):
                casillas_validas.append([self.pos_actual[0], self.pos_actual[1] + 1])
        toReturn = []
        for casilla_valida in casillas_validas:
            ruta = []
            ruta += self.ruta
            ruta.append(self.pos_actual)
            toReturn.append(Paso(self.n + 1, casilla_valida, ruta, self.pos_meta, self.costo_acumulado + costo, self.mapa))
        return toReturn

    def get_pasos_validos_Ecludia(self):
        casillas_validas = []
        # Distancia Euclidea
        costo = math.sqrt(2)
        # noreste
        if ((self.pos_actual[0] - 1 >= 0) and (self.pos_actual[1] - 1 >= 0)):
            if (self.mapa[self.pos_actual[0] - 1][self.pos_actual[1] - 1] == 0):
                casillas_validas.append([self.pos_actual[0] - 1, self.pos_actual[1] - 1])
        # noroeste
        if ((self.pos_actual[0] - 1 >= 0) and (self.pos_actual[1] + 1 <= len(self.mapa[self.pos_actual[0]]) - 1)):
            if (self.mapa[self.pos_actual[0] - 1][self.pos_actual[1] + 1] == 0):
                casillas_validas.append([self.pos_actual[0] - 1, self.pos_actual[1] + 1])
        # sureste
        if ((self.pos_actual[0] + 1 <= len(self.mapa) - 1) and (self.pos_actual[1] - 1 >= 0)):
            if (self.mapa[self.pos_actual[0] + 1][self.pos_actual[1] - 1] == 0):
                casillas_validas.append([self.pos_actual[0] + 1, self.pos_actual[1] - 1])
        # suroeste
        if ((self.pos_actual[0] + 1 <= len(self.mapa) - 1) and (self.pos_actual[1] + 1 <= len(self.mapa[self.pos_actual[0]]) - 1)):
            if (self.mapa[self.pos_actual[0] + 1][self.pos_actual[1] + 1] == 0):
                casillas_validas.append([self.pos_actual[0] + 1, self.pos_actual[1] + 1])
        toReturn = []
        for casilla_valida in casillas_validas:
            ruta = []
            ruta += self.ruta
            ruta.append(self.pos_actual)
            toReturn.append(Paso(self.n + 1, casilla_valida, ruta, self.pos_meta, self.costo_acumulado + costo, self.mapa))
        return toReturn

    def get_pasos_validos(self):
        toReturn = []
        toReturn += self.get_pasos_validos_Manhattan()
        toReturn += self.get_pasos_validos_Ecludia()
        return toReturn