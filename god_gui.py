import tkinter as tk

#STATE 1
TEXT1 = "Red"
COLOR1 = "red"
ICON1 = "red_circle.ico"

#STATE 2
TEXT2 = "Blue"
COLOR2 = "blue"
ICON2 = "blue_circle.ico"

class GodGUI(object):
    
    def __init__(self, root):
        self.root = root
        self.text = tk.StringVar()
        self.frame = tk.Frame(root)
        self.button = tk.Button(self.frame)
        
        self.text.set(TEXT1)
        self.frame.config(bg=COLOR1)
        self.button.config(textvariable=self.text, command=self.clicked, width=5)
        
        root.title("")
        root.minsize(160, 60)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        root.iconbitmap(ICON1)
        root.geometry("200x200")
        
        self.frame.grid(sticky="nsew")
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        
        self.button.grid()
        
        root.bind("<Return>", self.clicked)
        
    def clicked(self, event=None):
        if self.text.get() == TEXT1:
            self.text.set(TEXT2)
            self.frame.config(bg=COLOR2)
            self.root.iconbitmap(ICON2)
        else:
            self.text.set(TEXT1)
            self.frame.config(bg=COLOR1)
            self.root.iconbitmap(ICON1)
        

main = tk.Tk()
GodGUI(main)
main.mainloop()
