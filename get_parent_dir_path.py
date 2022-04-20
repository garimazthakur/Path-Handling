import os
from posixpath import dirname

P = "get_parent_dir_path.py"
Path = __file__  #automatically takes the absolute path of the file in which the code is running
Path1 =os.path.abspath(__file__)
Path2 = os.path.abspath(P)  #gives us the absolute path of P #gives us the parent folder
Path3 = os.path.dirname(__file__)  #will give dirname bec __file__ already took the abs path of the current file
Path4 = os.path.dirname(os.path.abspath(P)) #you will get the dir name now, as we gave the asoulte path this time
Path5 =  os.path.dirname(os.path.dirname(os.path.abspath(P)))

Path6 = os.path.dirname(os.path.dirname(__file__))
Path7 = os.path.dirname(os.path.abspath(__file__))  #if you give abs path, it will still give the dirname
Path8 =os.path.join(os.path.dirname(os.path.abspath(__file__)), "Files")  #to get the 
Path9 = os.path.dirname("FileHandeling") ##will not give any output because we have not given absolute path to it 
Path10= os.path.dirname(os.path.abspath("FileHandeling"))  #Now we will get the dirname of "FileHandeling "folder


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

"""

 output:  
   
"""

    