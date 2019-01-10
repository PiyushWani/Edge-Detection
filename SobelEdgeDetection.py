from imageio import imsave
import numpy
import cv2

im = cv2.imread('task1.png',0)

operatory = [[1,2,1],
             [0,0,0],
             [-1,-2,-1]]

operatorx = [[1,0,-1],
             [2,0,-2],
             [1,0,-1]]
           
height= len(im)
width = len(im[0])
canvas = numpy.zeros((height+2, width+2))
print("im shape:"+str(im.shape))
print("Canvas Dim:"+str(canvas.shape))

for i in range(height):
    for j in range(width):
        canvas[i+1][j+1] = im[i][j]  

print("Padded Image Dim: "+str(canvas.shape))
imsave("paddedImage.jpg", canvas)

gx= numpy.zeros((height,width))
gy= numpy.zeros((height,width))

subimg = numpy.zeros([3,3,4])
for row in range(1, height-1):
    for col in range(1, width-1):
        subimg = canvas[row:row+3, col:col+3]
        values_x = numpy.zeros((3, 3))
        values_y = numpy.zeros((3, 3))
        
        
        for i in range(0, 3):
            for j in range(0, 3):
                values_x[i][j] = subimg[i][j] * operatorx[i][j]
                values_y[i][j] = subimg[i][j] * operatory[i][j]
        
        sumX = 0
        sumY = 0
        for i in range(3):
            for j in range(3):
                sumX = sumX + values_x[i][j]
                sumY = sumY + values_y[i][j]
        
        #values_x = numpy.multiply(subimg, operatorx)
        # values_y = numpy.multiply(subimg, operatory)      
        
        gx[row-1][col-1] = sumY#values_x.sum()
        gy[row-1][col-1] = sumX#values_y.sum()
        
mag = numpy.sqrt(gx ** 2 + gy ** 2)
maxMag = -9999
maxGx = -9999
maxGy = -9999
for i in range(0, height):
    for j in range(0, width):
        if(maxMag < mag[i][j]):
            maxMag = mag[i][j]
        if(maxGx < gx[i][j]):
            maxGx = gx[i][j]
        if(maxGy < gy[i][j]):
            maxGy = gy[i][j] 
            
mag *= 255.0 / maxMag
gx  *= 255.0 / maxGx
gy  *= 255.0 / maxGy
imsave('TC_EdgeDetectionSelf_x.png', gx) 
imsave('TC_EdgeDetectionSelf_y.png', gy)     
imsave('TC_EdgeDetectionSelf_mag.png', mag)