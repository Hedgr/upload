import io
import matplotlib.pyplot as plot
import matplotlib.image as img
import numpy
from tqdm import tqdm as prbar

# inspiration from acerola on YT

file = io.open("output.txt","w")
plot.axis("off")
plot.rcParams['figure.facecolor'] = 'none'
input_im = img.imread("C:\\Users\\hedgr\\Downloads\\person.png")

bmask = []
mask1 = []
mask2 = []

image = []
# 224x138

def display(img_array, out_file):
    out = io.open(str(out_file),"w")
    for i in range(len(img_array)):
        out.write(str(img_array[i])+"\n")

for i in prbar(range(len(input_im)),ncols=75,desc="main pass"):
    bmask.append([])
    for j in range(len(input_im[i])):
        bmask[i].append(round(((input_im[i][j][0] * 255) + (input_im[i][j][1] * 255) + (input_im[i][j][2] * 255)) / 3, 0))
display(bmask,"output4.txt")

#make input mask
for i in prbar(range(len(input_im)),ncols=75,desc="make mask 1"):
    mask1.append([])
    for j in range(len(input_im[i])):
        #print(brightness)
        brightness = bmask[i][j]
        if not ((brightness >= 100)&(brightness <= 190)):
            mask1[i].append([255,255,255])
        else:
            mask1[i].append([50,50,50])

for i in prbar(range(len(input_im)),ncols=75,desc="make mask 2"):
    mask2.append([])
    for j in range(len(input_im[i])):
        mask2[i].append([0])
    prev = 0
    count = 0
    startj = 0
    for j in range(len(input_im[i])):
        if mask1[i][j][0] == 255:
            if prev == 0:
                prev = 1
                count = 1
                startj = j
            else:
                count += 1
        else:
            if prev == 1:
                mask2[i][startj][0] = count
            else:
                mask2[i][j][0] = 0
            prev = 0

def custSort(lst):
    templist = []
    for i in range(len(lst)):
        templist.append([lst[i],i])
    for i in range(len(lst)):
        if i == 0:
            if templist[i] > templist[i+1]:
                tmp = templist[i+1]
                templist[i+1].pop()
                templist.insert(i+1)
                templist[i] = tmp
        else:
            if i != len(lst):
                if templist[i] > templist[i+1]:
                    tmp = templist[i + 1]
                    templist[i + 1].pop()
                    templist.insert(i + 1)
                    templist[i] = tmp




for x in prbar(range(len(input_im)), ncols=75, desc="sort pixels"):
    for y in range(len(input_im[x])):
        if mask2[x][y][0] > 0:
            pass






display(input_im,"very_compressed_mountain.txt")
display(mask1,"output2.txt")
plot.imshow(mask2)
plot.savefig("image2.png", transparent=True)
display(mask2,"output3.txt")
plot.imshow(mask1)
image = numpy.array(mask1)
plot.savefig("image.png", transparent=True)
plot.show()