import os
from tkinter import Tk, Menu, filedialog, messagebox
from tkinter.ttk import Notebook

import yaml

from editor import OptionFile, Kit, Player
from editor import common_functions

from gui import ClubTab, LogosTab, ShopTab, StadiumLeagueTab, PlayersTab
from .config import Config


class Gui(Tk):
    appname="PES/WE/J League OF Team Editor 2006-2010"
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
        load_default = False
        try:
            with open(os.getcwd() + "/OTE_Settings.yaml") as stream:
                self.settings_file = yaml.safe_load(stream)
                print(self.settings_file.get('Last Config File Used'))
                self.my_config = Config(self.settings_file.get('Last Config File Used'))
        except FileNotFoundError:
            load_default = True
            pass
        if load_default:
            try:
                self.create_config()
            except FileNotFoundError as e:
                messagebox.showerror(title=self.appname, message=f"No config files found code error {e}")
                self.destroy()

        self.my_menu=Menu(self.master)
        self.config(menu=self.my_menu)
        self.file_menu = Menu(self.my_menu, tearoff=0)
        self.edit_menu = Menu(self.my_menu, tearoff=0)
        self.help_menu = Menu(self.my_menu, tearoff=0)

        self.my_menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open)
        self.file_menu.add_command(label="Save", state='disabled',command=self.save_btn_action)
        self.file_menu.add_command(label="Save as...", state='disabled', command=self.save_as_btn_action)
        self.file_menu.add_command(label="Save as OF decrypted", state='disabled',command=self.save_of_decrypted_btn_action)
        self.file_menu.add_command(label="Exit", command= lambda : self.stop())

        self.my_menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Export to CSV", state='disabled', command=None)
        self.edit_menu.add_command(label="Import from CSV", state='disabled', command=None)
        self.edit_menu.add_command(label="Convert OF to DB (Experimental)", state='disabled', command=self.convert_of_to_db)
        self.edit_submenu = Menu(self.my_menu, tearoff=0)
        # Dinamically loading game versions as sub menu
        for i in range(len(self.my_config.games_config)):
            self.edit_submenu.add_command(label=self.my_config.games_config[i],command= lambda i=i: self.change_config(self.my_config.filelist[i]))
        self.edit_menu.add_cascade(label="Game Version", menu=self.edit_submenu)

        self.my_menu.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="Manual", command=self.manual)
        self.help_menu.add_command(label="About", command=self.about)
        game_ver = self.my_config.file["Gui"]["Game Name"]
        self.title(f"{self.appname} Version: {game_ver}")
        self.tabs_container=Notebook(self)
        self.protocol('WM_DELETE_WINDOW', self.stop)


    def create_config(self):
        self.my_config = Config()

    def change_config(self, file):
        self.my_config = Config(file)
        game_ver = self.my_config.file["Gui"]["Game Name"]
        self.title(f"{self.appname} Version: {game_ver}")
        self.tabs_container.destroy()
        self.of = None
        self.file_menu.entryconfig("Save", state="disabled")
        self.file_menu.entryconfig("Save as...", state="disabled")
        self.file_menu.entryconfig("Save as OF decrypted", state="disabled")
        #self.edit_menu.entryconfig("Export to CSV", state="disabled")
        #self.edit_menu.entryconfig("Import from CSV", state="disabled")
        self.edit_menu.entryconfig("Convert OF to DB (Experimental)", state="disabled")
        self.tabs_container=Notebook(self)

        #self.refresh_gui()


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
            ("PES/WE/JL PS2 Option File", ".psu .xps"),
            ('All files', '*.*'),
        ]

        filename = filedialog.askopenfilename(
            title=f'{self.appname} Select your option file',
            initialdir='.',
            filetypes=filetypes)
        if filename == "":
            return 0
        #isencrypted = messagebox.askyesno(title=self.appname, message="Is your option file encrypted?")
        if self.of == None:
            self.of = OptionFile(filename,self.my_config.file)
        else:
            old_of = self.of
            try:
                self.of = OptionFile(filename,self.my_config.file)
            except Exception as e:
                self.of = old_of
                messagebox.showerror(
                    self.appname,
                    f"Fail to open new option file, previous option file restore, code error: {e}"
                )
        """
        try :
            f = open("./test/we2007.bin","wb")
            f.write(self.of.data)
            f.close()
            print("of desencriptado guardado")
        except Exception as e:
            print(e)
        """
        self.reload_gui_items()

    def reload_gui_items(self):
        """
        Refresh the whole gui once there's an update in one of the elements such as a new afl file or any file name change, etc

        Args:
            item_idx (int, optional): optional parameter, in case you need to keep the current selection on the listbox after the update
        """
        self.file_menu.entryconfig("Save", state="normal")
        self.file_menu.entryconfig("Save as...", state="normal")
        self.file_menu.entryconfig("Save as OF decrypted", state="normal")
        #self.edit_menu.entryconfig("Export to CSV", state="normal")
        #self.edit_menu.entryconfig("Import from CSV", state="normal")
        self.edit_menu.entryconfig("Convert OF to DB (Experimental)", state="normal")
        self.tabs_container.destroy()
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
            new_location = filedialog.asksaveasfile(initialdir=".",title=self.appname, mode='wb', filetypes=([("All files", "*")]), defaultextension=f"{self.of.extension}")
            if new_location is None:
                return 0
            self.of.save_option_file(new_location.name)
            messagebox.showinfo(title=self.appname,message=f"All changes saved at {self.of.file_location}")
        except EnvironmentError as e: # parent of IOError, OSError *and* WindowsError where available
            messagebox.showerror(title=self.appname,message=f"Error while saving, error type={e}, try running as admin or saving into another location")

    def save_of_decrypted_btn_action(self):
        try:
            new_location = filedialog.asksaveasfile(initialdir=".",title=self.appname, mode='wb', filetypes=([("All files", "*")]), defaultextension=f"{self.of.extension}")
            if new_location is None:
                return 0
            self.of.encrypted = False
            self.of.save_option_file(new_location.name)
            self.of.encrypted = self.my_config.file['option_file_data']['ENCRYPTED']
            messagebox.showinfo(title=self.appname,message=f"All changes saved at {self.of.file_location}")
        except EnvironmentError as e: # parent of IOError, OSError *and* WindowsError where available
            messagebox.showerror(title=self.appname,message=f"Error while saving, error type={e}, try running as admin or saving into another location")

    def convert_of_to_db(self):
        try:
            folder_selected = filedialog.askdirectory(initialdir=".",title=self.appname, )
            if folder_selected == "":
                return
            players_file = open(folder_selected + "/db.bin_000", "wb")
            for i in range(Player.first_unused):
                players_file.write(self.of.data[self.of.players[i].address : self.of.players[i].address + Player.size])
            players_file.close()
            kits_sub_bin_counter = 0
            kits_sub_bin_0 = open(folder_selected + f"/kits.bin_00{kits_sub_bin_counter}", "wb")
            if Kit.size_nation > 0:
                # this should be done in the future when there is more work done in the editor
                kits_sub_bin_0.close()
                return
            else:
                for i in range(Kit.total):
                    kits_sub_bin_0.write(self.of.data[Kit.start_address + (i * Kit.size_club) : Kit.start_address + (i * Kit.size_club) + Kit.size_club])
            kits_sub_bin_0.close()

            messagebox.showinfo(title=self.appname,message=f"All changes saved at {folder_selected}")
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

    def save_settings(self):
        settings_file_name = os.getcwd() + "/OTE_Settings.yaml"
        
        dict_file = {
            'Last Config File Used' : self.my_config.file_location
        }

        settings_file = open(settings_file_name, "w")
        yaml.dump(dict_file, settings_file)
        settings_file.close()

    def start(self):
        self.resizable(False, False)
        self.mainloop()

    def stop(self):
        self.save_settings()
        self.quit()
        self.destroy()



w = 800 # width for the Tk root
h = 600 # height for the Tk root
