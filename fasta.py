#import re
import os
import regex as re

accessionnumber = '[A-Z]{,6}[0-9]{,8}\.[0-9]'
ginumber = '\d*'
locus = '.*\n'
databases = [('Genbank', f'^\>gi\|{ginumber}\|gb\|{accessionnumber}\| {locus}')]
extensions = ['.txt','.fasta','.fa']
filename = ''
content = ''
#try




#get the file and check the extension
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
  

#Look for seuqence id:
print(f"content is: \n {content}")

for dbname, regex0 in databases:
    print(dbname, regex0)
    found = re.findall(regex0, content)
    if found:
        print(found)
        print(f"DATABASE:       {dbname}")
        break

reg1 = re.findall(">[a-b]", content)
print(reg1)
Identifiant = reg1.match(content)
print(f'Idenfiant is : {Identifiant}')

#for index, ligne in enumerate(content):
    #print(f"ligne{index} : {ligne}")

