# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
from urllib import request

try:
    site = urllib.request.urlopen("http://pudim.com.br/")
except:
    print("O site não está acessível.")
else:
    print("O site está funcionando normalmente.")