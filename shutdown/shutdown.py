import os

choice = input("shutdown? (y or n)")

if choice == 'y' or choice == 'Y':
    os.system('shutdown /r')
else:
    print('exiting')
