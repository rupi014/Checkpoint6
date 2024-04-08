class Usuario:
    def __init__(self, name, password):
        self.name = name
        self.password = password

# Crear un objeto Usuario
usuario1 = Usuario("Rubens", "12345678")

# Acceder a los atributos del objeto Usuario
print(usuario1.name)
print(usuario1.password)

# En este ejemplo, la clase Usuario tiene un método __init__ que inicializa los atributos name y password cuando se crea un objeto. Luego, se crea un objeto usuario1 con el nombre de usuario "Rubens" y la contraseña "12345678". Finalmente, se imprimen los atributos del objeto usuario1.