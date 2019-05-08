from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

contact_name = 'Pedro pontes'
message = '''TRAGA MINHA BOLSINHA PORRA!!!!
                se bloquear é puta'''
delay = 300 #in seconds

browser = webdriver.Firefox()
browser.get('https://web.whatsapp.com/')
assert 'WhatsApp' in browser.title

print('{:=^50}'.format('BEM VINDO AO SPAM DA BOLSINHA'))
print()
print('{:^50}'.format('Faça login no Whatsapp Web'))
input('{:^50}'.format('e aperte ENTER para comecar'))

print('Selecionando ' + contact_name)

try:
    elem = browser.find_element_by_class_name('jN-F5')
except NoSuchElementException:
    print('ALGO DEU ERRADO')
    exit()
else:
    elem.send_keys(contact_name + Keys.RETURN)

print(contact_name + ' selecionado')

count = 0
try:
    while True:
        elem = browser.find_element_by_class_name('_2S1VP')
        elem.send_keys(message + Keys.RETURN)
        count += 1
        print(' --- Voce enviou a {}^a mensagem'.format(count))
        time.sleep(delay)
except KeyboardInterrupt:
    print('Interrompido!')

print('Tchau!')

