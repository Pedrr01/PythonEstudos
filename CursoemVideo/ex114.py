import urllib
import urllib.request
from time import sleep

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Acessando...')
    sleep(2)
    print('\033[31mO site não está acessivel no momento!!!\033[0m')
else:
    print('Acessando...')
    sleep(2)
    print('Site acessado com sucesso.')
finally:
    print('FIM DO PROGRAMA...')
