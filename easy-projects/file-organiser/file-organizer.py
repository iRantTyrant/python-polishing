#This is a simple file organiser script that organises files in a specified directory into subdirectories based on their file types. Made by iRant

#Importing necessary modules
import os; #For interacting with the operating system
import shutil; #For high-level file operations like copying and moving files
import pathlib; #For object-oriented filesystem paths 

#File class to store file types and their corresponding extensions
class File:
    def __init__(self, file_type, extensions,file_path,file_name):
        self.file_type = file_type; #File type (e.g., Images, Documents, etc.)
        self.extensions = extensions; #Extention corresponding to the file type
        self.file_path = file_path; #Path of the file
        self.file_name = file_name; #Name of the file

#Dicttionary to store file types and their corresponding extensions
file_types = {
    #Documents
    "txt": "Documents",
    "pdf": "Documents",
    "doc": "Documents",
    "docx": "Documents",
    "xls": "Documents",
    "xlsx": "Documents",
    "ppt": "Documents",
    "pptx": "Documents",
    "odt": "Documents",
    "rtf": "Documents",
    "tex": "Documents",
    "wpd": "Documents",
    "md": "Documents",
    "csv": "Documents",
    #Images
    "jpg": "Images",
    "jpeg": "Images",
    "png": "Images",
    "gif": "Images",
    "bmp": "Images",
    "tiff": "Images",
    "svg": "Images",
    "heic": "Images",
    "webp": "Images",
    "raw": "Images",
    #Videos
    "mp4": "Videos",
    "mkv": "Videos",
    "mov": "Videos",
    "avi": "Videos",
    "flv": "Videos",
    "wmv": "Videos",
    "webm": "Videos",
    "vob": "Videos",
    "ogv": "Videos",
    "3gp": "Videos",
    "mpg": "Videos",
    #Audio
    "mp3": "Audio",
    "wav": "Audio",
    "aac": "Audio",
    "flac": "Audio",
    "ogg": "Audio",
    "wma": "Audio",
    "m4a": "Audio",
    "aiff": "Audio",
    "alac": "Audio",
    "amr": "Audio",
    #Archives
    "zip": "Archives",
    "rar": "Archives",
    "7z": "Archives",
    "tar": "Archives",
    "gz": "Archives",
    #Executables
    "exe": "Executables",
    "msi": "Executables",
    "bat": "Executables",
    "sh": "Executables",
    "bin": "Executables",
    "cmd": "Executables",
    "app": "Executables",
    #Code files
    "py": "Code",
    "js": "Code",
    "html": "Code",
    "css": "Code",
    "java": "Code",
    "c": "Code",
    "cpp": "Code",
    "cs": "Code",
    "rb": "Code",
    "php": "Code",
    "go": "Code",
    "rs": "Code",
    "swift": "Code",
    "kt": "Code",
    "ts": "Code",
    "json": "Code",
    "xml": "Code",
    "yml": "Code",
    "yaml": "Code"
}

valid_path_flag = True ; #Flag to check if the path is valid it loops until a valid path is given

#Taking input from user it loops until a valid path is given
while valid_path_flag == True:
    print("Enter the path of the directory you want to organise: \n");
    path = input("Path :"); #Taking input from user
    if os.path.exists(path): #Checking if the path exists
        valid_path_flag = False; #If the path exists, set the flag to False to exit the loop
    else:
        print("\nInvalid path. Please try again.\n"); #If the path doesn't exist, ask for input again

#Scanning the directory and it's subdirectories for files
print("\nScanning the directory and it's subdirectories for files...\n");
files_dict = {}; #Dictionary to store file types and their corresponding files (key:path value:file) 
for (root, dirs, files) in os.walk(path):
    for f in files:
        files_dict[os.path.join(root, f)] = f; #Adding the file path and file name to the dictionary
print("Scan complete.\n");

#Printing the contents of the directory to be organised
print("Contents of the directory to be organised: \n");
print(files_dict); #Printing the dictionary

#Analysing the files and creating objects of the File class
print("\nAnalysing the files...\n");
#A list to store objects of the File class
files_list = [];

#Looping through the dictionary and creating objects of the File class
for key in files_dict:
    file_name = files_dict[key]; #Getting the file name
    extensions = pathlib.Path(file_name).suffix; #Getting the file extension
    extensions = extensions.lower(); #Converting the extension to lowercase for uniform
    extensions = extensions.replace(".",""); #Removing the dot from the extension
    file_type = file_types.get(extensions, "Other"); #Getting the file type from the dictionary defaulting to "Other" if the extension is not found
    file_obj = File(file_type, extensions,key,file_name); #Creating an object of the File class
    files_list.append(file_obj); #Adding the object to the list
print("Analysis complete.\n");

#Organising the files
print("Organising the files...\n");
#Creating subdirectories for each file type if they don't exist
for file_type in set(file_types.values()): #Using set to avoid duplicate file types
    dir_path = os.path.join(path, file_type); #Creating the path for the subdirectory
    if not os.path.exists(dir_path): #Checking if the subdirectory exists
        os.makedirs(dir_path); #If the subdirectory doesn't exist, create it
        print(f"Created directory: {dir_path}\n"); #Printing the path of the created subdirectory
#Creating a subdirectory for "Other" file type
other_dir_path = os.path.join(path, "Other"); #Creating the path for the "Other" subdirectory
if not os.path.exists(other_dir_path): #Checking if the "Other" subdirectory exists
    os.makedirs(other_dir_path); #If the "Other" subdirectory doesn't exist, create it
    print(f"Created directory: {other_dir_path}\n"); #Printing the path of the created "Other" subdirectory

#Moving the files to their corresponding subdirectories
for file_obj in files_list:
    file_type = file_obj.file_type; #Getting the file type from the object
    src_path = file_obj.file_path; #Getting the source path from the object
    file_name = file_obj.file_name; #Getting the file name from the object
    dest_path = os.path.join(path, file_type, file_name); #Creating the destination path
    try:
        shutil.move(src_path, dest_path); #Moving the file to the destination path
        print(f"Moved file: {file_name} to {dest_path}\n"); #Printing the path of the moved file
    except Exception as e:
        print(f"Error moving file: {file_name}. Error: {e}\n"); #Printing the error if any
print("Organising complete.\n");
print("All files have been organised successfully!\n");

#Remove empty directories
print("Removing empty directories...\n");
for (root, dirs, files) in os.walk(path, topdown=False): #Walking the directory tree from bottom to top
    for d in dirs:
        dir_path = os.path.join(root, d); #Creating the path for the subdirectory
        try:
            os.rmdir(dir_path); #Removing the empty subdirectory
            print(f"Removed empty directory: {dir_path}\n"); #Printing the path of the removed subdirectory
        except OSError as e:
            pass; #If the subdirectory is not empty, do nothing
