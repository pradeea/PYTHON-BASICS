
def func(word):
    first_word=word[0]

    if word in 'aeiou':
        pig_word=word+'ay'

    else:
        pig_word=word[1:]+first_word+'ay'

    return pig_word



        
    
