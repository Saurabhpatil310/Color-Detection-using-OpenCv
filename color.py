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

#function to calculate min distance from all colors and get most matching color

def getColorName(R,G,B):
    minimun = max_distance
    for i in range (len(csv)):
        d=(
            abs(R - int(csv.loc[i,"R"]))
            +abs(G - int(csv.loc[i,"G"]))
            +abs(B - int(csv.loc[i,"B"]))
        )
        if d <= minimun:
            minimun=d
            cname =csv.loc[i,"color_name"]
    return cname
    
#function to get x,y coordinates of mouse click

def draw_function(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global b,g,r,xpos,ypos,clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
#diver code

cv2.namedWindow("Photo") 
cv2.setMouseCallback("Photo", draw_function)

while True:
    cv2.imshow("Photo", img)
    if clicked:
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)
        colorName = getColorName(r, g, b) + " R=" + str(r) + " G=" + str(g) + " B=" + str(b)
        cv2.putText(img, colorName, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        if r + g + b >= 600:
            cv2.putText(img, colorName, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        clicked = False

    # Exit Program if esc key is pressed
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()






