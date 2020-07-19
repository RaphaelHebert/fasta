#import re
import regex as re

extensions = ['.txt','.fasta','.fa']
#prompt the user for filename
#filename = input("Enter the name of the file to analize:\n")

##Chech the extension
filename = ''
#reg0 = reg0.match(filename)

#get the file and check the extension
while True:
    filename = input("Enter the name of the file to analize:\n")
    #reg0 = re.compile('\.\w*')
    reg0 = re.findall('\.\w*', filename)
    if not reg0:
        print('No extension found!')
        continue

    if len(reg0) > 1:
        print("Too many file extensions!")
        continue
    if reg0[0] in extensions: 
        break

    print("Extension not allowed!")
    

#stock the content of the file
with open(filename, 'r') as f:
    content = f.read()

#make it list of lines
content = content.splitlines()

reg1 = re.compile("^>.*$/s")
print(reg1)
Identifiant = reg1.match(content[0])
print(f'Idenfiant is : {Identifiant}', content)

for index, ligne in enumerate(content):
    print(f"ligne{index} : {ligne}")

