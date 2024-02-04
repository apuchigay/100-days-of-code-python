class User:
    def __init__(self, user_id, username):
        # Inicializamos/creamos los valores iniciales de nuestros atributos
        self.user_id = user_id
        self.username = username
        self.followers = 0  # Definimos el valor del atributo por defecto
        self.following = 0

    def follow(self, user):  # el segundo parametro es el usuario al que decimidos seguir
        user.followers += 1  # El contador aumenta para el user que estamos siguiendo
        self.following += 1  # El contador aumenta para la cantidad de users que seguimos


user_1 = User("001", "Andres")
user_2 = User("002", "Diego")

# Pasamos como parametro a la persona que user_1 empezó a seguir
user_1.follow(user_2)

# Seguidores y seguidos de user_1
print(user_1.followers)
print(user_1.following)

# Seguidores y seguidos de user_2
print(user_2.followers)
print(user_2.following)
