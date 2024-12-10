import os
from PIL import Image
pwd=os.path.dirname(__file__)
list=os.listdir(os.path.join(pwd,"temp"))
rmv=[]
for i in list:
    file=os.path.join(pwd,"temp",i)
    tar=os.path.join(pwd,"temp2",i)
    image = Image.open(file)
    width,height=image.size
    if max(width,height)>1024:
        d=1000/max(width,height)
        x=int(width*d)
        y=int(height*d)
        os.system(f"ffmpeg -i {file} -s {x}x{y} {tar}")
        rmv.append(file)
for i in rmv:
    os.system(f"del /q {i}")