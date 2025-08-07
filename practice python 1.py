name = "John"
greeting = 'Hello!'

multi_line = '''This is a
multi-line string.'''

word = "Python"
print(word[0])  #Output: 'P'
print(word[2])  #Output: 't'

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name #Output: 'John Doe'
print(full_name)

exclamation = "Wow!" * 3 #Output: 'Wow! Wow! Wow!'
print(exclamation)

name = "Python"
print(len(name)) #Output: 6

language = "Python"
print(language[0:3]) #output: 'Pyt'
print(language[3:]) #output: "hon"
print(language[-1]) #output: "n" (negative indexing)

message = "Hello, World!"
print(message.upper()) #output: 'HELLO, WORLD!'
print(message.lower()) #output: 'hello, world!'

text = " Python "
print(text.strip()) #output: 'Python'

greet = "Hello, World!"
print(greet.replace("World", "Python")) #output: 'Hello, Python!'
print(greet.split()) #output: ['Hello,', 'World!']

words = ['Python', 'is', 'fun']
sentence = " ".join(words) #output: 'Python is fun'

filename= "report.pdf" 
print(filename.endswith('.pdf')) #output: True