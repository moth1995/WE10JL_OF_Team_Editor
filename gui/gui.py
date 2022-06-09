from tkinter import Tk, Menu, filedialog, messagebox
from tkinter.ttk import Notebook

from editor import OptionFile, common_functions

from gui import ClubTab, LogosTab, ShopTab, StadiumLeagueTab, PlayersTab

class Gui(Tk):
    appname="J League WE10 OF Team Editor"
    report_callback_exception = common_functions.report_callback_exception
    of = None
    def __init__(self):
        Tk.__init__(self)
        self.title(self.appname)
        # get screen width and height
        ws = self.winfo_screenwidth() # width of the screen
        hs = self.winfo_screenheight() # height of the screen
        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        # set the dimensions of the screen 
        # and where it is placed
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.my_menu=Menu(self.master)
        self.config(menu=self.my_menu)
        self.file_menu = Menu(self.my_menu, tearoff=0)
        self.edit_menu = Menu(self.my_menu, tearoff=0)
        self.help_menu = Menu(self.my_menu, tearoff=0)

        self.my_menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open)
        self.file_menu.add_command(label="Save", state='disabled',command=self.save_btn_action)
        self.file_menu.add_command(label="Save as...", state='disabled', command=self.save_as_btn_action)
        self.file_menu.add_command(label="Exit", command= lambda : self.destroy())

        self.my_menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Export to CSV", state='disabled', command=None)
        self.edit_menu.add_command(label="Import from CSV", state='disabled', command=None)

        self.my_menu.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="Manual", command=self.manual)
        self.help_menu.add_command(label="About", command=self.about)

    def publish(self):
        """
        Method to expose the gui into the form
        """
        # Players tab placing
        
        self.players_tab.publish()

        # Clubs tab placing

        self.clubs_tab.publish()

        # Stadium Leagues tab placing

        self.stadium_league_tab.publish()

        # Shop tab placing

        self.shop_tab.publish()

        #Placing tabs and container in the root

        self.tabs_container.pack()
        self.clubs_tab.pack(fill="both", expand=1)
        self.stadium_league_tab.pack(fill="both", expand=1)
        self.shop_tab.pack(fill="both", expand=1)

        self.tabs_container.add(self.players_tab, text="Players")
        self.tabs_container.add(self.clubs_tab, text="Clubs")
        self.tabs_container.add(self.stadium_league_tab, text="Stadiums & Leagues")
        self.tabs_container.add(self.logos_tab, text="Logos")
        self.tabs_container.add(self.shop_tab, text="Shop")

        self.tabs_container.bind('<<NotebookTabChanged>>', self.on_tab_change)

    def on_tab_change(self,event):
        tab = event.widget.tab('current')['text']
        if tab == 'Clubs':
            self.clubs_tab.refresh_gui()
        #elif tab == 'Swap Teams' or tab == 'Export/Import CSV' or tab == 'Extra':
            #refresh_gui()


    def open(self):
        """
        Shows the user an interactive menu to select their afl file and then update the whole gui
        enabling widgets

        Returns:
            Bolean: Returns False if the user hits the "cancel" button, otherwise does their actions
        """
        filetypes = [
            ("JL WE10 PS2 Option File", ".psu .xps"),
            ('All files', '*.*'),
        ]

        filename = filedialog.askopenfilename(
            title=f'{self.appname} Select your option file',
            initialdir='.',
            filetypes=filetypes)
        if filename == "":
            return 0
        isencrypted = messagebox.askyesno(title=self.appname, message="Is your option file encrypted?")
        if self.of == None:
            self.of = OptionFile(filename,isencrypted)
        else:
            old_of = self.of
            try:
                self.of = OptionFile(filename,isencrypted)
            except Exception as e:
                self.of = old_of
                messagebox.showerror(
                    self.appname,
                    f"Fail to open new option file, previous option file restore, code error: {e}"
                )
        self.reload_gui_items()

    def reload_gui_items(self):
        """
        Refresh the whole gui once there's an update in one of the elements such as a new afl file or any file name change, etc

        Args:
            item_idx (int, optional): optional parameter, in case you need to keep the current selection on the listbox after the update
        """
        self.file_menu.entryconfig("Save", state="normal")
        self.file_menu.entryconfig("Save as...", state="normal")
        #self.edit_menu.entryconfig("Export to CSV", state="normal")
        #self.edit_menu.entryconfig("Import from CSV", state="normal")
        self.tabs_container=Notebook(self)
        self.players_tab = PlayersTab(self.tabs_container,self.of, w, h, self.appname)
        self.clubs_tab = ClubTab(self.tabs_container,self.of, w, h, self.appname)
        self.stadium_league_tab = StadiumLeagueTab(self.tabs_container,self.of, w, h, self.appname)
        self.logos_tab = LogosTab(self.tabs_container,self.of, w, h, self.appname)
        self.shop_tab = ShopTab(self.tabs_container,self.of, w, h, self.appname)
        self.publish()



    def save_btn_action(self):
        try:
            #call the object method save_file
            self.of.save_option_file()
            messagebox.showinfo(title=self.appname,message=f"All changes saved at {self.of.file_location}")
        except EnvironmentError as e: # parent of IOError, OSError *and* WindowsError where available
            messagebox.showerror(title=self.appname,message=f"Error while saving, error type={e}, try running as admin")

    def save_as_btn_action(self):
        try:
            new_location = filedialog.asksaveasfile(initialdir=".",title=self.appname, mode='wb', filetypes=([("All files", "*")]), defaultextension=f".{self.object.file_extension}")
            if new_location is None:
                return 0
            self.of.save_option_file(new_location)
            messagebox.showinfo(title=self.appname,message=f"All changes saved at {self.of.file_location}")
        except EnvironmentError as e: # parent of IOError, OSError *and* WindowsError where available
            messagebox.showerror(title=self.appname,message=f"Error while saving, error type={e}, try running as admin or saving into another location")


    def about(self):
        messagebox.showinfo(title=self.appname,message=
        """
        Thanks to PeterC10 for python de/encrypt code for OF,
        Yerry11 for png import/export, 
        Aurelio José Parra Morales for players nationalities.
        """.replace('        ', ''))

    def manual(self):
        messagebox.showinfo(title=self.appname,message=
        r"""
        Write here some manual to your tool
        """.replace('        ', ''))

    def start(self):
        self.resizable(False, False)
        self.mainloop()

w = 800 # width for the Tk root
h = 600 # height for the Tk root
