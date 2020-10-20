numbers = range(0,100)
output = ''
for number in numbers:
    if number % 2 == 0:
        output += 'foo'
    if number % 3 == 0:
        output += 'bar'
    
    if output == '':
        output = str(number)
    print(output + '\n') 
    output = ''
 