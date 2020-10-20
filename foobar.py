for number in range(1, 100):
    output = ''
    if number % 2 == 0:
        output += 'foo'
    if number % 3 == 0:
        output += 'bar'    
    if output == '':
        output = str(number)
    print(output) 
    
 