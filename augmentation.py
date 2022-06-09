from numpy import ndim
import imageio
from scipy import ndimage
import os


path = r"dataset-c\test"
outPath = path
#outPath = r"dataset-c\train"

i = 0
for image_path in os.listdir(path):
  if not ".npy" in image_path:
    input_path = os.path.join(path, image_path)
    image_to_edit = imageio.imread(input_path)

    # rotacja zdjęcia o 90 stopni
    edited_image = ndimage.rotate(image_to_edit, 90)
    fullpath = os.path.join(outPath,"rotated90_" + image_path)
    print(fullpath)
    imageio.imwrite(fullpath, edited_image)

    edited_image = ndimage.rotate(image_to_edit, 180)
    fullpath = os.path.join(outPath,"rotated180_" + image_path)
    print(fullpath)
    imageio.imwrite(fullpath, edited_image)

    edited_image = ndimage.rotate(image_to_edit, 270)
    fullpath = os.path.join(outPath,"rotated270_" + image_path)
    print(fullpath)
    imageio.imwrite(fullpath, edited_image)

    edited_image = ndimage.gaussian_filter(image_to_edit, sigma=2)
    fullpath = os.path.join(outPath,"blur_" + image_path)
    print(fullpath)
    imageio.imwrite(fullpath, edited_image)
    # rozmycie zdjęcia względem parametru sigma
    # 
    #print(image_path)
    
    i=i+1