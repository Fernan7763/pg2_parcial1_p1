# pg2_parcial1_p1

# Implementacion de clases y metodos de conversion de unidades de medida.

Una clase básica de conversión de unidades que admite conversiones específicas entre unidades.
Atributos:
_valor (float): El valor a convertir.
_unidad_origen (str): La unidad del valor a convertir.
_unidad_destino (str): La unidad de destino de la conversión.
_resultado (float): El resultado de la conversión.
Métodos:
_conversion_generica(valor, unidad_origen, unidad_destino):
Realiza una conversión genérica entre las unidades admitidas.
Conversiones admitidas:

- "metros" a "centímetros"
- "centímetros" a "kilómetros"
Genera:
ValueError: Si la conversión no es compatible.
_mostrar_resultados():
Muestra el resultado de la conversión en una cadena formateada.

Ejemplo de uso:

```python
conversor.metros_a_centimetros(10)  # 10 metros son 1000 centimetros
```
![Resultado](img/image.png)

```python
conversor.centimetros_a_kilometros(100000)  # 100000 centimetros son 1 kilometro

```

![Resultado](img/image2.png)
