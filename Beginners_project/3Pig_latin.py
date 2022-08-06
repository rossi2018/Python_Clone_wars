# Pig Latin is a secret language used by children in which any consonants at the beginning
# of a word are placed at the end, followed by -ay; for example cathedral becomes athedralcay. 
#  Slang.

# What is Pig Latin origin?
# In fact, Pig Latin may go all the way back to the time of Shakespeare. Many trace its roots 
# back to a Medieval language game called Dog Latin. It was very popular and was even mentioned 
# in Shakespeare's “Love's Labour's Lost.” A more recent predecessor was Hog Latin, which became 
# popular in the mid-1800s.

sentence = input('Enter the sentence to translate to pig latin').upper()
vowels = {'A', 'E', 'I', 'O', 'U'} 
words = sentence.strip().split(' ') 
pig_latin = [] 
 
for word in words: 
    if word[0] in vowels: 
        pig_latin.append(word + 'AY') 
    else: 
        pig_latin.append(word[1:] + word[0] + 'AY') 
 
print(' '.join(pig_latin)) 

#incomplete implementation with function 

# def pig_latin(sentence): 
#     result = "" 
#     for word in sentence.split(): 
#         result += word[1:] + word[0] + "AY " 
#     return result 