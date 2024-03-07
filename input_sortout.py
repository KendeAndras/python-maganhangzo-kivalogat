def swap(x):
    vowels="aáeéiÍoóuúöőüű"
    vowels+=vowels.upper()

    swapped=""
    for i in x:
        swapped+='X' if i in vowels else i
#        if i in vowels:
#            swapped+='X'
#        else:
#            swapped+=i

    return swapped

def inputWord():
    word=input("adjal egy szot testver")
    print(swap(word))

inputWord()