from bs4 import BeautifulSoup
import random
import requests

final_poem = []
q = 0
file_number = 0
print ("Hello \n World")


def scan_poem(poem):
    poem_length = len(poem)
    random_number = random.randint(1,poem_length)
    z = 0
    print (poem_number)



    for x in poem: 
        y = x.text.strip()
        z = z + 1
        if z == random_number & len(y) > 15:
            scan_poem(poem)


        else:
            if z == random_number:
                return y

while (file_number<20):
    custom_poem_length = random.randint(5,15)
    q = 0
    while (q<int(custom_poem_length)):
        print (custom_poem_length)
        print (q)
        baseurl = 'https://www.poetryfoundation.org/poems/'

        poem_number = random.randint(45000,49000)


        complete_url = baseurl + str(poem_number)

        page = requests.get(complete_url)

        soup = BeautifulSoup(page.content, 'html.parser')

        poem = soup.find_all('div', {"style" : "text-indent: -1em; padding-left: 1em;"})
        if (len(poem) != 0):
            final_poem.append(scan_poem(poem))
            print (final_poem)
            q = q+1
        else:
            print ("Crap")

    file_name = "poem" + str(file_number) + ".txt"
    f = open(file_name, "w")
    for line in final_poem:
        try:
            f.write(line)
            f.write("\n")
        except:
            f.write("")
    
    f.close()
    file_number = file_number + 1
    final_poem = []

    
    
        



    
