from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json
import random
import string

with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    contact_name = data['contact']
    messages = data['messages']

min_delay = 100 #in seconds
max_delay = 200 #in seconds
min_interval = 480 #in seconds
max_interval = 600 #in seconds
min_count2interval = 20 #in seconds
max_count2interval = 26 #in seconds

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
    elem = browser.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]')
except NoSuchElementException:
    print('ALGO DEU ERRADO')
    exit()
else:
    elem.send_keys(contact_name + Keys.RETURN)
print(contact_name + ' selecionado')


try:
    elem = browser.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div/div[2]')
except NoSuchElementException:
    print('ALGO DEU ERRADO')
    exit()

totalcount = 1
count = 0
count2interval = random.randint(min_count2interval, max_count2interval)
''
try:
    while True:
        elem = browser.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div/div[2]')
        elem.send_keys(random.choice(messages) + Keys.RETURN)
        if count == count2interval/2:
            random_str = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(25, 32)])
            elem.send_keys(random_str + Keys.RETURN)
        print(' --- Voce enviou a {}^a mensagem'.format(totalcount))
        if count > count2interval:
            count = 0
            interval = random.randint(min_interval, max_interval)
            print(' intervalo de {} segundos'.format(interval))
            count2interval = random.randint(min_count2interval, max_count2interval)
            time.sleep(interval)
        else:
            time.sleep(random.randint(min_delay, max_delay))
        count += 1
        totalcount += 1
except KeyboardInterrupt:
    print('Interrompido!')

print('Tchau!')

