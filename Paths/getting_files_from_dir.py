import os


file = os.path.join("Paths", "Files")
path1 = os.path.abspath(file)
get_files = os.listdir(path1)  #to get the list of all  docs present in a folder

print(file) # Paths\Files
print(path1) # C:\Users\garim\Desktop\gz7.ai\Path-Handling\Paths\Files
print(get_files) #['words1.txt', 'words2.txt', 'words3.txt']




#Get file names using os.walk
for path, dirnames, filenames in os.walk(path1) #path returns the path of the folder, dirnames returns the names of the folder present in the path, filenames returns the list of all the files present in the path
    print(f'{repr(path)} \n {repr(dirnames)} \n {repr(filenames)}')
   
    # 'C:\\Users\\garim\\Desktop\\gz7.ai\\Path-Handling\\Paths\\Files'
    #[]
    #['words1.txt', 'words2.txt', 'words3.txt']
    for name in filenames:    
        print(name)
        # words1.txt
        # words2.txt
        # words3.txt  






# """
# output:



# ['words1.txt', 'words2.txt', 'words3.txt']

# """

