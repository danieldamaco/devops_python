class Pizzas:
    def __init__(self):
        self.types = ['pepperoni', 'hawaiana', '3 quesos', 'vegetariana']

class Orders:
    def __init__(self, id, status, user, pizza):
        self.id = id
        self.status= status
        self.user = user
        self.pizza = pizza

class Users:
    def __init__(self, name):
        self.name = name

class Admin(Users):
    def __init__(self, id, token):
        super().__init__(id)
        self.token = token 