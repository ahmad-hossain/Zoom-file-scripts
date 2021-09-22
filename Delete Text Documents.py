import os

#contains directory that has all the date sorted folders 
d = r''
#loop through all files by traversing every directory in the tree
for subdir, dirs, files in os.walk(d):

	#loop through every file
    for file in files:

        #if the file is a text file
		if file.endswith('.txt'):

            #print the files to be deleted
            print(fr'{subdir}\{file}')

            #files are permanently removed with os.remove() method without being sent to recycle bin so code is commented out for safety
            #os.remove(fr'{subdir}\{file}')