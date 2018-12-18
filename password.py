passwordFile = open('SecretPasswordFile.txt')
secretPassword = passwordFile.read().lstrip().rstrip()
typedPassword = input('Enter your password: ')
if (typedPassword == secretPassword):
    print('Access granted')
    if (typedPassword == '123456789'):
        print('That password is one that an idiot puts on their luggage.')
else:
    print('Access denied')

while True:
    print('Who are you?')
    name = input('Name: ')
    if name != 'Zero':
        continue
    print('Hi, Zero. What is the password? (It is a Inf..)')
    password = input('Password: ')
    if password == 'infinity':
        break
print('Access granted Zero')
