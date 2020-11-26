# ZIPPING AND UNZIPPING FILES  

from zipfile import *
f = ZipFile('test.zip', 'w', ZIP_DEFLATED) #Create zip file

#Add some files which are available in current directory
#These files are zipped
x = 'file1.txt', ascii
f.write('Corona_counter.exe')
f.write('Bird.png')
f.write('mean.dat')

#Close the zip file
print('test.zip file created.....')
f.close()

#Unzipping
z = ZipFile('test.zip', 'r') #Open the zip file to read
print(z.extractall()) #Extract all the file names which are in the zip file