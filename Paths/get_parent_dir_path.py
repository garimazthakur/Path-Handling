import os
from posixpath import dirname
# Path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Files")
# Path = os.path.dirname
P = "get_parent_dir_path.py"
Path = __file__  #automatically takes the absolute path of the file in which the code is running
Path1 =os.path.abspath(__file__)
Path2 = os.path.abspath(P)  #gives us the absolute path of P #gives us the parent folder
Path3 = os.path.abspath("Path/get_parent_dir_path.py")
Path4 = os.path.dirname(__file__)  #will give dirname bec __file__ already took the abs path of the current file
Path5 = os.path.dirname(os.path.abspath(P)) #you will get the dir name now, as we gave the asoulte path this time
Path6 =  os.path.dirname(os.path.dirname(os.path.abspath(P)))

Path7 = os.path.dirname(os.path.dirname(__file__))
Path8 = os.path.dirname(os.path.abspath(__file__)) #if you give abs path, it will still give the dirname
Path9 =  os.path.abspath(os.path.dirname(__file__))

Path10=os.path.join(os.path.dirname(os.path.abspath(__file__)), "Files")  #to get the 
Path11 = os.path.dirname("Paths") ##will not give any output because we have not given absolute path to it 
Path12= os.path.dirname(os.path.abspath("Paths"))  #Now we will get the dirname of "FileHandeling "folder

Path13 =  os.path.abspath(os.path.dirname(P))
Path14 = os.path.dirname(P)   #you will not get any output, bec you have to give path to get the dir name

print("this is path", Path)
print("this is Path1", Path1)
print("this is Path2", Path2)
print("this is Path3", Path3)
print("this is Path 4", Path4)
print("this is Path 5", Path5)
print("this is Path6", Path6)

print("this is Path7", Path7)
print("this is Path8", Path8)
print("this is Path9", Path9)

print("this is Path10", Path10)
print("this is Path11", Path11)
print("this is Path12", Path12)
print("this is Path13", Path13)
print("this is Path14", Path14)


#  output: 
# this is path c:\Users\garim\Desktop\gz7.ai\Path-Handling\Paths\get_parent_dir_path.py
# this is Path1 c:\Users\garim\Desktop\gz7.ai\Path-Handling\Paths\get_parent_dir_path.py
# this is Path2 C:\Users\garim\Desktop\gz7.ai\Path-Handling\get_parent_dir_path.py
# this is Path3 C:\Users\garim\Desktop\gz7.ai\Path-Handling\Path\get_parent_dir_path.py
# this is Path 4 c:\Users\garim\Desktop\gz7.ai\Path-Handling\Paths
# this is Path 5 C:\Users\garim\Desktop\gz7.ai\Path-Handling
# this is Path6 C:\Users\garim\Desktop\gz7.ai
# this is Path7 c:\Users\garim\Desktop\gz7.ai\Path-Handling
# this is Path8 c:\Users\garim\Desktop\gz7.ai\Path-Handling\Paths
# this is Path9 c:\Users\garim\Desktop\gz7.ai\Path-Handling\Paths
# this is Path10 c:\Users\garim\Desktop\gz7.ai\Path-Handling\Paths\Files
# this is Path11
# this is Path12 C:\Users\garim\Desktop\gz7.ai\Path-Handling
# this is Path13 C:\Users\garim\Desktop\gz7.ai\Path-Handling
# this is Path14

   

    