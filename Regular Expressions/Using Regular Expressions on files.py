#USING REGULAR EXPRESSIONS ON FILES

##Write text into the file
#f = open('mails.txt', 'w')
#f.write('This project is assigned to Mr.Gagan Adithya Reddy at gaganreddy2705@gmail.com, and in case of any queries, you can contact Mr.Jagdish Babu at ejbsiro@gmail.com, or Mr.Anoop at anoop@project.org who would be acting as assistant project coordinators')
#f.close()

#Program to create a regular expression to retrieve all mails from the file
import re
f = open('mails.txt', 'r') #Open the text file
for line in f:
    res = re.findall(r'\S+@\S+', line) # '\S' represents non-space character, find words which has non-whitespace character before '@' and after that also
if len(res)>0:
    print(res)
f.close() #Close the file

#Program to retrieve data from a file using regular expressions and then write that data into a file
import re
f1 = open('salaries.txt', 'r')
f2 = open('newfile.txt', 'w')
for line in f1:
    res1 = re.search(r'\d{4}', line)
    res2 = re.search(r'\d{4,}.\d{2}', line)
    print(res1.group(), res2.group())
    f2.write(res1.group()+"\t")
    f2.write(res2.group()+"\n")
f1.close()
f2.close()
    