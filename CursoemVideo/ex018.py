from math import sin, cos, tan, radians
ang = float(input("Digite o ângulo:"))
sen = sin(radians(ang))
cs = cos(radians(ang))
tg = tan(radians(ang))
print(' SEN = {:.2f} \n COS = {:.2f} \n TAN = {:.2f}'.format(sen, cs, tg))
