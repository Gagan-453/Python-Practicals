# WORKING WITH DIRECTORIES

#The os module represents operating system dependant functionality
# A program to know currently working directory
import os
current_dir = os.getcwd() #Get current working directory
print('Current Working directory: ', current_dir)

#A program to create a sub directory and then sub-sub directory in the current directory
import os
os.mkdir('mysub') #Create a sub directory by the name mysub
os.mkdir('mysub\mysub2') #Create a sub-sub directory by the name sub2
# mkdir() method can't create a sub-directory unless the parent directory exists
# That is where makedirs() function can be used

#Using makedirs() function
import os
os.makedirs('newsub/newsub2') #This creates a newsub directory if it does not exist, then it will create newsub2 inside it

#A program to change to another directory
import os
goto = os.chdir('newsub/newsub2')

#A program to remove a sub directory that is inside another directory
import os
os.rmdir('newsub/newsub2')

#A program to remove a group of ddirectories in the path
import os
os.removedirs('newsub/newsub2/newsub3') #Remove all three directories where mysub contains mysub2 and that again contains mysub3

#A program to rename a directory
import os
os.rename('mysub', 'Gagan') #Rename 'mysub' as 'Gagan'

#A program to display all the contents of the current directory
import os
for dirpath, dirnames, filenames in os.walk('.'):
    print('Current path: ', dirpath)
    print('Directories: ', dirnames)
    print('Files: ', filenames)
    print()