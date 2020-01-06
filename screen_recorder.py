from tkinter import *
import tkinter.messagebox
from tkinter import font
import cv2
from PIL import Image
import numpy as np
from mss import mss
import threading
from datetime import datetime


def stop_rec():
	global recording,vid_file
	recording=False

	status_bar['text']=vid_file+',saved'



def on_exit():
	chk=tkinter.messagebox.askquestion("Exit App","Are you sure want to exit ?")
	if chk=='yes':
		stop_rec()
		root.destroy()
	

def thread_recording():
	global vid_file
	n=datetime.now()
	vid_file=str(n.date()).replace('-','')+str(n.hour)+str(n.minute)+str(n.second)+'.avi'
	#fourcc=cv2.VideoWriter_fourcc(*'mp4v')
	fourcc=cv2.VideoWriter_fourcc(*'MJPG')
	out=cv2.VideoWriter(vid_file,fourcc,50,(width,height))
	mon = {"top": 0, "left": 0, "width":width, "height":height}
	sct = mss()


	status_bar['text']="Recording... "
	
	thread1=threading.Thread(target=record,args=(mon,out,sct))
	thread1.start()

def record(mon,out,sct):

	global recording
	
	recording=True
	i=1
	
	while recording:
		
		frame = sct.grab(mon)
		frame = Image.frombytes('RGB', frame.size, frame.rgb)
		frame = cv2.cvtColor(np.array(frame), cv2.COLOR_BGR2RGB)
		out.write(np.array(frame))

	out.release()




def show_info():
	tkinter.messagebox.showinfo("About ScreenRec","it the the tool for screen recording written python")


def show_dev():
	tkinter.messagebox.showinfo("About Developer","Pramod Mangesh Pardeshi\nB.E.(Computer)\n\npramodmpardeshi@gmail.com")




if __name__ == "__main__":

	root = Tk()
	#screen height and width for recording video
	width = int(root.winfo_screenwidth())
	height = int(root.winfo_screenheight())


	#------initialization for screen recording------
	
	recording=False
	vid_file=''
	print(cv2.__version__)
	#------initialization GUI------

	icon = PhotoImage(file='img/rec.gif')
	root.tk.call('wm', 'iconphoto', root._w, icon)

	myFont = font.Font(family="Helvetica", size=10)
	
	root.option_add('*Dialog.msg.font', myFont)
	root.configure(background='#282923')
	root.resizable(0,0)
	root.geometry('180x90')
	root.title("ScreenRec")

	#menubar
	menubar=Menu(root,bg='#6D6E6A',bd = 0,fg='#c8cbcf',font=myFont)
	root.config(menu=menubar)

	submenu=Menu(menubar,tearoff=0,bg='#6D6E6A',fg='#c8cbcf',font=myFont)
	menubar.add_cascade(label="File",menu=submenu)
	submenu.add_command(label="Record")
	submenu.add_command(label="Pause")
	submenu.add_command(label="Exit",command=on_exit)

	submenu2=Menu(menubar,tearoff=0,bg='#6D6E6A',fg='#c8cbcf',font=myFont)
	suboption=Menu(submenu2,tearoff=0,bg='#6D6E6A',fg='#c8cbcf',font=myFont) #for menu inside menu
	menubar.add_cascade(label="Help",menu=submenu2)
	submenu2.add_cascade(label="About",menu=suboption)#menu to be defined under submenu
	suboption.add_command(label="About Developer",command=show_dev)#for label does not require menu
	suboption.add_command(label="About Product",command=show_info)
	#root.iconbitmap(r'rec.ico')
	


	btn_frame=Frame(root,bg="#282923")
	btn_frame.pack(pady=15)

	record_label=Label(btn_frame,text="record",bg='#282923',fg='#a3a5a8',font=myFont)
	record_label.grid(row=1,column=0,padx=10)


	img=PhotoImage(file='img/record.png')
	record_button=Button(btn_frame,image=img,command=thread_recording,bg='#282923', highlightthickness = 0, bd = 0)
	record_button.grid(row=0,column=0,padx=10)

	stop_label=Label(btn_frame,text="stop",bg='#282923',fg='#a3a5a8',font=myFont)
	stop_label.grid(row=1,column=1,padx=10)

	img2=PhotoImage(file='img/stop.png')
	stop_button=Button(btn_frame,image=img2,command=stop_rec,bg='#282923', highlightthickness = 0, bd = 0)
	stop_button.grid(row=0,column=1,padx=10)

	status_bar=Label(root,text="ScreenRec...",relief=GROOVE, anchor=W,bg='#ABB1BA',fg='#282923',font=myFont)
	status_bar.pack(side=BOTTOM,fill=X)



	root.protocol("WM_DELETE_WINDOW",on_exit)#for exit button
	root.mainloop()