# Zoom-file-scripts
## files_organizer.py
Parses the datetime from file names then organizes them into folders based on the date
Example:
```
% ls
GMT20240810-145510_Recording.m4a
GMT20240810-145510_Recording_640x360.mp4
GMT20231108-122511_Recording_640x360.mp4

% python3 files_organizer.py

% ls
08_10_2024/
11_08_2023/
```

## Delete Text Documents
Walks down the directory tree, deleting all text files

### Purpose
These scripts were created to help a family member keep the zoom recording files they downloaded more organized by automating the process of sorting the files into folders by the recording date given in the file names.
Additionally, another small script was made to delete all the text files which were not needed.

