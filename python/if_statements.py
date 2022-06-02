loops = 0

def loopin_stuff(loops) : 
    select = input('Select 1 to continue the loop. Select 2 to end the loop: ')

    if select == '1':
        loops += 1
        loopin_stuff(loops)
    elif select == '2':
        print('End of loop')
        print(str(loops) + " loops have been executed") 
    else:
        print('1 or 2 was not selected')
        loopin_stuff(loops)

loopin_stuff(loops)
