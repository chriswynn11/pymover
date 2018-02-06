import os
import getpass
import shutil

username = getpass.getuser()
print username

looping = True
files_tomove = []
cur_file = ""
directory = raw_input("Enter Directory you want to move files from (leave blank if you want to use pymover's directory) or press E to exit\n>")
break_loop = False
if directory.upper() == "E":
    quit()
if directory is "":
    directory = os.getcwd()
print ""
files_arr = os.listdir(directory)
if len(files_arr) < 1:
    print "No file in directory! Exiting pymover"
    quit()

files_search = raw_input("Enter file you wish to search for and move (leave blank if all)\n>")
str(files_search)

print ""
x = 0
for i in range(len(files_arr)):
    if files_search in files_arr[i]:
        files_tomove.append(files_arr[i])
        x = x + 1
    elif files_search is "":
        files_tomove = os.listdir(directory)
print str(x) + " Files in search. Names: "
print files_tomove
folder_tomove = raw_input("Enter directory to move to\n>")
str(folder_tomove)
print "Moving to folder " + folder_tomove
for i2 in range(len(files_tomove)):
    print ""
    looping = True
    while(looping is True):
        x = x + 1
        print "You found file " + files_tomove[i2]
        y_or_n = raw_input("Do you wish to move this file? [Y]es [N]o [M]ove all [E]xit\n>")
        if y_or_n.upper() == "Y" or y_or_n.upper() == "YES":
            print "Moving..."
            looping = False
            shutil.move(directory + '/' + files_tomove[i2],folder_tomove)
            #Move code goes here
        elif y_or_n.upper() == "N" or y_or_n.upper() == "NO":
            looping = False
            print "You did not move file " + files_tomove[i2]
        elif y_or_n.upper() == "M" or y_or_n.upper() == "MOVE ALL":
            print "You moved all files"
            looping = False
            break_loop = True
            #move all files code goes here
        elif y_or_n.upper() == "E" or y_or_n.upper() == "EXIT":
            looping = False
            exit()
        else:
            print "ERROR: enter proper input"
            print ""
            looping = True
    if break_loop == True:
        break
print "Done!"