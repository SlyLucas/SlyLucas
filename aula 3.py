a = int(input('primeiro bimestre: '))
if a > 10:
    a = int(input('voce digitou errado. primeiro bimestre:'))
b = int(input('segundo bimestre: '))
if b > 10:
    b = int(input('voce digitou errado. segundo bimestre:'))
c = int(input('terceiro bimestre: '))
if c > 10:
    c = int(input('voce digitou errado. terceiro bimestre:'))
d = int(input('quarto bimestre: '))
if d > 10:
    d = int(input('voce digitou errado. quarto bimestre:'))
media = (a + b + c + d) / 4
print('media: {}'.format(media))
# if a <= 10 and b <= 10 and c <= 10 and c <= 10:
#     print('media: {}'.format(media))
# else:
#     print('foi informado alguma nota errado')

#
# a = int(input('primeiro valor: '))
# b = int(input('segundo valor: '))
# c = int(input('terceiro valor: '))
#
# if a > b and a > c:
#     print('o maior numero é {}'.format(a))
# elif b > a and b > c:
#     print('o maior numero é {}'.format(b))
# else:
#     print('o maior numero é {}'.format(c))
# print('final do programa')
