## WEEK 2 ----

# Regular expressions

import re

s = ("If I’m not in a hurry, then I should stay. " +
    "On the other hand, if I leave, then I can sleep.")

#print(s)
#print(re.findall(r'[Ii]f (.*), then', s))
#print(bool(0))

# Basic file processing


#print("a".encode("utf-8"))


#print(list("a".encode("utf-8"))  )            # Show as a list of integers


# reading a file
#f = open("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/exercises_instructions.txt", "r") # Let's open this notebook file, 
                              # which is essentially a text file.
                              # So you can open it in a texteditor as well.
        
#for i in range(10):            # And read the first five lines
    #line = f.readline()
    #print(f"Line {i}: {line}", end="")
#f.close()

s = ''
#print(s)
#print(type(s))
s = int('0'+s)
#print(type(s))


w = "Release Date: August 12, 2006 [EBook #19033]"
print(w)
a = re.split(r'\s', w)
print(a)
print(type(a), len(a))
for i in a:
    if not re.findall(r'[\w]$', i) or not re.findall(r'^[\w]', i):
        print(i.strip("""!"#$%&'()*,-./:;?@[]_"""))




