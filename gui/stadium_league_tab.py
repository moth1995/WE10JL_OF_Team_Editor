from tkinter import Entry, Frame, Label, messagebox, Listbox

from gui.club_tab import ClubTab

class StadiumLeagueTab(Frame):
    def __init__(self, master, option_file, w, h, appname):
        super().__init__(master,width=w,height=h)
        self.of = option_file
        self.appname = appname
        self.stadiums_lbl = Label(self, text="Insert the new stadium name")
        self.stadiums_box = Entry(self, width=30)
        self.stadiums_box.bind('<Return>', lambda event: self.stadium_set_name())
        self.stadiums_list_box = Listbox(self, height = 30, width = 30, exportselection=False)
        self.stadiums_list_box.selectedindex = 0
        self.stadiums_list_box.bind('<<ListboxSelect>>',lambda event: self.set_stadium_box())
        self.stadiums_list_box.insert('end',*[stadium.name for stadium in self.of.stadiums])

        self.leagues_lbl = Label(self, text="Insert the new league name")
        self.leagues_box = Entry(self, width=30)
        self.leagues_box.bind('<Return>', lambda event: self.league_set_name())
        self.leagues_list_box = Listbox(self, height = 30, width = 30, exportselection=False)
        self.leagues_list_box.selectedindex = 0
        self.leagues_list_box.bind('<<ListboxSelect>>',lambda event: self.set_leagues_box())
        self.leagues_list_box.insert('end',*self.of.leagues_names)

    def league_set_name(self):
        try:
            lg_new_name = self.leagues_box.get()
            league_id = self.leagues_list_box.get(0, "end").index(self.leagues_list_box.get(self.leagues_list_box.curselection()))
            self.of.leagues[league_id].set_name(lg_new_name)
            
            self.leagues_list_box.delete(0,'end')
            self.leagues_list_box.insert('end',*self.of.leagues_names)
            
            messagebox.showinfo(title=self.appname,message="League name changed correctly")
        except ValueError as e:
            messagebox.showerror(title=self.appname,message=e)


    def set_leagues_box(self):
        self.leagues_box.delete(0,'end')
        self.leagues_box.insert(0,self.leagues_list_box.get(self.leagues_list_box.curselection()))

    def stadium_set_name(self):
        try:
            std_new_name = self.stadiums_box.get()
            stadium_id = self.stadiums_list_box.get(0, "end").index(self.stadiums_list_box.get(self.stadiums_list_box.curselection()))
            self.of.stadiums[stadium_id].set_name(std_new_name)
            self.stadiums_list_box.delete(0,'end')
            self.stadiums_list_box.insert('end',*self.of.stadiums_names)
            messagebox.showinfo(title=self.appname,message="Stadium name changed correctly")
        except ValueError as e:
            messagebox.showerror(title=self.appname,message=e)

    def set_stadium_box(self):
        self.stadiums_box.delete(0,'end')
        self.stadiums_box.insert(0,self.stadiums_list_box.get(self.stadiums_list_box.curselection()))


    def publish(self):
        self.stadiums_lbl.place(x=205, y=20)
        self.stadiums_box.place(x=205, y=50)
        self.stadiums_list_box.place(x=5, y=20)
        self.leagues_lbl.place(x=600, y=20)
        self.leagues_box.place(x=600, y=50)
        self.leagues_list_box.place(x=405, y=20)
        