import os
import random
import time

x = 0
while x == 0:
    b = input('Готов? \n')

    if b == 'нет':
        print('Ладно')
        time.sleep(3)
        quit()
    else:
        print('Крутим барабан:')

    a = ['1', '2', '3', '4', '5', '6']
    a = random.choice(a)

    if a == str(1):
        print('Бах!')
        time.sleep(3)
        os.system('start https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        quit()
    elif a == str(2):
        print('О-о-о повезло, повезло!')
    elif a == str(3):
        print('О-о-о повезло, повезло!')
    elif a == str(4):
        print('О-о-о повезло, повезло!')
    elif a == str(5):
        print('О-о-о повезло, повезло!')
    elif a == str(6):
        print('О-о-о повезло, повезло!')
    else:
        print('Что-та поломалося :(')
