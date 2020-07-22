#import re
import pandas as pd
import os
import regex as re
import numpy as np

accessionnumber = '[A-Z]{,6}[0-9]{,8}\.[0-9]'
ginumber = '[0-9]+'
locus = '.*\n'
databases = [('Genbank', f'^\>gi\|{ginumber}\|gb\|{accessionnumber}\| {locus}')]
extensions = ['.txt','.fasta','.fa']
filename = ''
content = ''





############get the file and check the extension###############
while True:
    #prompt the user for input
    filename = input("Enter the name of the file to analize:\n")
    #find the extension
    reg0 = re.findall('\.\w*', filename)

    if not reg0:
        print('No extension found!')
        continue

    if reg0[0] in extensions:
        try: 
            with open(filename, 'r') as f:
                content = f.read()
        except:
            print('Empty or not existing file!')
            continue
        break       
    else:
        print("Extension not allowed!")
  

############look for the sequence id and extract informations###############
for dbname, regex0 in databases:
    #print(dbname, regex0)
    found = re.findall(regex0, content)
    if found:
        print(found[0])
        print(f"DATABASE:               {dbname}")
        accessionnumber1 = re.findall(accessionnumber, found[0])
        print(f'ACCESSION NUMBER is:    {accessionnumber1[0]}')
        ginumber1 = re.findall(ginumber, found[0])
        print(f'GI NUMBER is:           {ginumber1[0]}')
        locus0 = re.findall(f"[^\|]+\n", found[0])
        print(f'LOCUS is:               {locus0[0]}')
        #delete the sequence id
        content = content.replace(found[0],'',1)
        break

#put every caracter in         
pattern = re.compile('.')
matches = pattern.finditer(content)

mylist1 = []
for match in matches:
    #print (match.group())
    mylist1.append({ 'Position': match.end(), match.group(): 1})
    
mydf = pd.DataFrame(mylist1)

mydf = mydf.replace(np.nan, 0)

for col, row in mydf.iteritems():
    print(f'Number of {col} : {sum(row)}')



