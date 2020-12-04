import re

pattern = re.compile(r"")
myString = input("Enter a string")
pattern = re.compile(r"[0-9]+")
result = pattern.sub("_",myString)
print(result)