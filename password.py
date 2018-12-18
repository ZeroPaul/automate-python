passwordFile = open('SecretPasswordFile.txt')
secretPassword = passwordFile.read().lstrip().rstrip()
typedPassword = input('Enter your password: ')
if (typedPassword == secretPassword):
    print('Access granted')
    if (typedPassword == '123456789'):
        print('That password is one that an idiot puts on their luggage.')
else:
    print('Access denied')
