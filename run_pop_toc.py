from pop_toc_functions import *
# We will need to import our functions
# Play the game and while loop here
user_input = ''

while user_input != 'whatever':
    user_input = int(input('SHOW ME WHAT YOU GOT!!! (Integers only)').strip())
    if div3(user_input) and div5(user_input):
        print('POPTOC')
    elif div3(user_input):
        print('POP')
    elif div5(user_input):
        print('TOC')
    else:
        while True:
            print('potato')
        #this has to have an exit statement (break) otherwise it will go from the top
    print(user_input) #this will run