#open file for reading
txt_file = open("AI.txt", 'r')

#create an empty dictionary
word_dict = {}

#loop through the file
for l in txt_file:
    #remove leading spaces & newline
    l = l.strip() 

    #convert to lower case
    l = l.lower()

    #split line to words
    words = l.split(" ")

    #iterate over each word
    for word in words:
        #check if word is in dict
        if word in word_dict:
            #increment count by 1
            word_dict[word] += 1
        else:
            word_dict[word]= 1

#print word frequency
for key in list(word_dict.keys()):
    print(key, ":", word_dict[key])