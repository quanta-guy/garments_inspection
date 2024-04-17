import cv2
import numpy as np


# define a video capture object 
url='http://192.168.103.200:4747/video'
vid = cv2.VideoCapture(url) 
#Model Image
image1 = cv2.imread('test.jpeg')
  
while(True): 
      
    # Capture the video frame 
    # by frame 
    ret, image2 = vid.read() 
    # Load the input images
    image1=cv2.resize(image1,(1280,720))
    image2=cv2.resize(image2,(1280,720))

    # Convert the images to grayscale
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    # Apply Canny edge detection to both images
    edges1 = cv2.Canny(gray1, 100, 200)
    edges2 = cv2.Canny(gray2, 100, 200)

    # Use bitwise AND to find overlapping edges
    overlap_edges = cv2.bitwise_and(edges1, edges2)

    # Display the original images and the overlapping edges
    cv2.imshow('Image 1', image1)
    cv2.imshow('Edges 1', edges1)
    cv2.imshow('Image 2', image2)
    cv2.imshow('Edges 2', edges2)
    cv2.imshow('Overlap Edges', overlap_edges)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
        
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 



