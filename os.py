import os

data= os.path.dirname(__file__)  
file_path= os.path.join(data,'hi.txt')  

with open(file_path,'r',encoding= 'utf-8') as f:  
    content= f.read()

print(content)
