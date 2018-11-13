import os, webbrowser

filePath = input("What is the path to the .txt? ")

while not os.path.isfile(filePath):
    print("Incorrect file name. Please try again. ")

with open(filePath, 'r') as X:
    fileText = X.read().splitlines()

print(fileText)

for url in fileText:
    webbrowser.open(url)