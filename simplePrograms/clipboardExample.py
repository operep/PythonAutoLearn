#! python2
#Example how to work with clipboard

import pyperclip

pyperclip.copy('Hello World!')
#this was just for allow user to copy something into clipboard 
raw_input("Enter something: ")

print(pyperclip.paste())
