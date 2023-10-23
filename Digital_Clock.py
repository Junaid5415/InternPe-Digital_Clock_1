from tkinter import * # Import tkinter library

from time import strftime #strftime is a method to get time in a format

class my_Clock: # make a class

    def __init__(self,root): # Initialize all the property of root
        self.root = root
        self.root.title('Digital Clock') # Give title of the application
        self.root.wm_iconbitmap('Digital_Clock.ico') # This code is use to set icon of the application
        self.root.config(bg= 'black') # Changes background to black
        self.label1 = Label(root,bg='#000000',fg= '#7FFF00', # Initiallized a label to hold the time value
                            cursor='crosshair',font=('Radioland',30))
        self.label1.pack(anchor='center') # Anchor value is set to center it means the value will be show in center
        self.clock() # Call the method

    def clock(self): # Make a method
        time = strftime('%H,%M,%S,%p') # Format the values you want to get in the label
        self.label1.config(text=time) # With this code the value will be visible to label
        self.label1.after(1000,self.clock) # this will update the clock every 1000 ms or 1 seconds



if __name__ == '__main__':
    root = Tk()
    app = my_Clock(root)
    root.mainloop()