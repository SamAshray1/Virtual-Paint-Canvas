# Virtual-Paint-Canvas

A OpenCV Virtual Paint project which detects the colour of the marker via webcam and draws on the screen. Colour detection is handled by using tracbars and the image is converted to HSV colour scheme and then using Masking techniques and Contour Detection - drawing circles of respective colour on the tip of the held marker.

Steps to Run this Project:
1) Download the Zip folder, extract and open the Project in PyCharm IDE. (Python 3.7-3.9.x versions can be used.)
2) Import opencv-python and numpy libraires in the settings of the IDE.
3) Use Colour_Detection.py to find the Hue_Min, Hue_Max, Sat_Min, Sat_Max, Val_Min, Val_Max of a particular colour marker.
4) Make the necessary changes in myColours in Project.py with the above found values.
5) Change the values in myColorValues to match the colour of the marker.
6) Run Project.py
