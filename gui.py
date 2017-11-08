import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from programming_main import *
from tkinter import messagebox
import re

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
        tk.Tk.iconbitmap(self, default="favicon.png")
        tk.Tk.wm_title(self, "NS-Fietsenstalling")
        tk.Tk.wm_geometry(self,"700x455")       #start screen diameters
        #tk.Tk.resizable(self, False, False)
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, RegisterPage, StallPage, PickupPage, InfoPage, PersonalInfoPage):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
    def showDisplayFrame(self,code,bday):
        frame = PersonalInfoDisplayer(self.container,self,code,bday)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
    def showInfoPage(self):
        frame = GeneralInfoPage(self.container,self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

class StartPage(tk.Frame):

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height - 10
        self.image = self.img_copy.resize((new_width, new_height))
        self.photoholder = ImageTk.PhotoImage(self.image)
        self.photo.configure(image =  self.photoholder)

    def __init__(self, parent, controller):

        self.image = Image.open("NS_new2.jpg")
        self.img_copy= self.image.copy()

        tk.Frame.__init__(self, parent)

        self.configure(background=background_color)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1, uniform="fred")
        self.grid_columnconfigure(1, weight=1, uniform="fred")
        self.grid_columnconfigure(3, weight=1, uniform="fred")
        titleLabel = ttk.Label(self, text="NS-Fietsenstalling", font=LARGE_FONT, background=background_color)
        titleLabel.grid(row=0, column=0, columnspan=4, pady=10, padx=10)
        #titelLabel = tk.Label(self, bg=background_color, anchor=tk.W, justify=tk.LEFT, text="NS-Fietsenstalling", font=LARGE_FONT)
        #titelLabel.pack(pady=10, padx=10)

        self.photoholder = ImageTk.PhotoImage(self.image)
        self.photo = tk.Label(self, image=self.photoholder)

        self.photo.image = self.photoholder
        self.photo.grid(row=1, columnspan=4,column=0,sticky=tk.NSEW)
        #self.photo.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
        self.photo.bind('<Configure>', self._resize_image)

        registerButton = tk.Button(self, height=5, justify=tk.LEFT, bg=button_background_color, activebackground=button_active_background_color, fg=button_foreground_color, activeforeground=button_foreground_color, text="Registreer", command=lambda: controller.show_frame(RegisterPage))
        stallButton = tk.Button(self, height=5, justify=tk.LEFT, bg=button_background_color, activebackground=button_active_background_color, fg=button_foreground_color, activeforeground=button_foreground_color, text="Stal fiets", command=lambda: controller.show_frame(StallPage))
        pickupButton = tk.Button(self, height=5, justify=tk.LEFT, bg=button_background_color, activebackground=button_active_background_color, fg=button_foreground_color, activeforeground=button_foreground_color, text="Haal fiets op", command=lambda: controller.show_frame(PickupPage))
        infoButton = tk.Button(self, height=5, justify=tk.LEFT, bg=button_background_color, activebackground=button_active_background_color, fg=button_foreground_color, activeforeground=button_foreground_color, text="Informatie opvragen", command=lambda: controller.show_frame(InfoPage))

        registerButton.grid(row=2, column=0, sticky=tk.NSEW)
        stallButton.grid(row=2,column=1, sticky=tk.NSEW)
        pickupButton.grid(row=2,column=2, sticky=tk.NSEW)
        infoButton.grid(row=2,column=3, sticky=tk.NSEW)
        #registerButton.pack(fill=tk.BOTH, side=tk.LEFT)
        #stallButton.pack(fill=tk.BOTH, side=tk.LEFT)
        #pickupButton.pack(fill=tk.BOTH, side=tk.LEFT)
        #infoButton.pack(fill=tk.BOTH, side=tk.LEFT)

