sentence = input("Type a Sentence :")
print(sentence)
number=0
letter=0
for characther in sentence :
    if characther == " ":
        number=number+1
    else:
        letter=letter+1

print ("number of words are "+ str(number))
print ("numbers of characther are"+ str (letter))