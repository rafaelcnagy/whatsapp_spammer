from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import string

contact_name = 'Pedro pontes'
message = ['TRAGA MINHA BOLSINHA PORRA!!!!', 'se bloquear é puta', 'BORA MERMAO, DEVOLVE ESSA MERDA', 'se nao devolver amanha, seu pau vai cair', 'block = 50 conto!', 'while (pedro == gado)<br>   bot_active = true;', 'só traz essa porra, tamo junto man']
min_delay = 30 #in seconds
max_delay = 50 #in seconds
min_interval = 480 #in seconds
max_interval = 600 #in seconds
min_count2interval = 100
max_count2interval = 150

browser = webdriver.Firefox()
browser.get('https://web.whatsapp.com/')
assert 'WhatsApp' in browser.title

print()
print('='*50)
print()
print('{:=^50}'.format(' BEM VINDO AO SPAM DA BOLSINHA '))
print()
print('{:^50}'.format('Faça login no Whatsapp Web'))
input('{:^50}'.format('e aperte ENTER para comecar'))
print()
print('='*50)
print()


print('Selecionando ' + contact_name)
try:
    elem = browser.find_element_by_class_name('jN-F5')
except NoSuchElementException:
    print('ALGO DEU ERRADO')
    exit()
else:
    elem.send_keys(contact_name + Keys.RETURN)
print(contact_name + ' selecionado')


try:
    elem = browser.find_element_by_class_name('_2S1VP')
except NoSuchElementException:
    print('ALGO DEU ERRADO')
    exit()

totalcount = 1
count = 0
count2interval = random.randint(min_count2interval, max_count2interval)

try:
    while True:
        elem = browser.find_element_by_class_name('_2S1VP')
        elem.send_keys(random.choice(message) + Keys.RETURN)
        if count == count2interval/2:
            random_str = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(25, 32)])
            elem.send_keys(random_str + Keys.RETURN)
        print(' --- Voce enviou a {}^a mensagem'.format(totalcount))
        if count > count2interval:
            count = 0
            print(' intervalo de {} segundos'.format(count2interval))
            count2interval = random.randint(min_count2interval, max_count2interval)
            time.sleep(min_interval, max_interval)
        else:
            time.sleep(random.randint(min_delay, max_delay))
        count += 1
        totalcount += 1
except KeyboardInterrupt:
    print('Interrompido!')

print('Tchau!')

