#import re
import pandas as pd
import os
import regex as re
import numpy as np
import matplotlib.pyplot as plt

accessionnumber = '[A-Z]{,6}[0-9]{,8}\.[0-9]'
ginumber = '[0-9]+'
locus = '.*\n'
databases = [('Genbank', f'^\>gi\|{ginumber}\|gb\|{accessionnumber}\| {locus}')]
extensions = ['.txt','.fasta','.fa']
filename = ''
content = ''

#codons
initiation = "ATG"
stop = "TAA|TAG|TGA"





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
    else:
        first = '>.*\n'
        firstline = re.findall(first, content)
        print(firstline)
        content = content.replace(firstline[0],'',1)
        

######################Look at the sequence #######################
#char by char        
pattern = re.compile('.')
matches = pattern.finditer(content)

mylist1 = []
for match in matches:
    #print (match.group())
    mylist1.append({ 'Position': match.end(), match.group(): 1})
    
mydf = pd.DataFrame(mylist1)

mydf = mydf.fillna(0)
mydf = mydf.set_index(mydf['Position'])
#print(mydf)
listA = mydf['A'].tolist()
print(listA)
plt.hist(x = listA, bins = 160)
plt.show()

#NUMBER OF EACH BASE
for col, row in mydf.iteritems():
    if col == "Position":
        print(f'Number of {col} :   {max(row)}')
    else:
        print(f'Number of {col} :           {sum(row)}')

#GC CONTENT
print(f"GC content :         {(sum(mydf['G']) + sum(mydf['C']))/max(mydf['Position'])}")

#FIND THE START AND STOP CODONS
start = re.compile(initiation)
end = re.compile(stop)

start = start.finditer(content)
stop0  = end.finditer(content)
mylist2 = []

for (startcodon, stopcodon) in zip(start, stop0):
    mylist2.append({'Position': startcodon.start(), 'Start (ATG)': startcodon.group()})
    mylist2.append({'Position': stopcodon.start(), 'Stop (TAA, TAG,TGA)': stopcodon.group()})

features = pd.DataFrame(mylist2)
print(features.sort_values('Position'))
