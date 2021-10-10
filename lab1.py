#Take input file, make into list of bigrams, sort to top 20 in descending order

ffrom operator import itemgetter

file = open("body.txt") #this will be the file holding the articles



text = file.read()#read the file
text = text.lower()#make each word lower case
text = text.replace("\r\n"," ").replace("\n"," ").replace("  "," ")

content = text #content is variable used for creating the list
contentList = content.split(" ")#split each new word on a blank space



bigrams = []
for i in range(len(contentList)-1):
    temp = (contentList[i],contentList[i+1]) #Manually append to bigrams list the various bigrams
    bigrams.append(temp)



frequency = {}#dictionary, and is utlized to count the number of times bigram occurs
for item in bigrams:
   # checking the element in dictionary

    if item in frequency:
      # incrementing the counr

        frequency[item] += 1

    else:
      # initializing the count

        frequency[item] = 1 




frequency = sorted(frequency.items(),key = lambda x:x[1],reverse = True)


print()
print("Top 20 descending order bigram")
res = dict(sorted(frequency, key = itemgetter(1), reverse = True)[:20])
print(res)
