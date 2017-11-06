import tkinter as tk
from tkinter import ttk

LARGE_FONT=("Verdana", 12)

class NSFietsenstalling(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #tk.Tk.iconbitmap(self, default="")
        tk.Tk.wm_title(self, "NS-Fietsenstalling")
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
        self.configure(bg='yellow')
        titelLabel = ttk.Label(self, text="NS-Fietsenstalling", font=LARGE_FONT)
        titelLabel.pack(pady=10, padx=10)

        registerButton = ttk.Button(self, text="Registreer", command=lambda: controller.show_frame(RegisterPage))
        stallButton = ttk.Button(self, text="Stal fiets", command=lambda: controller.show_frame(StallPage))
        pickupButton = ttk.Button(self, text="Haal fiets op", command=lambda: controller.show_frame(PickupPage))
        infoButton = ttk.Button(self, text="Informatie opvragen", command=lambda: controller.show_frame(InfoPage))

        registerButton.pack()
        stallButton.pack()
        pickupButton.pack()
        infoButton.pack()

class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='yellow')
        titelLabel = ttk.Label(self, text="NS-Fietsenstalling", font=LARGE_FONT)
        titelLabel.pack(pady=10, padx=10)

        homeButton = ttk.Button(self, text="Naar beginscherm", command=lambda: controller.show_frame(StartPage))
        homeButton.pack()

class StallPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='yellow')
        titelLabel = ttk.Label(self, text="NS-Fietsenstalling", font=LARGE_FONT)
        titelLabel.pack(pady=10, padx=10)

        homeButton = ttk.Button(self, text="Naar beginscherm", command=lambda: controller.show_frame(StartPage))
        homeButton.pack()

class PickupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='yellow')
        titelLabel = ttk.Label(self, text="NS-Fietsenstalling", font=LARGE_FONT)
        titelLabel.pack(pady=10, padx=10)

        homeButton = ttk.Button(self, text="Naar beginscherm", command=lambda: controller.show_frame(StartPage))
        homeButton.pack()

class InfoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='yellow')
        titelLabel = ttk.Label(self, text="NS-Fietsenstalling", font=LARGE_FONT)
        titelLabel.pack(pady=10, padx=10)

        homeButton = ttk.Button(self, text="Naar beginscherm", command=lambda: controller.show_frame(StartPage))
        homeButton.pack()

app = NSFietsenstalling()
app.mainloop()
