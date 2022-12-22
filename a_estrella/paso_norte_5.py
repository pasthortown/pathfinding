import math

class Paso:
    def __init__(self, g , pos_actual, ruta, pos_meta, costo_acumulado, mapa):
        self.g = g
        self.costo_acumulado = costo_acumulado
        self.pos_actual = pos_actual
        self.ruta = ruta
        self.pos_meta = pos_meta
        self.mapa = mapa
    
    def get_f(self):
        return self.g + self.get_h()

    def get_g(self):
        return self.g
    
    def get_h(self):
        return abs(self.pos_meta[0] - self.pos_actual[0]) + abs(self.pos_meta[1] - self.pos_actual[1])
    
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
            if (self.pos_actual[0] > casilla_valida[0]):
                # el costo de ir al norte es 5
                incremento_g = 5
            else:
                # el costo de ir al sur, al este o al oeste es 1
                incremento_g = 1
            toReturn.append(Paso(self.g + incremento_g, casilla_valida, ruta, self.pos_meta, self.costo_acumulado + incremento_g, self.mapa))
        return toReturn

    def get_pasos_validos_Ecludia(self):
        casillas_validas = []
        # Distancia Euclidea
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
            if (self.pos_actual[0] > casilla_valida[0]):
                # el costo de ir al norte es 5 y a los lados 1
                incremento_g = math.sqrt(math.pow(5,2) + 1)
            else:
                # el costo de ir al sur es 1 y a los lados 1
                incremento_g = math.sqrt(2)
            toReturn.append(Paso(self.g + incremento_g, casilla_valida, ruta, self.pos_meta, self.costo_acumulado + incremento_g, self.mapa))
        return toReturn

    def get_pasos_validos(self):
        toReturn = []
        toReturn += self.get_pasos_validos_Manhattan()
        toReturn += self.get_pasos_validos_Ecludia()
        return toReturn