import os
import os.path

month_dict = {
  '01':'Jan',
  '02':'Feb',
  '03':'Mar',
  '04':'Apr',
  '05':'May',
  '06':'Jun',
  '07':'Jul',
  '08':'Aug',
  '09':'Sep',
  '10':'Oct',
  '11':'Nov',
  '12':'Dec',
}

#contains the absolute path for the directory where all the zoom recording files are
directory = r''

#loop through all files and directories in the directory
for filename in os.listdir(directory):
    
    #assign absolute path for file or directory to a string
    f = os.path.join(directory, filename)
    
    #if the string is a path to a file
    if os.path.isfile(f):
        #parse date from filename 
        year = filename[3:7]
        month = filename[7:9]
        day = filename[9:11]

        #the desired name format for the folder the file will be placed in
        desired_folder = fr'{directory}\{month_dict[month]} {day}, {year}'

        #if desired folder already exists
        if os.path.isdir(desired_folder):
            #move the file to the folder
            os.rename(f, fr'{desired_folder}\{filename}')
            print('moved a file')
        else:
            #create a folder and move the file to the folder     
            os.mkdir(desired_folder)
            os.rename(f, fr'{desired_folder}\{filename}')
            print('created folder and moved a file')

#Filename Example: GMT20210727-200343_Recording
