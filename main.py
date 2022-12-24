import random
import string
import re
import os


print('''
░█████╗░██╗░░░██╗████████╗░█████╗░░██████╗░███████╗███╗░░██╗██╗░░░░░██╗███╗░░██╗███████╗
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔════╝░██╔════╝████╗░██║██║░░░░░██║████╗░██║██╔════╝
███████║██║░░░██║░░░██║░░░██║░░██║██║░░██╗░█████╗░░██╔██╗██║██║░░░░░██║██╔██╗██║█████╗░░
██╔══██║██║░░░██║░░░██║░░░██║░░██║██║░░╚██╗██╔══╝░░██║╚████║██║░░░░░██║██║╚████║██╔══╝░░
██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝╚██████╔╝███████╗██║░╚███║███████╗██║██║░╚███║███████╗
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝╚═╝░░╚══╝╚══════╝Dirify21
''')

i = 0
quantity = input('Кол-во строк:   ')
lenght = input('Кол-во символов:   ')
my_file = open("baseOne.txt", "w+")

while int(i) <= int(quantity):
    newText = [random.choice(string.ascii_lowercase + string.digits if i != 5 else string.ascii_uppercase) for i in range(int(lenght))]
    my_file.write(''.join(newText) + '\n')
    i += 1

my_file.close()
os.replace('baseOne.txt', 'Out/baseOne.txt')
print('Готово')
input('Нажмите ENTERE для выхода')