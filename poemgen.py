from bs4 import BeautifulSoup
import random
import requests

final_poem = []
q = 0
file_number = 0
custom_poem_length = 5

def stripIndividualPoem(poem):
    poemLength = len(poem)
    numLinesToTake = random.randint(2, 3)
    lineCount = 0
    arrayOfLines = []
    for x in poem:
        # print ("line is " + x)
        if (lineCount == numLinesToTake):
            ##print("returning")
            ##print(arrayOfLines)
            return arrayOfLines
        else:
            arrayOfLines.append(x)
            lineCount += 1


while (q<int(custom_poem_length)):
    #print (custom_poem_length)
    #print (q)
    apiurl = 'https://poetrydb.org/random'
    response = requests.get(apiurl)
    poemResponse = response.json()
    poem = poemResponse[0]["lines"]
    if (len(poem) != 0):
        ##print(stripIndividualPoem(poem))
        final_poem.append(stripIndividualPoem(poem))
        ##print("final poem is currently")
        ##print (final_poem)
        q+=1 
    else:
        print ("Crap")

file_name = "poemName.txt"
f = open(file_name, "w")
print ("final poem is ")
print(final_poem)
for line in final_poem:
    try:
        ##f.write(line)
        for line_piece in line:
            print ("line piece is " + line_piece)
            f.write(line_piece)
            f.write("\n")
    except:
        f.write("fail")
f.close()

    
    
        



    
