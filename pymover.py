import os

looping = True
files_tomove = [""]
cur_file = ""
directory = raw_input("Enter Directory you want to move files (leave blank if you want to use current directory)\n>")
break_loop = False

if directory is "":
    directory = os.getcwd()
    
files_arr = os.listdir(directory)
print files_arr[0]

files_search = raw_input("Enter file you wish to search for and move (leave blank if all)\n>")

if files_search is "":
    files_tomove = os.listdir(directory)
x = 0
for i in range(len(files_arr)):
    if files_search in files_arr[i]:
        files_tomove.append(files_arr)
        x = x + 1

print str(x) + " Files in search. Names: "
print files_tomove
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
            looping = True
    if break_loop is True:
        break
print "Done!"