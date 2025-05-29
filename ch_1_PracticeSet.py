#Q.1 write a program to print program twinkle twinkle little star..
print("""
 Twinkle, twinkle, little star,
 How I wonder what you are.
 Up above the world so high,
 Like a diamond in the sky.

 When the blazing sun is gone,
 When he nothing shines upon,
 Then you show your little light,
 Twinkle, twinkle, all the night.

 Then the traveller in the dark,
 Thanks you for your tiny spark,
 He could not see which way to go,
 If you did not twinkle so.

 In the dark blue sky you keep,
 And often through my curtains peep,
 For you never shut your eye,
 ‘Till the sun is in the sky.

 As your bright and tiny spark,
 Lights the traveller in the dark.
 Though I know not what you are,
 Twinkle, twinkle, little star.

 Twinkle, twinkle, little star.
 How I wonder what you are.
 Up above the world so high,
 Like a diamond in the sky.

 Twinkle, twinkle, little star.
 How I wonder what you are.
 How I wonder what you are.
 """)

# Q.2 Useing REPL print table of 5
# open command prompt And print table like this 5*1 5*2 and so on.....

# Q.3 Install an extrnal module and use it to perform an opration of your intrest
# In VS code trminal write "PIP install pyttsx3"
# And after

import pyttsx3
engine = pyttsx3.init()
engine.say("I am Prajwal")
engine.runAndWait()

# Q.4 Write a python program to print the content of a directory using os module.
# Search online for the function which does that

import os
directory_path = '/Web_Page_Desining'
content = os.listdir(directory_path)
for item in content:
    print(item)

# Q.5 Label the program written in the Q.4 with comments

import os

# specific directory which you want to list
directory_path = '/Web_Page_Desining'

# List all files and directory in specific path
content = os.listdir(directory_path)

# Print each file and directory name
for item in content:
     print(item)