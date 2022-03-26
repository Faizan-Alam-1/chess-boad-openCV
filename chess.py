from ast import For
import cv2
print(cv2.__version__)
import numpy as np

Size_boad = int(input("Enter the size of boad "))
Number_box =int(input("Enter the number of box "))
Size_box =  int(Size_boad/Number_box)

white_color = (255, 255 ,255)
black_color = (0,0,0)
current_color = black_color


while True :
    frame = np.zeros([Size_boad,Size_boad ,3], dtype=np.uint8)
    for row in range(0 , Number_box):
        for col in range(0, Number_box):
            frame[Size_box*row : Size_box*(row+1),Size_box*col:Size_box*(col+1)] = current_color
            if  current_color == black_color :
                current_color = white_color
            else:
                current_color = black_color
         
       


    cv2.imshow("my windows", frame)
    if cv2.waitKey(100) & 0xff == ord('q'):
            break