class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        sex = tk.IntVar()

        self.configure(background=background_color)
        #Weight for column and row configure for better positioning on grid layouty
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(7, weight=1)

        titleLabel = ttk.Label(self, text="NS-Fietsenstalling", font=LARGE_FONT, background=background_color)
        titleLabel.grid(row=0, column=0, columnspan=3, pady=10, padx=10)

        #Input for registering
        #Inputs: Name, Tel, Sex, Bday

        nameEntryLabel = tk.Label(self, background=background_color, text="Naam (ex. Jan Janssen):")
        nameEntry = tk.Entry(self)
        telEntryLabel = tk.Label(self, background=background_color, text="Telefoonnummer (ex. +31612345678):")
        telEntry = tk.Entry(self)
        sexLabel = tk.Label(self, background=background_color, text="Geslacht:")
        sexButtonMan = tk.Radiobutton(self, bg=background_color, activebackground=background_color, text="Man", value=1, variable=sex)
        sexButtonWoman = tk.Radiobutton(self, bg=background_color, activebackground=background_color, text="Vrouw", value=0, variable=sex)
        bdayEntryLabel = tk.Label(self, background=background_color, text="Geboortedatum (ex. 01-01-2001):")
        bdayEntry = tk.Entry(self)
        mailEntryLabel = tk.Label(self, background=background_color, text="E-Mail (ex. ditis@eenmailadres.nl):")
        mailEntry = tk.Entry(self)

        registerButton = tk.Button(self, bg=button_background_color, activebackground=button_active_background_color, fg=button_foreground_color, activeforeground=button_foreground_color, height=4, width=30, relief="flat", text="Registreer", command=lambda: checkField(nameEntry.get(), telEntry.get(), sex.get(), bdayEntry.get(), mailEntry.get()))

        registerButton.grid(row=6, column=0, columnspan=3, pady=30)

        #Put all enties, radiobuttons and labels on grid

        nameEntryLabel.grid(row=1, column=0, pady=10, padx=10, sticky=tk.E)
        nameEntry.grid(row=1, column=1, sticky=tk.EW)
        telEntryLabel.grid(row=2, column=0, pady=10, padx=10, sticky=tk.E)
        telEntry.grid(row=2, column=1, sticky=tk.EW)
        sexLabel.grid(row=3, column=0, pady=10, padx=10, sticky=tk.E)
        sexButtonMan.grid(row=3, column=1,sticky=tk.W)
        sexButtonWoman.grid(row=3, column=1)
        bdayEntryLabel.grid(row=4, column=0,pady=10, padx=10, sticky=tk.E)
        bdayEntry.grid(row=4, column=1, sticky=tk.EW)
        mailEntryLabel.grid(row=5, column=0, pady=10, padx=10, sticky=tk.E)
        mailEntry.grid(row=5, column=1, sticky=tk.EW)

        #Home buttton
        homeButton = tk.Button(self, height=4, text="Naar beginscherm", bg=button_background_color, activebackground=button_active_background_color, fg=button_foreground_color, activeforeground=button_foreground_color, relief="flat", command=lambda: controller.show_frame(StartPage))

        homeButton.grid(row=7, column=0, columnspan=3, sticky=tk.EW+tk.S)

        def checkField(name, tel, sex, bday, mail):
            if name == "" or tel == "" or bday == "" or mail == "":
                #Popup
                tk.messagebox.showerror("Oops", "Vul alle velden in")
            else:
                #Do regex check
                matchBday = re.match('\d{2}-\d{2}-\d{4}', bday)
                matchTel = re.match('\+\d{11}', tel)
                matchMail = re.match('.*@.*\.*.', mail)
                if matchBday and matchTel and matchMail:
                    if matchBday.group(0) == bday and matchTel.group(0) == tel and matchMail.group(0) == mail:
                        #Send vars to programming_main, clear fields and go to StartScreen
                        nameEntry.delete(0, tk.END)
                        telEntry.delete(0, tk.END)
                        bdayEntry.delete(0, tk.END)
                        mailEntry.delete(0, tk.END)
                        code = Register(name, tel, sex, bday, mail)
                        tk.messagebox.showinfo("Code", "Uw persoonlijke code is: " + str(code) + "\nDeze staat ook in uw mail.")
                        controller.show_frame(StartPage)
                    else:
                        tk.messagebox.showerror("Oops", "Vul alle velden in zoals de voorbeelden")
                else:
                    tk.messagebox.showerror("Oops", "Vul alle velden in zoals de voorbeelden")

