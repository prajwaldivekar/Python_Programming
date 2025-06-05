# String method is used to perform specific tasks to string

# 1. len() function = Length function is used to find the length of String
length = len("Prajwal")
print(length) #Output = 7

#2. Strings.endswith(" ") = the method is used whether the variable string is ends with string " " or not
name = "Prajwal"
endswith = name.endswith("wal")
print("name is ends with 'wal' or not :-",endswith)

# 3. String.count(""):- this is used to count perticular character
name_count = "Prajwal Shivaji Divekar"
count = name_count.count("a")
print(count)

# 4. string.capitalized():- this is used to convert first leter of string into capital
String = "prajwal"
capital = String.capitalize()
print(capital)

# 5. String.find(word) :- This is ued to fing word in the string
s = "I want to get placement in 3rd year in Diploma"
find = s.find("placement")
print(find)

#6. String.replace("old word","new word") :- this function is used to replace any word
word = "I am looser in collage"
replace = word.replace("looser","Topper")
print("old -->"+word)
print("New version -->"+replace)

