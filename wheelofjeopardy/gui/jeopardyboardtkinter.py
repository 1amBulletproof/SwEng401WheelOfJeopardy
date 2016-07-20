"""
wheelofjeopardy GUI prototype using

using 3rd party Pillow which is a fork of the (possibly dead) Python Image Library
"""

from Tkinter import *
from PIL import Image, ImageTk

#@TODO make rotating image
#@TODO include basic features for game GUI
#@TODO Update this GUI to represent Game Board
class WheelOfJeopardyGui(Tk):
    def __init__(self, parent=None):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        self.configure(bg="#e6f3ff")

    def initialize(self):
        self.grid() # packing/geometry method

        #buttons
        self.button_1 = Button(self, text = "Button 1", command = self.press_button_1)
        self.button_1.grid(column=0, row=0, sticky="S", padx=20, pady=10)

        self.button_spin_wheel = Button(self, text = "Spin the Wheel", command = self.rotate_wheel)
        self.button_spin_wheel.grid(column=2, row=0, sticky="S", padx=20, pady=10)

        self.button_quit = Button(self, text = "QUIT", command = self.quit)
        self.button_quit.grid(column=1, row=4, padx=30, pady=15)

        #Labels
        self.label_1 = Label(self,  text ="Button 1")
        self.label_1.grid(column=0, row=1, sticky="N", padx=20, pady=10)

        self.label_2 = Label(self,  text ="Spin The Wheel!")
        self.label_2.grid(column=2, row=1, sticky="N", padx=20, pady=10)

        #image
        # self.image_wheel = Image.open("../../img/wheel_of_fortune_1975.png")
        self.image_wheel = Image.open("wheel_of_fortune_1975.png")
        self.tk_image_wheel = ImageTk.PhotoImage(self.image_wheel)
        self.label_image = Label(image=self.tk_image_wheel)
        self.label_image.image = self.tk_image_wheel

        #Canvas for image
        self.canvas = Canvas(self, width=1500, height=1200)
        self.canvas.create_image(500, 500, image=self.tk_image_wheel)
        self.canvas.grid(column=1, row=2, sticky="S", padx=20, pady=10)

    def press_button_1(self):
        print("button 1 pressed")

    def rotate_wheel(self):
        #@todo wheel spin logic
        print("spin the wheel! WEEEEEEE!")

if __name__ == "__main__":
    gui = WheelOfJeopardyGui(None)
    gui.title("Wheel Of Jeopardy!")
    gui.geometry()
    gui.mainloop()
