#import re
import pandas as pd
import os
import regex as re

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

mydict1 = {}
for match in matches:
    print (match.end)
    if match.group not in mydict1.keys():
        mydict1[match.group] = ([],[])
    mydict1[match.group][0].append(1)
    mydict1[match.group][1].append(match.end)
    
mydict1 = pd.DataFrame(mydict1)
print(mydict1)
#stuck on git push again !!!






