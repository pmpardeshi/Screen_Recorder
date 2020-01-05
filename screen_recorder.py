import cv2
import numpy as np
import mss
import tkinter
import threading
 





root = tkinter.Tk()
width = int(root.winfo_screenwidth())
height = int(root.winfo_screenheight())


#fourcc=cv2.VideoWriter_fourcc(*'mp4v')
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter("output4.avi",fourcc,29.0,(width,height))
mon = {"top": 0, "left": 0, "width":width, "height":height}
sct = mss.mss()

#print(f"width {width}1366,\n height {height} 768")
recording=True
thread1=threading.Thread(target=record,args=(mon,out))
thread1.start()


