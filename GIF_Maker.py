import os, sys
from PIL import Image, ImageOps
qual, dur, name, path, images=100, 200, 'final_GIF.gif', './', []
for arg in sys.argv[1:] :
    if(arg.startswith('-h')) :
        print("GIF_Maker.py -q[Quality (float)%] -d[Duration] -n[Name]\nExamples :\n\tGIF_Maker.py -q33.33\n\tGIF_Maker.py -d300 -nHurrah.gif\n")
        print("Use:\n\tPut all the images in a folder. Put the script in the same folder.")
        sys.exit("Warning : Do NOT rename the script")
    if(arg.startswith('-q')) :
        qual=float(arg[2:].strip())
    if(arg.startswith('-n')) :
        name=arg[2:].strip()
    if(arg.startswith('-d')) :
        dur=int(arg[2:].strip())
    # if(arg.startswith('-f')) :
    #     path=arg[2:].strip()
    
imageNames = os.listdir(path)
for imageName in imageNames :
    if(imageName !='GIF_Maker.py' and  not imageName.endswith('.gif')):
        image =ImageOps.exif_transpose(Image.open(path+imageName))
        images.append(image.resize((int(image.size[0]*qual/100),int(image.size[1]*qual/100))))
images[0].save(name, save_all=True, append_images=images[1:],duration=dur,loop=0)