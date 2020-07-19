#import re
import os
import regex as re

extensions = ['.txt','.fasta','.fa']
filename = ''
content = ''

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

    
    


print("out of the loop")
#make it list of lines
content = content.splitlines()

reg1 = re.compile("^>.*$/s")
print(reg1)
Identifiant = reg1.match(content[0])
print(f'Idenfiant is : {Identifiant}', content)

for index, ligne in enumerate(content):
    print(f"ligne{index} : {ligne}")

