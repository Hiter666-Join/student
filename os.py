import os

data= os.path.dirname(__file__)  #os.path.dirname打开当前目录文件夹
file_path= os.path.join(data,'hi.txt')  #os.path.join加上上面提取的目录用逗号拼接目录

with open(file_path,'r',encoding= 'utf-8') as f:  #open打开
    content= f.read()

print(content)