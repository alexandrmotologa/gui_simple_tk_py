import tkinter as tk
import json
import requests
from tkinter import messagebox
from tkinter import Menu


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()

        menu = Menu(root)
        new_item = Menu(menu, tearoff=0)
        new_item.add_command(label='Exit', command=self.master.destroy)
        menu.add_cascade(label='Option', menu=new_item)
        root.config(menu=menu)

        self.hello_label = tk.Label(root, text="Welcome to IP INFO APP!", font =('arial', 16, 'bold'), fg='green', bg='#10a0bc', relief='solid', width=38, height=3)
        self.hello_label.grid(row=0,column=0, columnspan=3)
        self.lbl = tk.Label(root, text="Enter an IP or DOMAIN name")
        self.lbl.grid(column=0, row=1)
        self.inp_main = tk.Entry(root, width=35)
        self.inp_main.grid(column=1, row=1)
        self.inp_main.focus()
        self.btn = tk.Button(root, text="Search!", command=self.inputDomain)
        self.btn.grid(column=2, row=1)
        self.result =tk.Label(root, font=('arial', 10, 'bold'), fg='darkblue')
        self.result.grid(column=0, row=2,columnspan=3)
        self.all_info = tk.Label(root)
        self.all_info.grid(column=0, row=3, columnspan=3, pady=20)

    def clearAllInfo(self):
        try:
            self.all_info['text'] = ""
            self.result['text'] = ""
            self.clear_btn.destroy()
        except :
            pass

    def inputDomain(self):
        query = self.inp_main.get()
        if len(query.strip()) == 0:
            messagebox.showerror("Error", "Error... Try Again... ENTER IP or DOMAIN name")
            self.inp_main.delete(first=0, last=100)
            self.clearAllInfo()

        if len(query.strip()) != 0:
            endpoint = f"http://ip-api.com/json/{query}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,zip,lat,lon,timezone,currency,isp,org,as,query"
            response = requests.get(endpoint)
            data = json.loads(response.text)
            r = (f"Your enter :  {query}, with IP: {data['query']}")
            self.result['text'] = str(r)
            self.inp_main.delete(first=0,last=100)

            if data['status'] == 'success':
                dom_ip =( f"\nThe domain is located in {data['continent']} / {data['country']} [{data['countryCode']}],\n\
                \rRegion/State: {data['regionName']} / City: {data['city']},\n\
                \rLatitude of {data['city']}: {data['lat']} and Longitude of {data['city']}: {data['lon']}\n\
                \rNational currency: {data['currency']}\n\
                \rInternet service provider: {data['isp']}\n\
                \rOrganisation: {data['org']},\n\
                \rNumber and Organisation: {data['as']}\n\
                \rIP: {data['query']}")
                self.all_info['text'] = str(dom_ip)
                self.clear_btn = tk.Button(root, text="Clear Info!", fg="red", command=self.clearAllInfo)
                self.clear_btn.grid(column=2, row=4, columnspan=2)

            else:
                messagebox.showerror("Error", "Error... Try Again... ENTER IP or DOMAIN name")
                self.inp_main.delete(first=0, last=100)
                self.clearAllInfo()


root = tk.Tk()
root.geometry('500x500+700+200')
root.title("IP INFO")
app = Application(master=root)
app.mainloop()
