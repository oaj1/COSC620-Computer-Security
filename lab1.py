#Take input file, make into list of bigrams, sort to top 20 in descending order

from operator import itemgetter

filePtr = open('body.txt', 'r')
text = "" #collect text one line at a time
while True:
        # Get next line from file
        line = filePtr.readline()
        # if line is empty
        # end of file is reached
        if not line:
            break
        text = text + line.lower().strip() # strip() is to strip the newline character
filePtr.close()

content = text #content is variable used for creating the list
contentList = content.split(" ")#split each new word on a blank space

bigrams = [] #bigrams will be used to place list of bigrams
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
print("Top 20 descending order bigram")
res = dict(sorted(frequency, key = itemgetter(1), reverse = True)[:20])
print(res)
