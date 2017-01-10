def digit_sum(n):
    x=[]
    y=str(n)
    for char in y:
        z=int(char)
        x.append(z)
    return sum(x)

def is_int(x):
    y=int(x)
    if (x-y)==0:
        return True
    else:
        return False

def is_even(x):
    if x%2==0:
        return True
    else:
        return False

def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)

def is_prime(x):
    if x<2:
        return False
    for i in range(2,x+1):
        if (x/i)==1:
            return True
        elif x%i==0:
            return False

def reverse(text):
    x = []
    y = ""
    i = len(text)-1
    while i >= 0:
        x.append(text[i])
        i-=1
    for char in x:
        y=y+char
    return yr

def anti_vowel(text):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    x=[]
    t=list(text)
    for char in text:
        if char not in vowels:
            x.append(char)
    return ''.join(x)

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         

def scrabble_score(word):
    result=0
    word=word.lower()
    for char in word:
        result+=score[char]
    return result

