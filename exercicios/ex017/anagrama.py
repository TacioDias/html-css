print('Calcular Anagrama\n')
crt = str(input('Digite qualquer coisa: '))
v = len(crt) - crt.count(' ')
print ('\nQuantos caracteres existem:',v)
print('')
max = v
min = 1
print('a ',v)
while max > 0:
    