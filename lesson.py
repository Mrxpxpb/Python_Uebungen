number = 0
maximum = None
try:
    #number = int(input('Numbers:'))
    maximum = int(input('Max:'))

    for number in range (2, maximum):
        print(number)

   # if number % 2 == 0:
   #     print('Even: ', number)
    #elif number > 100:
    #    print('Too High: ', number)
    #elif number < 0:
    #    print('Too Low: ', number)
except:
    print('Error: ')
    

   