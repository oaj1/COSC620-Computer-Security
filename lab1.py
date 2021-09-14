#from collections import Counter
#from nltk.util import ngrams

from operator import itemgetter

file = open("body.txt") #this will be the file holding the articles

#punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''  #These punctuations will be ignored

text = file.read()#read the file
text = text.lower()#make each word lower case
#text = text.replace("\r\n"," ").replace("  "," ")#Talk with professor about new line issues
text = text.replace("\r\n"," ").replace("\n"," ").replace("  "," ")
"""
noPunct = ""
for char in text:
    if char not in punctuations:---------------------------->Didn't end up needing this code
        noPunct = noPunct + char
text = noPunct
"""


    
#print("orignal file: ")#show professor original list
print(text) #check to see if it went through
#file was read successfully, create some space between lists, utilized print() X 2


content = text #content is variable used for creating the list
contentList = content.split(" ")#split each new word on a blank space
#print("List of words: ")
#print(contentList)#successfully created the list of words, now I need to create a list of bigrams,

#print("All Bigrams: ")
#bigrams = [b for l in contentList for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]
bigrams = []
for i in range(len(contentList)-1):
    temp = (contentList[i],contentList[i+1]) #Manually append to bigrams list the various bigrams
    bigrams.append(temp)
#print(bigrams)


frequency = {}#dictionary, and is utlized to count the number of times bigram occurs
for item in bigrams:
   # checking the element in dictionary

    if item in frequency:
      # incrementing the counr

        frequency[item] += 1

    else:
      # initializing the count

        frequency[item] = 1 

#print("Bigram's frequencies")
#print(frequency)


#print("Descending order bigram")
frequency = sorted(frequency.items(),key = lambda x:x[1],reverse = True)
#print(frequency)

print()
print("Top 20 descending order bigram")
res = dict(sorted(frequency, key = itemgetter(1), reverse = True)[:20])
print(res)
