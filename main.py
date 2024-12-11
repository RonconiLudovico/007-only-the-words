#here we define a function in which the result of the following function is copied onder another variable
def main(inpt):
    arr = de_punct(inpt).copy()
    #here the final list is formatted and printed
    return ''.join(arr)

def de_punct(inpt):
    #we create an empty list
    phrase = []
    #we then create a list containing all the punctuation marks that we want to remove
    punctuation = [".", ",", "?", "!", ";", ":", "-", "'"]
    #initiating the loop for every character in the phrase
    for i in inpt:
        #we state the condition for which if any character is not in the punctuation list the program should add it to the new list
        if i not in punctuation:
            phrase.append(i)
    #here we return the newly created list
    return phrase


#first we ask for an user input, passing it afterward in the main function
if __name__ == '__main__':
    phrase = input('write a sentence here: ')
    print(main(phrase))
