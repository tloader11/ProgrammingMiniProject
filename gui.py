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
        self.configure(bg='#FFCC18')
        titelLabel = tk.Label(self, bg="#FFCC18", anchor=tk.W, justify=tk.LEFT, text="NS-Fietsenstalling", font=LARGE_FONT)
        titelLabel.pack(pady=10, padx=10)

        registerButton = tk.Button(self, height=5, width=20, justify=tk.LEFT, text="Registreer", command=lambda: controller.show_frame(RegisterPage))
        stallButton = tk.Button(self, height=5, width=20, justify=tk.LEFT, text="Stal fiets", command=lambda: controller.show_frame(StallPage))
        pickupButton = tk.Button(self, height=5, width=20, justify=tk.LEFT, text="Haal fiets op", command=lambda: controller.show_frame(PickupPage))
        infoButton = tk.Button(self, height=5, width=20, justify=tk.LEFT, text="Informatie opvragen", command=lambda: controller.show_frame(InfoPage))

        registerButton.pack(side=tk.LEFT)
        stallButton.pack(side=tk.LEFT)
        pickupButton.pack(side=tk.LEFT)
        infoButton.pack(side=tk.LEFT)

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
