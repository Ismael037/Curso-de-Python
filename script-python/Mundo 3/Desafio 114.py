import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.error.URLError:
    print('O site pudim não está disponível')
else:
    print('O site Pudim está dísponivel')
