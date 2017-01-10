def piglatin():

    x=raw_input('Input a word: ')
    
    if len(x)==0 and x.isalpha() == False:
        print 'This is not a valid word'
    else: 
        z=x[0]
        x=x+z
        x=x+'ay'
        print 'Your name in pig latin is %s' %(x)

piglatin()

