#strings
text = "This is a string"
#in method
#in is used when a string is inside other string
print('string' in text)
print('no string' in text)

#size of the string
size = len(text)

#string methods
print(text.upper()) #upper case
print(text.lower()) #lower case
print(text.count('a')) #count
print(text.swapcase()) #reverse case
print(text.startswith('This')) #return true or false if the string start with it
print(text.endswith('This')) #return true or false if the string ends with it
print(text.replace('String', 'Recharged string')) #replace the text
print(text.capitalize()) #change the first letter to upper case
print(text.title()) #change the first letter of every word to upper case
print(text.isdigit()) #return if the string is a digit

#index
print(text[0]) #print the caracter with position 0
print(text[-1]) # print last character
print(text[text.size() - 1 ]) # print last character

#slicing
print(text[2:5]) #print from position x to y
print(text[:10]) #print since beginin to position 0
print(text[6:]) #print since postition 6 to end
print(text[::2]) #print the number of jumps
print(text[::-1]) #print the revere string
