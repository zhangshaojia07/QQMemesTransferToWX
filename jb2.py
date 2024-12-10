import os
from PIL import Image
pwd=os.path.dirname(__file__)
list=os.listdir(os.path.join(pwd,"qwq"))
for i in list:
    file=os.path.join(pwd,"qwq",i)
    image = Image.open(file)
    width,height=image.size
    tar=os.path.join(pwd,"qwq2",i)
    l=0
    r=1
    for j in range(10):
        mid=(l+r)/2
        x=int(width*mid)
        y=int(height*mid)
        os.system(f"ffmpeg -i {file} -s {x}x{y} -lavfi split[v],palettegen,[v]paletteuse {tar}")
        if os.stat(tar).st_size>=1000000:
            r=mid
        else:
            l=mid
        os.remove(tar)
    x=int(width*l)
    y=int(height*l)
    os.system(f"ffmpeg -i {file} -s {x}x{y} {tar}")