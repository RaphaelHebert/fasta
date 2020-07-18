import regex as re

#prompt the user for filename
filename = input("Enter the name of the file to analize:\n")

#stock the content of the file
with open(filename, 'r') as f:
    content = f.read()

#make it list of lines
content = content.splitlines()


Identifiant = re.search("^>.*$/s", content)
print(f'Idenfiant is : {Identifiant}', content)

for index, ligne in enumerate(content):
    print(f"ligne{index} : {ligne}")

