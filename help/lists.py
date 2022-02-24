# se pueden guarar listas dentro de otra lista

demo_list = [1, "hello", False, [1, 2, 3]]

#constructor

cosas_list = list([1, "Hola", True, [1, 2, 3]])

print(cosas_list)
print(type(cosas_list))

#rango numeros entre medio

range = list(range(1, 10))

print(range)

print(type(cosas_list))

#print(dir(cosas_list))


#metodos
print(len(cosas_list))
print(cosas_list[3])
print(1 in cosas_list)


print(cosas_list)
#cambiar elementos de la lista

cosas_list[3] = "mierda"

print(cosas_list)

#agregar elementos a la lista

cosas_list.append(('ta difici', 'mierda'))
print(cosas_list)


cosas_list.append(['ta difici', 'mierda'])
    #no sirve el apend para agregar varios elementos y 
    #y que los agrege de forma independiente
print(cosas_list)


cosas_list.extend(['ta dificil', 'mierda'])
print(cosas_list)

#insertar algo en un lugar espec'ifico

cosas_list.insert(1, 'violet')

print(cosas_list)

cosas_list.insert(len(cosas_list), 'violin')

print(cosas_list)

cosas_list.pop(1)

print(cosas_list)

#para quitar especifico

cosas_list.remove('mierda')

print(cosas_list)

cosas_list.clear # no recibe ARGUMENTOS

print(cosas_list)

print(cosas_list.index('mierda'))







