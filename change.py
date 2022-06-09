from PIL import Image
import os, sys
import cv2
import numpy as np

'''
Converts all images in a directory to '.npy' format.
Use np.save and np.load to save and load the images.
Use it for training your neural networks in ML/DL projects. 
'''

# Path to image directory
path = "dataset/test/"
dirs = os.listdir( path )
dirs.sort()

def load_dataset():
    # Append images to a list
    for item in dirs:
        if os.path.isfile(path+item):
            if not ".npy" in item:
                print(path+item)
                os.rename(path+item,path+os.path.splitext(item)[0]+"_input.png")
                #np.save(path+os.path.splitext(item)[0]+"_label.npy",im)

if __name__ == "__main__":
    
    load_dataset()
    #path = "dataset/train/"
    #dirs = os.listdir( path )
    #dirs.sort()
    #load_dataset()
    
    # Convert and save the list of images in '.npy' format
    #imgset=np.array(x_train)
    #np.save("imgds.npy",imgset)