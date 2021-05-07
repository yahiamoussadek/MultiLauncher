import tkinter
from tkinter import filedialog, Text, messagebox
import os 
import webbrowser
###################
root = tkinter.Tk()
root.configure(background="#f43421")
root.title('MultiLauncher')
root.resizable(0,0)
root.iconbitmap('icon.ico')

apps = []
###################
if os.path.isfile('data.txt'):
	with open('data.txt','r') as f:
		tempApps = f.read()
		tempApps = tempApps.split(',')
		apps = [x for x in tempApps if x.strip()]
###################
def donate():
	messagebox.showinfo("EMAIL","E-Mail : yahiamoussadek17@gmail.com")
def add_app(event="walo"):
	filename = filedialog.askopenfilename(initialdir="/",title="Select File", filetypes=(("excutables","*.exe"),("all files","*.*")))
	apps.append(filename)
	for i in apps:
		label = tkinter.Label(frame,text=i)
	label.pack()
###################
def run_apps(event="walo"):
	for i in apps:
		os.startfile(i)
###################
root.bind('<Control-o>', add_app)
root.bind('<Control-r>', run_apps)
###################
def contact():
	webbrowser.open_new(r'https://www.facebook.com/thomas.stewart.336333')
###################
canvas = tkinter.Canvas(root, height=500, width=500, bg="#f43421",highlightthickness=0)
canvas.pack()
###################
frame = tkinter.Frame(root, bg='white')
frame.pack(fill=None, expand=False)
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
###################
openFile = tkinter.Button(root,text="Open File - CTRL+O", padx=10, pady=5,fg="white", bg="#0c0c0c",command=add_app)
openFile.pack()
###################
runApps = tkinter.Button(root,text='Run Apps - CTRL+R',padx=10,pady=5,fg="white",bg="#0c0c0c",command=run_apps)
runApps.pack()
###################
contact = tkinter.Button(root,text="Contact Me",padx=10,pady=5,fg="white",bg="#0c0c0c",command=contact)
contact.pack(side="right",fill="y")
developer = tkinter.Button(root,text="Yahia Moussadek",padx=10,pady=5,fg="white",bg="#0c0c0c",command=donate)
developer.pack(side="left",fill="y")
###################
for app in apps: 
	label = tkinter.Label(frame,text=app)
	label.pack()
###################
root.mainloop()
###################
###################
with open('data.txt','w') as f:
	for app in apps:
		f.write(app+',')