class StallPage(tk.Frame):
    def StallBike(self, controller, code, bday):
        code_text = code.get("1.0",tk.END)[:-1]
        bday_text = bday.get("1.0",tk.END)[:-1]
        bday.delete("1.0",tk.END)
        code.delete("1.0",tk.END)
        if CheckAuth(code_text,bday_text):
            if(Stall(code_text) == 0):
                LogAction("Er is een fiets geplaatst onder code:"+code_text)

                details = GetMailFromCode(code_text)
                SendMessage(details[0],"Beste "+details[1]+",\n\nUw fiets is zojuist aangemeld bij ons.\nWe wensen u een fijne reis!\n\nWe hopen u voldoende informatie te hebben verstrekt,\nHet NS team.")

                messagebox.showinfo("Success", message="Uw fiets is aangemeld in ons systeem!\nTot snel!")
            else:
                messagebox.showerror("Helaas...", message="U heeft al een fiets aangemeld staan.\nHelaas kunt u maar 1 fiets aanmelden.")
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
    def RemoveBike(self, controller, code, bday):
        code_text = code.get("1.0",tk.END)[:-1]
        bday_text = bday.get("1.0",tk.END)[:-1]
        bday.delete("1.0",tk.END)
        code.delete("1.0",tk.END)
        if CheckAuth(code_text,bday_text):
            if BikePickup(code_text) == 0:
                LogAction("Er is een fiets verwijderd onder code:"+code_text)

                details = GetMailFromCode(code_text)
                SendMessage(details[0],"Beste "+details[1]+",\n\nUw fiets is zojuist afgemeld bij ons.\nHopelijk tot snel!\n\nWe hopen u voldoende informatie te hebben verstrekt,\nHet NS team.")
                messagebox.showinfo("Success", message="Uw fiets is afgemeld in ons systeem!\nVeel rijdplezier.")
            else:
                messagebox.showerror("Helaas", message="U had uw fiets al opgehaald.\nDronken avond gehad?")
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

        stallButton = tk.Button(self, height=4, width=30, text="Haal fiets op", background=button_background_color, activebackground=button_active_background_color, foreground=button_foreground_color, activeforeground=button_foreground_color, relief="flat", command=lambda: self.RemoveBike(controller, code, bday))
        stallButton.grid(row=3, column=0, columnspan=3, pady=30)

        homeButton = tk.Button(self, height=4, text="Naar beginscherm", background=button_background_color, activebackground=button_active_background_color, foreground=button_foreground_color, activeforeground=button_foreground_color, relief="flat", command=lambda: controller.show_frame(StartPage))
        homeButton.grid(row=5, column=0, columnspan=3, sticky=tk.EW+tk.S)
        #homeButton.pack(fill=tk.BOTH,side=tk.BOTTOM)

class InfoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background=background_color)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        titleLabel = ttk.Label(self, text="NS-Fietsenstalling", font=LARGE_FONT, background=background_color)
        titleLabel.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        GeneralInfoButton = tk.Button(self, height=4, background=button_background_color, activebackground=button_active_background_color, foreground=button_foreground_color, activeforeground=button_foreground_color, relief="flat", text="Algemene informatie", command=lambda: controller.showInfoPage())
        GeneralInfoButton.grid(row=1, column=0, padx=10, pady=10, sticky=tk.EW+tk.S)
        personalInfoButton = tk.Button(self, height=4, background=button_background_color, activebackground=button_active_background_color, foreground=button_foreground_color, activeforeground=button_foreground_color, relief="flat", text="Persoonlijke informatie", command=lambda: controller.show_frame(PersonalInfoPage))
        personalInfoButton.grid(row=1, column=1, padx=10, pady=10, sticky=tk.EW+tk.S)

        homeButton = tk.Button(self, height=4, text="Naar beginscherm", background=button_background_color, activebackground=button_active_background_color, foreground=button_foreground_color, activeforeground=button_foreground_color, relief="flat", command=lambda: controller.show_frame(StartPage))
        homeButton.grid(row=2, column=0, columnspan=2, sticky=tk.EW+tk.S)

class GeneralInfoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background=background_color)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(4, weight=1)
        operating_details = GetInfo()
        titleLabel = ttk.Label(self, text="NS-Fietsenstalling", font=LARGE_FONT, background=background_color).grid(row=0,pady=10, padx=10,columnspan=2)
        statusLabel = ttk.Label(self, text="Systeem status:", background=background_color).grid(row=1,column=0, sticky=tk.E)
        status2Label = ttk.Label(self, text=operating_details['system_status'], background=background_color).grid(row=1,column=1, sticky=tk.W)

        counterLabel = ttk.Label(self, text="Aantal plaatsen bezet:", background=background_color).grid(row=2,column=0, sticky=tk.E)
        counter2Label = ttk.Label(self, text=str(operating_details['counter'])+" / " + str(operating_details['total_places']), background=background_color).grid(row=2,column=1, sticky=tk.W)

        copyright = ttk.Label(self, text="Gemaakt door Sjoerd, Max, Hidde, Vincent en Tristan", background=background_color).grid(row=3,column=0, pady=20, columnspan=2)

        homeButton = tk.Button(self, height=4, text="Naar beginscherm", background=button_background_color, activebackground=button_active_background_color, foreground=button_foreground_color, activeforeground=button_foreground_color, relief="flat", command=lambda: controller.show_frame(StartPage))
        homeButton.grid(row=4, column=0, columnspan=2, sticky=tk.EW+tk.S)

