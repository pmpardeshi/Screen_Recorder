from tkinter import *
import tkinter.messagebox
import cv2
import numpy as np
import mss
import threading


def stop_rec():
	global recording
	recording=False



def on_exit():
	tkinter.messagebox.showinfo("","You sure want to exit")
	root.destroy()

def thread_recording():
	global recording,mon,out

	status_bar['text']="Recording... "
	recording=True
	thread1=threading.Thread(target=record,args=(mon,out))
	thread1.start()

def record(mon,out):
	
	while recording:
		
		frame= np.asarray(sct.grab(mon))
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		out.write(frame)
	
	out.release()




def show_info():
	tkinter.messagebox.showinfo("About ScreenRec","it the the tool to screen recording")






if __name__ == "__main__":

	root = Tk()
	#screen height and width for recording video
	width = int(root.winfo_screenwidth())
	height = int(root.winfo_screenheight())


	#------initialization for screen recording------
	
	#fourcc=cv2.VideoWriter_fourcc(*'mp4v')
	fourcc=cv2.VideoWriter_fourcc(*'XVID')
	out=cv2.VideoWriter("output4.avi",fourcc,29.0,(width,height))
	mon = {"top": 0, "left": 0, "width":width, "height":height}
	sct = mss.mss()
	recording=False



	#------initialization GUI------


	root.configure(background='#282923')
	root.resizable(0,0)
	root.geometry('175x90')
	root.title("ScreenRec")

	#menubar
	menubar=Menu(root,bg='#6D6E6A',bd = 0)
	root.config(menu=menubar)

	submenu=Menu(menubar,tearoff=0,bg='#6D6E6A')
	menubar.add_cascade(label="File",menu=submenu)
	submenu.add_command(label="Record")
	submenu.add_command(label="Pause")
	submenu.add_command(label="Exit",command=on_exit)

	submenu2=Menu(menubar,tearoff=0,bg='#6D6E6A')
	suboption=Menu(submenu2,tearoff=0,bg='#6D6E6A') #for menu inside menu
	menubar.add_cascade(label="Help",menu=submenu2)
	submenu2.add_cascade(label="About",menu=suboption)#menu to be defined under submenu
	suboption.add_command(label="About Developer")#for label does not require menu
	suboption.add_command(label="About Product",command=show_info)
	#root.iconbitmap(r'rec.ico')
	icon = PhotoImage(file='rec.gif')
	root.tk.call('wm', 'iconphoto', root._w, icon)


	btn_frame=Frame(root,bg="#282923")
	btn_frame.pack(pady=15)

	record_label=Label(btn_frame,text="record",bg='#282923')
	record_label.grid(row=1,column=0,padx=10)

	img=PhotoImage(file='record.png')
	record_button=Button(btn_frame,image=img,command=thread_recording,bg='#282923', highlightthickness = 0, bd = 0)
	record_button.grid(row=0,column=0,padx=10)

	stop_label=Label(btn_frame,text="stop",bg='#282923')
	stop_label.grid(row=1,column=1,padx=10)

	img2=PhotoImage(file='stop.png')
	stop_button=Button(btn_frame,image=img2,command=stop_rec,bg='#282923', highlightthickness = 0, bd = 0)
	stop_button.grid(row=0,column=1,padx=10)

	status_bar=Label(root,text="welcome...",relief=GROOVE, anchor=W,bg='#ABB1BA')
	status_bar.pack(side=BOTTOM,fill=X)



	root.protocol("WM_DELETE_WINDOW",on_exit)
	root.mainloop()