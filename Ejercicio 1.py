class ConversorBasico:
    def __init__(self):
        self._valor = 0
        self._unidad_origen = ""
        self._unidad_destino = ""
        self._resultado = 0

    def _conversion_generica(self, valor, unidad_origen, unidad_destino):
        self._valor = valor
        self._unidad_origen = unidad_origen
        self._unidad_destino = unidad_destino
        if unidad_origen == "metros" and unidad_destino == "centimetros":
            self._resultado = valor * 100
        elif unidad_origen == "centimetros" and unidad_destino == "kilometros":
            self._resultado = valor / 100000
        else:
            raise ValueError("Conversión no soportada")

    def _mostrar_resultados(self):
        print(f"{self._valor} {self._unidad_origen} son {self._resultado} {self._unidad_destino}", end=". \n")
    
class ConversorDistancia(ConversorBasico):
    def metros_a_centimetros(self, valor):
        self._conversion_generica(valor, "metros", "centimetros")
        self._mostrar_resultados()

    def centimetros_a_kilometros(self, valor):
        self._conversion_generica(valor, "centimetros", "kilometros")
        self._mostrar_resultados()
    
# Ejemplo de uso

conversor = ConversorDistancia()
conversor.metros_a_centimetros(10)  # 10 metros son 1000 centimetros
conversor.centimetros_a_kilometros(100000)  # 100000 centimetros son 1 kilometro

