'''add introduciton'''
'''get a random number betwen 0 to 19'''
import random
right_number = random.randint(0,20)

# google'python 生成随机数', get random, google' python random' get MVP

''' print introduction'''
print ('''
       game rules:
       We will choose a random integer less than 20, 
       you have 10 times to guess,
       the less time, the better~
       ''')

'''10 times loop'''
for i in range(0,10):

    '''input'''
    guess_number = int(input('>>'))    
    '''choice'''    
    if guess_number < right_number:
        print ("less than the right number" )
    elif 20 > guess_number > right_number:
        print ("more than the right number" )
    elif guess_number > 20:
        print ('please input a integer less than 20')
    else:
        print ('Correct! Fantastic! see you!')
        break
print ('the correct number is %d'%right_number)