class PersonalInfoDisplayer(tk.Frame):

    def __init__(self, parent, controller,code,bday):
        tk.Frame.__init__(self, parent)

        code_text = code.get("1.0",tk.END)[:-1]
        bday_text = bday.get("1.0",tk.END)[:-1]
        bday.delete("1.0",tk.END)
        code.delete("1.0",tk.END)
        details = GetUserInfo(code_text,bday_text)
        print(details)
        if len(details) == 0:
            messagebox.showerror("Ongeldig", message="Ongeldige code / geboortedatum combinatie")
            controller.show_frame(StartPage)
        else:
            print("Fissa!!")
            self.configure(background=background_color)
            self.grid_columnconfigure(0, weight=1)
            self.grid_columnconfigure(1, weight=1)
            self.grid_rowconfigure(6, weight=1)
            titleLabel = ttk.Label(self, text="NS-Fietsenstalling", font=LARGE_FONT, background=background_color)
            titleLabel.grid(row=0,pady=10, padx=10,columnspan=2)

            nameLabel = ttk.Label(self, text="Uw naam:", background=background_color).grid(row=1,column=0, sticky=tk.E)
            name = ttk.Label(self, text=details[1], background=background_color).grid(row=1,column=1, sticky=tk.W)

            phoneLabel = ttk.Label(self, text="Uw telefoonnummer:", background=background_color).grid(row=2,column=0, sticky=tk.E)
            phone = ttk.Label(self, text=details[2], background=background_color).grid(row=2,column=1, sticky=tk.W)

            sexLabel = ttk.Label(self, text="Uw geslacht:", background=background_color).grid(row=3,column=0, sticky=tk.E)
            if details[3]:
                sexval = "man"
            else:
                sexval = "vrouw"
            sex = ttk.Label(self, text=sexval, background=background_color).grid(row=3,column=1, sticky=tk.W)

            bdayLabel = ttk.Label(self, text="Uw geboortedatum:", background=background_color).grid(row=4,column=0, sticky=tk.E)
            bdayText = ttk.Label(self, text=details[4], background=background_color).grid(row=4,column=1, sticky=tk.W)

            bdayLabel = ttk.Label(self, text="Uw fietscode:", background=background_color).grid(row=5,column=0, sticky=tk.E)
            bdayText = ttk.Label(self, text=str(details[5]), background=background_color).grid(row=5,column=1, sticky=tk.W)

            homeButton = tk.Button(self, height=4, text="Naar beginscherm", background=button_background_color, activebackground=button_active_background_color, foreground=button_foreground_color, activeforeground=button_foreground_color, relief="flat", command=lambda: controller.show_frame(StartPage))
            homeButton.grid(row=6, column=0, columnspan=2, sticky=tk.EW+tk.S)


class PersonalInfoPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background=background_color)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(5, weight=1)

        titleLabel = ttk.Label(self, text="NS-Fietsenstalling", font=LARGE_FONT, background=background_color).grid(row=0,pady=10, padx=10,columnspan=2)

        codeLabel = ttk.Label(self, text="Uw unieke nummer (ex. 6658469):", background=background_color)
        codeLabel.grid(row=1,column=0, sticky=tk.E)
        code = tk.Text(self, height=1, width=15)
        code.grid(row=1,pady=10, padx=10,column=1, sticky=tk.W)
        bdayLabel = ttk.Label(self, text="Uw geboortedatum (ex. 15-04-1998):", background=background_color)
        bdayLabel.grid(row=2,column=0, sticky=tk.E)
        bday = tk.Text(self, height=1, width=15)
        bday.grid(row=2,pady=10, padx=10,column=1, sticky=tk.W)

        homeButton = tk.Button(self, height=4, text="Naar beginscherm", background=button_background_color, activebackground=button_active_background_color, foreground=button_foreground_color, activeforeground=button_foreground_color, relief="flat", command=lambda: controller.show_frame(StartPage))
        homeButton.grid(row=5, column=0, columnspan=2, sticky=tk.EW+tk.S)

        infoButton = tk.Button(self, height=4, width=30, text="Bekijk info", background=button_background_color, activebackground=button_active_background_color, foreground=button_foreground_color, activeforeground=button_foreground_color, relief="flat", command=lambda: controller.showDisplayFrame(code,bday))
        infoButton.grid(row=3, column=0, columnspan=2, pady=30)

app = NSFietsenstalling()
app.mainloop()
