import os, argparse
from PIL import Image, ImageOps
parser = argparse.ArgumentParser(
                    prog='GIF Maker',
                    description='To make a gif file with images',
                    epilog='Use:\n\tPut all the images in a folder. Put the script in the same folder.\nWarning : Do NOT rename the script')
parser.add_argument('-o', '--output_file', help='Name of the final GIF file',default='final_GIF.gif')
parser.add_argument('-d', '--duration', help='Total runtime of the final output',default=200)
parser.add_argument('-q', '--quality', help='The quality of final output (0-100)',default=100)
args = parser.parse_args()
qual, dur, name ,path, images= int(args.quality) , int(args.duration), args.output_file, './', []
imageNames = os.listdir(path)
for imageName in imageNames :
    if(imageName !='GIF_Maker.py' and  not imageName.endswith('.gif')):
        image =ImageOps.exif_transpose(Image.open(path+imageName))
        images.append(image.resize((int(image.size[0]*qual/100),int(image.size[1]*qual/100))))
images[0].save(name, save_all=True, append_images=images[1:],duration=dur,loop=0)
