<h1 align="center">Checkpoint 6</h1>
<h2 align="center">Rubens Ballester Lillo</h2>

<h3 align="center">¿Para qué usamos las clases en Python?</h3>  

#### ¿Qué son las clases en Python?

En Python, una clase es una especie de "plano" o "plantilla" que define las propiedades y comportamientos comunes que un tipo de objeto puede tener. Estas propiedades se llaman atributos y los comportamientos se llaman métodos. La clase en sí misma no es un objeto, sino más bien una descripción de cómo crear un objeto.

#### ¿Por qué usar clases en Python?

1. **Organización del código**: Las clases permiten organizar el código de manera estructurada y modular. En lugar de tener todas las variables y funciones dispersas por el código, podemos agruparlas en clases relacionadas, lo que facilita la comprensión y el mantenimiento del código, especialmente en proyectos grandes.
2. **Reutilización de código** : La definición de clases permite encapsular funcionalidades relacionadas en un solo lugar. Esto facilita la reutilización del código, ya que podemos crear múltiples instancias (objetos) de una clase y reutilizar su funcionalidad en diferentes partes de nuestro programa sin tener que volver a escribir el mismo código.
3. **Abstracción**: Las clases nos permiten modelar objetos del mundo real en nuestro código. Podemos representar características y comportamientos comunes de estos objetos a través de atributos y métodos, lo que facilita la comprensión del código para los desarrolladores y permite una mejor comunicación entre el código y el problema real que estamos tratando de resolver.


#### Sintaxis de definición de clases en Python:
 ```
   class NombreClase:
    # Constructor
    def __init__(self, atributo1):
        self.atributo1 = atributo1

    # Definición de métodos
    def nombre_metodo(self, argumentos):
        # Código del método

 ```

En esta sintaxis:  

1. ```class NombreClase```: define la clase con el nombre NombreClase.
2. ```def __init__ (self, atributo1)```: es el constructor de la clase que se llama automáticamente cuando se crea una nueva instancia de la clase. El parámetro self se refiere a la instancia actual de la clase, y se utiliza para acceder a sus atributos y métodos.
3. ```self.atributo1``` es un ejemplo de cómo definir y asignar valores a los atributos de la clase.
4. ```def nombre_metodo(self, argumentos)```: define un método de la clase. Al igual que el constructor, el parámetro self se refiere a la instancia actual de la clase.

#### Ejemplo detallado de uso de clases en Python:

```
class Coche:
    # Constructor
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    # Método para imprimir información del coche
    def imprimir_info(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Color:", self.color)

# Crear una instancia de la clase Coche
mi_coche = Coche("Volkswagen", "Golf", "Gris")

# Acceder a los atributos y métodos del coche
print("Marca del coche:", mi_coche.marca)
mi_coche.imprimir_info()

```

Salida: 
```
Marca del coche: Volkswagen
Marca: Volkswagen
Modelo: Golf
Color: Gris
```
En esta sintaxis:  

1. Se define un método especial llamado ```__init__```, que es el constructor de la clase. Este método se llama automáticamente cuando se crea una nueva instancia de la clase. Toma tres parámetros (marca, modelo, y color) además del parámetro ```self```, que hace referencia a la instancia actual de la clase. Dentro del constructor, se asignan los valores de los parámetros a los atributos de la instancia utilizando self.
2. Se define otro método llamado ```imprimir_info```, que imprime la información del automóvil, es decir, la marca, el modelo y el color.
3. Se crea una instancia de la clase Coche llamada ```mi_coche``` pasando los valores "Volkswagen", "Golf", y "Gris" como argumentos al constructor.
4. Se accede a los atributos del ```objeto mi_coche``` (marca, modelo, y color) usando la notación de punto y se imprime la marca del coche.
5. Se llama al método ```imprimir_info``` del objeto ```mi_coche```, que imprime la información completa del coche (marca, modelo y color) utilizando el método definido en la clase.

---

</br>

<h3 align="center">¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?</h3>  
</br>
Una instancia de una clase es un objeto específico creado a partir de esa clase. En otras palabras, una instancia es una copia individual de una clase que tiene sus propios valores para los atributos definidos en la clase y puede ejecutar sus propios métodos.  

Para crear una instancia de una clase en Python, simplemente llamamos al nombre de la clase seguido de paréntesis, opcionalmente pasando los argumentos requeridos por el constructor de la clase. Por ejemplo, si tenemos una clase llamada Coche, podemos crear una instancia de ella de la siguiente manera:  

```
mi_coche = Coche(argumentos)
```

Cuando se crea una instancia de una clase en Python, el método que se ejecuta automáticamente es el método especial ```__init__```, también conocido como el constructor de la clase. Este método se utiliza para inicializar los atributos de la instancia recién creada.  
</br>
**Constructor ```(__init__)```**:
</br>
El constructor es un método especial en Python que se llama automáticamente cuando se crea una nueva instancia (objeto) de una clase. Su nombre es ```__init__``` (doble guion bajo, seguido por "init" y otro doble guion bajo).    
#### Ejemplo:  

```
def __init__(self, argumentos_constructor):
    # Cuerpo del constructor
```
1. El primer parámetro del método ```__init__``` es ```self```, que hace referencia a la instancia actual de la clase.
2. Los parámetros restantes representan los valores que se pasan al crear la instancia de la clase.
3. Dentro del constructor, se asignan estos valores a los atributos de la instancia utilizando ```self```.

Por ejemplo, en el código del ejemplo anterior:

```
def __init__(self, marca, modelo, color):
    self.marca = marca
    self.modelo = modelo
    self.color = color
```
1. ```def __init__(self, marca, modelo, color)```: Aquí definimos el método especial ```__init__```, que es el constructor de la clase ```Coche```. Este método se llama automáticamente cada vez que se crea una nueva instancia de la clase. Toma cuatro parámetros: ```self``` (que hace referencia a la instancia actual de la clase) y los atributos específicos de un coche: marca, modelo y color.

2. ```self.marca = marca```: Esta línea asigna el valor del parámetro marca al atributo marca de la instancia actual (referenciada por self). Esto significa que cada instancia de la clase Coche tendrá su propia variable marca con el valor que se le pase al crear la instancia.

3. ```self.modelo = modelo```: Similarmente, esta línea asigna el valor del parámetro modelo al atributo modelo de la instancia actual. Cada instancia tendrá su propio valor para el modelo del coche.

4. ```self.color = color```: Aquí, se asigna el valor del parámetro color al atributo color de la instancia actual. De esta manera, cada instancia puede tener su propio color asignado.  

Por lo tanto, cuando creamos una nueva instancia de la clase ```Coche``` como ```mi_coche```, se llama automáticamente al método ```__init__```, pasando los valores especificados como argumentos al crear la instancia. Esto asegura que la instancia se inicialice correctamente con los valores proporcionados.   

---

</br>

<h3 align="center">¿Qué es una API?</h3>  
</br>

Definición:

Una API (Interfaz de Programación de Aplicaciones) es un conjunto de reglas y protocolos que permite que diferentes sistemas informáticos se comuniquen entre sí. En otras palabras, proporciona un conjunto de herramientas y definiciones que permiten que una aplicación use ciertas funciones o acceda a ciertos datos de otra aplicación, servicio o sistema operativo de manera segura y controlada.  

Ejemplo:

Para entender de manera algo más simple que es una API, esta es como un camarero en un restaurante. El camarero toma tu pedido (solicitud), comunica esa solicitud al cocinero (servidor) y luego trae tu comida (respuesta) de vuelta a ti. En este caso, el camarero actúa como una interfaz entre tú y el chef, simplificando el proceso de pedir comida.  
