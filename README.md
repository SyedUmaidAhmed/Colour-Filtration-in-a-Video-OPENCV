# Colour-Filtration-in-a-Video-OPENCV
This will filter out required color using HSV and we can track objects through it


Object Tracking
Now we know how to convert BGR image to HSV, we can use this to extract a colored object. In HSV, it is more easier to represent a color than RGB color-space. In our application, we will try to extract a blue colored object. So here is the method:
Take each frame of the video
Convert from BGR to HSV color-space
We threshold the HSV image for a range of blue color
Now extract the blue object alone, we can do whatever on that image we want.


How to find HSV values to track?
This is a common question found in stackoverflow.com. It is very simple and you can use the same function, cv2.cvtColor(). Instead of passing an image, you just pass the BGR values you want. For example, to find the HSV value of Green, try following commands in Python terminal:
>>> green = np.uint8([[[0,255,0 ]]])
>>> hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
>>> print hsv_green
[[[ 60 255 255]]]

Also check this,


http://answers.opencv.org/question/134248/how-to-define-the-lower-and-upper-range-of-a-color/
