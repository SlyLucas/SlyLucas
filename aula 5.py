lista_numerica = [12, 10, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

lista_animal[0] = 'macaco'


tupla = (1, 10, 12, 14)
print(len(tupla))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)

#print(lista_animal[1])
# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)



# if 'lobo' in  lista_ainal:
#     print('existe um lobo na lista')
# else:
#     print('não existe um lobo na lista. será incluido')
#     lista_animal.append('lobo')
#     print(lista_animal)
#
# lista_animal.pop(1)
# print(lista_animal)