'''*** Invisible Cloak Harry Potter style made via Aafreen Khan & Smita Joshi*** '''


#Steps to Build Invisible Cloak OpenCV Project:

#Now we have everything ready. Below are the steps to create invisible cloak:

#1.Import necessary packages and Initialize the camera.
#2.Store a single frame before starting the infinite loop.
#3.Detect the color of the cloth and create a mask.
#4.Apply the mask on frames.
#5.Combine masked frames together.
#6.Removing unnecessary noise from masks.

#Step 1 – Import necessary packages and Initialize the camera:


# Import Libraries
import numpy as np
import cv2
import time

'''Explanation:

Using import, we imported the required libraries
To access the camera, we use the method cv2.VideoCapture(0) 
and set the capture object as cap.'''

#Step 2 – Store a single frame before starting the infinite loop:

cap = cv2.VideoCapture(0)
time.sleep(2)     
background = 0

'''Explanation:

-> cap.read() function captures frames from webcam
-> 2-second delay between two captures are for adjusting camera auto exposure
-> cap.isOpen() function checks if the camera is open or not and returns true
if the camera is open and false if the camera is not open.
-> While capturing the background make sure that you or your clothes 
don’t accidentally come into the frame.'''


#Step 3 – Detect the cloth:

'''In this invisible cloak opencv project, we are using Red cloth so we
 have to detect Red color. So how can we do this?

OpenCV reads the frame as BGR colorspace. To detect any color first we 
have to convert the frame to HSV colorspace.'''


for i in range(50):
    ret, background = cap.read()

while(cap.isOpened()): 
    ret, img = cap.read()

    if not ret:
        break
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # all this Comes in the while loop
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])  # values is for red colour Cloth
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    # Step 4 – Apply the mask:
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    # Combining the masks so that It can be viewd as in one frame
    mask1 = mask1 + mask2
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations=1)

    mask2 = cv2.bitwise_not(mask1)

    res1 = cv2.bitwise_and(background, background, mask=mask1)

    res2 = cv2.bitwise_and(img, img, mask=mask2)
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
    cv2.imshow('Invisible Cloak', final_output)
    k = cv2.waitKey(10)
    if k == 27:
        break

'''Why HSV?

HSV stands for HUE, SATURATION, and VALUE (or brightness).
 It is a cylindrical color space.

 HUE: The hues are modeled as an angular dimension which encodes color
 information.
SATURATION: Saturation encodes intensity of color.
VALUE: Value represents the brightness of the color.'''





'''Explanation:

* cv2.cvtColor() function converts colorspace.
* Lower bound and Upper bound are the boundaries of green color.
* cv2.inRange() function returns a segmented binary mask of the frame
 where the green color is present.'''
    


'''Here we can see in the frame wherever the Red color is detected
 the mask shows that as white. The rest of the region is black.'''




#Combining the masks so that It can be viewd as in one frame


''' Removing unnecessary noise from mask :'''




'''Explanation:

1.cv2.MORPH_CLOSE removes unnecessary black noise from the white 
region in the mask. And how much noise to remove that is defined by 
morphology.
2.cv2.MORPH_OPEN removes unnecessary white noise from the black
 region.
3.cv2.dilate increases white region in the image.'''




'''
We have successfully detected the cloak. We want to show our 
previously-stored background in the main frame where the cloak is 
present. First, we need to take the only white region from the
 background.'''




'''Explanation:

cv2.bitwise_and() applies mask on frame in the region where mask
 is true (means white).
 
 
We have successfully replaced the cloak region with the background.
Now we need those regions of our main frame where the clock is not 
present. To get this we can simply invert the mask and do the same 
procedure for the main frame. 
Here we have the inverse mask at the left and the corresponding 
region from the current frame at the right.'''

    


'''Explanation:

cv2.bitwise_not() inverse the mask pixel value. Where the mask is
 white it returns black and where is black it returns white.'''



'''Step 5 – Combine masked frames together:
Finally, we have a cloak background and current frame background. 
Now it’s time to combine those to get a whole frame.


Explanation:

cv2.add() adds two frames and returns a single frame.'''




cap.release()
cv2.destroyAllWindows()


'''Summary:
In this Computer vision project, we have created Invisible Cloak
 using OpenCV. We implemented color detection and segmentation
  technique. In this opencv project, we learned about morphological 
    operations, masking, and other image processing concepts.
'''