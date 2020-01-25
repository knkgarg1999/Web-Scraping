import requests
from bs4 import BeautifulSoup
import os

print("Type your Author's Name")
s = input()
s = s.split()
n1 = s[0]
n2 = s[1]

file = open('quotes.txt','w')
file.write('Some of the famous quotes of' + ' ' + n1 + ' ' + n2 + ' ' + 'are:\n\n')

url = "https://www.goodreads.com/search?q=" + n1 + n2 + "&search%5Bsource%5D=goodreads&search_type=quotes&tab=quotes"    
r = requests.get(url)

soup = BeautifulSoup(r.content,'html5lib')
row = soup.findAll('div', attrs = {'class':'quoteText'})
for div in row:
    text = div.text
    text = text.replace('\n','')
    text = text.replace('  ','')
    split = text.split('"')
    split = text.split('"')
    quote = split[1]
    author = split[2]
    author = author.replace('—','')
    author = author.split('(')
    author = author[0]
    
    if os.path.exists('quotes.txt'):
        mode = 'a'
    else:
        mode = 'w'
        
    file = open('quotes.txt',mode)
    file.write(str(quote)+'\n')
    
file.close()

print("\nAll the quotes are saved in the file : quotes.txt")
