import cv2
import numpy as np
import glob
import os

dic = "D:\\python-workspace\\my_yolo\\ultralytics\\final_mask_1\\"  #待合并图片文件夹  your small images directory



'''

将多个小图合并成大图   combine small picture to a big one

fileNum  合并数量， numbers of small images
row      行数
col      列数
'''

def combineImage(fileNum,row,col):

    x = 0
    y = 0

    big_picture = np.full((1024 * row, 1024 * col, 3), 255, dtype=np.uint8)  #1024表示图片尺寸，按照自己的设置，我这边图片（小）尺寸为1024*1024 (1024 is the size of the your small picture)
    #big_picture = np.full((25182, 23315, 3), 255, dtype=np.uint8)

    for epoch in range(fileNum):
        pic = cv2.imread(dic+str(epoch+1)+".png")
        if((epoch)%col == 0):
            x = 1024
            y = y + pic.shape[0]
        else:
            x = x + pic.shape[1]
        big_picture[(y-pic.shape[0]):y,(x-pic.shape[1]):x,:] = pic
    cv2.imwrite("big_result.png",cv2.cvtColor(big_picture,cv2.COLOR_BGR2RGB))

if __name__ == '__main__':

    #执行函数，生成大图   excute function,get a big picture
    combineImage(24*22,24,22)
