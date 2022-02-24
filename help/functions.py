# porcion de codigo que procesa y devuelve un resultado
# se pueden crear funciones

def hello(name="person"):
    print("la concha de la lora", name)

hello("asd")
hello("gd")
hello()


def add(one, ntwo):
    return one + ntwo

print(add(10, 30))
print(add(500, 3))

suma = lambda uno, dos: uno + dos

print(suma(1,2))
