import cv2
import pandas as pd
import argparse 

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True, help="Image Path")
args=vars(ap.parse_args())
img_path=args["image"]


img=cv2.imread(img_path)
height, width, _ = img.shape

# print("Height:", height)
# print("Width:", width)


max_distance=height * width

print("Press Esc to exit Program")

#declaring the global variables
clicked=False
r = g = b = xpos = ypos = 0

#reading csv file with pandas and giving names to each column

index= ["color","color_name","hex", "R", "G", "B"]
csv =pd.read_csv("colors.csv", names=index,header=None)





