import sys
import tkinter
from tkinter import *
import customtkinter
from PIL import ImageTk, Image


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"

class App(customtkinter.CTk):
    APP_NAME = "Predection Tweets"
    WIDTH = 700
    HEIGHT = 500

    MAIN_COLOR = "#3498DB"
    MAIN_COLOR_DARK = "#2D5862"
    MAIN_HOVER = "#3498DB"


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(App.APP_NAME)
        self.geometry(str(App.WIDTH) + "x" + str(App.HEIGHT))
        self.minsize(App.WIDTH, App.HEIGHT)
        self.iconbitmap(r'C:\Users\PRO\PycharmProjects\pythonProject\twitter.ico')

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        if sys.platform == "darwin":
            self.bind("<Command-q>", self.on_closing)
            self.bind("<Command-w>", self.on_closing)
            self.createcommand('tk::mac::Quit', self.on_closing)


        self.button_1 = customtkinter.CTkButton(master=self,
                                                border_color=App.MAIN_COLOR,
                                                fg_color=None,
                                                hover_color=App.MAIN_HOVER,
                                                text="Exit",
                                                command=self.on_closing,
                                                border_width=2,
                                                corner_radius=5)
        self.button_1.place(relx=0.7, y=380, anchor=tkinter.CENTER)
        self.button_2 = customtkinter.CTkButton(master=self,
                                                border_color=App.MAIN_COLOR,
                                                fg_color=None,
                                                hover_color=App.MAIN_HOVER,
                                                text="Predict",
                                                command=self.display_dialog,
                                                border_width=2,
                                                corner_radius=5)
        self.button_2.place(relx=0.3, y=380, anchor=tkinter.CENTER)

        self.entry = customtkinter.CTkEntry(master=self,
                                            width=500,
                                            height=100,
                                            corner_radius=5)
        self.entry.place(relx=0.5, y=300, anchor=tkinter.CENTER)
        self.entry.insert(0, "Enter the Tweet")

        self.img1 = ImageTk.PhotoImage(Image.open("logo.jpeg"))
        self.labelimage=Label(image=self.img1)
        self.labelimage.pack(pady=(4, 20))



#########
    # windows 3

    def display_dialog(self):

        dialog = tkinter.Toplevel()
        big_frame = tkinter.Frame(dialog)
        big_frame.pack(fill='both', expand=True)
        dialog.iconbitmap(r'C:\Users\PRO\PycharmProjects\pythonProject\twitter.ico')
        btn = Button(dialog, text="Close", command=dialog.destroy)
        btn.pack()
        #recupere le txt de l'entree
        text = self.entry.get()
        print(text)
        label = tkinter.Label(big_frame, text="Hello World")
        label.place(relx=0.5, rely=0.3, anchor='center')
        dialog.transient(self)
        dialog.geometry('300x150')
        dialog.wait_window()

    def button_event(self):
        print("Button pressed")

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()



if __name__ == "__main__":
        app = App()
        app.start()