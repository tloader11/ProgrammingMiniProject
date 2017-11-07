import base64
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from programming_main import *
from tkinter import messagebox

import io

LARGE_FONT=("Verdana", 12)
background_color="#F6D03F"
button_background_color="#1D0065"
button_foreground_color="white"
button_active_background_color="#005ca0"

# example code = 8470486
# example bday = 15-04-1998
class NSFietsenstalling(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #tk.Tk.iconbitmap(self, default="")
        tk.Tk.wm_title(self, "NS-Fietsenstalling")
        tk.Tk.wm_geometry(self,"700x455")       #fixed screen diameters
        tk.Tk.resizable(self, False, False)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, RegisterPage, StallPage, PickupPage, InfoPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background=background_color)
        titelLabel = tk.Label(self, bg=background_color, anchor=tk.W, justify=tk.LEFT, text="NS-Fietsenstalling", font=LARGE_FONT)
        titelLabel.pack(pady=10, padx=10)

        image = Image.open("NS.jpg")
        photoholder = ImageTk.PhotoImage(image)
        photo = tk.Label(self, image=photoholder)
        photo.image = photoholder
        photo.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)

        registerButton = tk.Button(self, height=5, width=23, justify=tk.LEFT, bg=button_background_color, activebackground=button_active_background_color, fg=button_foreground_color, activeforeground=button_foreground_color, text="Registreer", command=lambda: controller.show_frame(RegisterPage))
        stallButton = tk.Button(self, height=5, width=25, justify=tk.LEFT, bg=button_background_color, activebackground=button_active_background_color, fg=button_foreground_color, activeforeground=button_foreground_color, text="Stal fiets", command=lambda: controller.show_frame(StallPage))
        pickupButton = tk.Button(self, height=5, width=25, justify=tk.LEFT, bg=button_background_color, activebackground=button_active_background_color, fg=button_foreground_color, activeforeground=button_foreground_color, text="Haal fiets op", command=lambda: controller.show_frame(PickupPage))
        infoButton = tk.Button(self, height=5, width=22, justify=tk.LEFT, bg=button_background_color, activebackground=button_active_background_color, fg=button_foreground_color, activeforeground=button_foreground_color, text="Informatie opvragen", command=lambda: controller.show_frame(InfoPage))

        registerButton.pack(fill=tk.BOTH, side=tk.LEFT)
        stallButton.pack(fill=tk.BOTH, side=tk.LEFT)
        pickupButton.pack(fill=tk.BOTH, side=tk.LEFT)
        infoButton.pack(fill=tk.BOTH, side=tk.LEFT)

class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background=background_color)
        titelLabel = ttk.Label(self, text="NS-Fietsenstalling", font=LARGE_FONT, background=background_color)
        titelLabel.pack(pady=10, padx=10)

        homeButton = tk.Button(self, height=4, text="Naar beginscherm", background=button_background_color, activebackground=button_active_background_color, foreground=button_foreground_color, activeforeground=button_foreground_color, relief="flat", command=lambda: controller.show_frame(StartPage))

        homeButton.pack(fill=tk.BOTH,side=tk.BOTTOM)

class StallPage(tk.Frame):
    def StallBike(self, controller, code, bday):
        code_text = code.get("1.0",tk.END)[:-1]
        bday_text = bday.get("1.0",tk.END)[:-1]
        print(code_text)
        print(bday_text)
        bday.delete("1.0",tk.END)
        code.delete("1.0",tk.END)
        if CheckAuth(code_text,bday_text):
            Stall(code)
            controller.show_frame(StartPage)
        else:
            messagebox.showerror("Ongeldig", message="Ongeldige code / geboortedatum combinatie")

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background=background_color)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(5, weight=1)

        titleLabel = ttk.Label(self, text="NS-Fietsenstalling", font=LARGE_FONT, background=background_color).grid(row=0,pady=10, padx=10,columnspan=3)
        codeLabel = ttk.Label(self, text="Uw unieke nummer (ex. 6658469):", background=background_color).grid(row=1,column=0, sticky=tk.E)
        code = tk.Text(self, height=1, width=15)
        code.grid(row=1,pady=10, padx=10,column=1, sticky=tk.W)
        bdayLabel = ttk.Label(self, text="Uw geboortedatum (ex. 15-04-1998):", background=background_color).grid(row=2,column=0, sticky=tk.E)
        bday = tk.Text(self, height=1, width=15)
        bday.grid(row=2,pady=10, padx=10,column=1, sticky=tk.W)

        stallButton = tk.Button(self, height=4, width=30, text="Zet fiets in stalling", background=button_background_color, activebackground=button_active_background_color, foreground=button_foreground_color, activeforeground=button_foreground_color, relief="flat", command=lambda: self.StallBike(controller, code, bday))
        stallButton.grid(row=3, column=0, columnspan=3, pady=30)

        homeButton = tk.Button(self, height=4, text="Naar beginscherm", background=button_background_color, activebackground=button_active_background_color, foreground=button_foreground_color, activeforeground=button_foreground_color, relief="flat", command=lambda: controller.show_frame(StartPage))
        homeButton.grid(row=5, column=0, columnspan=3, sticky=tk.EW+tk.S)
        #homeButton.pack(fill=tk.BOTH,side=tk.BOTTOM)


class PickupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background=background_color)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(5, weight=1)

        titleLabel = ttk.Label(self, text="NS-Fietsenstalling", font=LARGE_FONT, background=background_color).grid(row=0,pady=10, padx=10,columnspan=3)
        codeLabel = ttk.Label(self, text="Uw unieke nummer (ex. 6658469):", background=background_color).grid(row=1,column=0, sticky=tk.E)
        code = tk.Text(self, height=1, width=15).grid(row=1,pady=10, padx=10,column=1, sticky=tk.W)
        codeLabel = ttk.Label(self, text="Uw geboortedatum (ex. 15-04-1998):", background=background_color).grid(row=2,column=0, sticky=tk.E)
        code = tk.Text(self, height=1, width=15).grid(row=2,pady=10, padx=10,column=1, sticky=tk.W)

        stallButton = tk.Button(self, height=4, width=30, text="Haal fiets op", background=button_background_color, activebackground=button_active_background_color, foreground=button_foreground_color, activeforeground=button_foreground_color, relief="flat", command=lambda: controller.show_frame(StartPage))
        stallButton.grid(row=3, column=0, columnspan=3, pady=30)

        homeButton = tk.Button(self, height=4, text="Naar beginscherm", background=button_background_color, activebackground=button_active_background_color, foreground=button_foreground_color, activeforeground=button_foreground_color, relief="flat", command=lambda: controller.show_frame(StartPage))
        homeButton.grid(row=5, column=0, columnspan=3, sticky=tk.EW+tk.S)

class InfoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background=background_color)
        titelLabel = ttk.Label(self, text="NS-Fietsenstalling", font=LARGE_FONT, background=background_color)
        titelLabel.pack(pady=10, padx=10)

        homeButton = tk.Button(self, height=4, text="Naar beginscherm", background=button_background_color, activebackground=button_active_background_color, foreground=button_foreground_color, activeforeground=button_foreground_color, relief="flat", command=lambda: controller.show_frame(StartPage))

        homeButton.pack(fill=tk.BOTH,side=tk.BOTTOM)

app = NSFietsenstalling()
app.mainloop()
