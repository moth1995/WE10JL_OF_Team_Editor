from tkinter import Button, Entry, Frame, Label, Toplevel, messagebox, Listbox,Scrollbar
from tkinter.ttk import Combobox

from editor import OptionFile, Player, common_functions, nations

class PlayersTab(Frame):

    order_by_name = False
    player_filter_list = nations + ["Shop", "ML Youth", "ML Old", "Unused Players", "Edited Players", "All Players"]

    def __init__(self, master, option_file:OptionFile, w, h, appname):
        super().__init__(master,width=w,height=h)
        self.of = option_file
        self.appname = appname
        self.players_filter_combobox = Combobox(self, state="readonly", value=self.player_filter_list, width=30)
        self.players_filter_combobox.current(len(self.player_filter_list)-1)
        self.players_filter_combobox.bind('<<ComboboxSelected>>', lambda event: self.apply_player_filter())
        self.players_filter_combobox.bind('<Key>', lambda event: common_functions.find_in_combobox(event,self.players_filter_combobox, self.players_filter_combobox["values"]))

        self.players_list_box = Listbox(self, height = 31, width = 30, exportselection=False)
        self.players_list_box.bind('<Double-1>',lambda event: self.on_lb_double_click())
        self.players_list_box.bind('<<ListboxSelect>>',lambda event: self.on_lb_click())
        self.players_list_box_sb = Scrollbar(self.master, orient="vertical") 
        self.players_list_box_sb.config(command = self.players_list_box.yview)
        self.players_list_box.config(yscrollcommand = self.players_list_box_sb.set)
        # Loading all players into the listbox
        self.apply_player_filter()
        #self.bind("<Motion>", lambda e: self.find_widget_placing(e, self.order_by_name_button))
        self.order_by_name_button = Button(
            self, 
            text="Order by A-Z", 
            command=lambda: self.on_order_by_clic()
        )

        self.player_info_label = Label(
            self, 
            text="", 
            width=20, 
            height=50, 
            anchor="nw",
            justify="left",
            background="black", 
            foreground="white",
        )

    def find_widget_placing(self, e, widget):

        widget.place(x=e.x,y=e.y)
        print(f"{e.x},{e.y}")

    def apply_player_filter(self):
        filter_selected = self.players_filter_combobox.get()
        if filter_selected == self.player_filter_list[-1]:
            player_list = [self.of.players[i].name for i in range(1, len(self.of.players))] + [self.of.edited_players[i].name for i in range(len(self.of.edited_players))]
        elif filter_selected == self.player_filter_list[-2]:
            player_list = [self.of.edited_players[i].name for i in range(len(self.of.edited_players))]
        elif filter_selected == self.player_filter_list[-3]:
            player_list = [self.of.players[i].name for i in range(Player.first_unused, len(self.of.players))]
        elif filter_selected == self.player_filter_list[-4]:
            player_list = [self.of.players[i].name for i in range(Player.first_ml_old, Player.first_unused)]
        elif filter_selected == self.player_filter_list[-5]:
            player_list = [self.of.players[i].name for i in range(Player.first_ml_youth, Player.first_ml_old)]
        elif filter_selected == self.player_filter_list[-6]:
            player_list = [self.of.players[i].name for i in range(Player.first_shop, Player.first_ml_youth)]
        elif filter_selected in nations:
            player_list = [
                self.of.players[i].name 
                for i in range(1, len(self.of.players)) 
                if self.of.players[i].nation() == filter_selected
            ] + [
                self.of.edited_players[i].name
                for i in range(len(self.of.edited_players))
                if self.of.players[i].nation() == filter_selected
            ]
        else:
            player_list = []
        if self.order_by_name: player_list.sort()
        self.players_list_box.delete(0,'end')
        self.players_list_box.insert('end',*player_list)

    def on_order_by_clic(self):
        self.order_by_name = False if self.order_by_name else True
        self.order_by_name_button['text'] = 'Order by ID' if self.order_by_name else 'Order by A-Z'
        self.apply_player_filter()

    def on_lb_click(self):
        """
        Display player info at the black label
        """
        #item_idx = self.players_list_box.get(0, "end").index(self.players_list_box.get(self.players_list_box.curselection())) + 1
        player_id = self.of.get_player_idx_by_name(self.players_list_box.get(self.players_list_box.curselection()))
        #print(f"player id antes de la condicion: {player_id}")
        if player_id < Player.first_edited_id:
            temp_list_player = self.of.players
        else:
            player_id = player_id - Player.first_edited_id
            temp_list_player =self.of.edited_players
        #print(player_id)
        player_info = f"""Player id: {temp_list_player[player_id].idx} 
        
        Name: {temp_list_player[player_id].name}
        
        Shirt Name: {temp_list_player[player_id].shirt_name} 
        
        Nationality: {temp_list_player[player_id].nation()}

        Age: {temp_list_player[player_id].age()}
        """.replace("        ", "")
        self.player_info_label.config(text=player_info)
        

    def on_lb_double_click(self):
        """
        Creates a new window showing selected player attributes
        """
        item_idx = self.players_list_box.get(0, "end").index(self.players_list_box.get(self.players_list_box.curselection())) + 1
        player_id = self.of.get_player_idx_by_name(self.players_list_box.get(self.players_list_box.curselection()))
        #print(f"player id antes de la condicion: {player_id}")
        if player_id < Player.first_edited_id:
            temp_player_id = player_id
            temp_list_player = self.of.players
        else:
            temp_player_id = player_id - Player.first_edited_id
            temp_list_player =self.of.edited_players
        #print(player_id)

        self.window = Toplevel(self)
        w = 500 # width for the Tk root
        h = 500 # height for the Tk root
        ws = self.window.winfo_screenwidth() # width of the screen
        hs = self.window.winfo_screenheight() # height of the screen
        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        # set the dimensions of the screen 
        # and where it is placed
        self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.player_name_entry = Entry(self.window, width=30)
        self.player_name_entry.focus_force()
        self.player_name_entry.delete(0,'end')
        self.player_name_entry.insert(0,temp_list_player[temp_player_id].name)
        self.player_name_entry.pack()
        self.player_shirt_name_entry = Entry(self.window, width=30)
        self.player_shirt_name_entry.delete(0,'end')
        self.player_shirt_name_entry.insert(0,temp_list_player[temp_player_id].shirt_name)
        self.player_shirt_name_entry.pack()
        self.player_age_entry = Entry(self.window, width=30)
        self.player_age_entry.delete(0,'end')
        self.player_age_entry.insert(0,temp_list_player[temp_player_id].age())
        self.player_age_entry.pack()
        self.apply_button = Button(self.window, text="Apply", command=lambda: self.update_player_data(item_idx, player_id))
        self.apply_button.pack()
        self.cancel_button = Button(self.window, text="Cancel", command=lambda :self.window.destroy())
        self.cancel_button.pack()
        self.window.lift()
        self.window.grab_set()
        self.window.resizable(False, False)
        self.window.mainloop()
        
    def update_player_data(self,idx, player_id):
        if player_id < Player.first_edited_id:
            temp_player_id = player_id
            temp_list_player = self.of.players[:]
        else:
            temp_player_id = player_id - Player.first_edited_id
            temp_list_player =self.of.edited_players[:]

        temp_list_player[temp_player_id].name = self.player_name_entry.get()
        temp_list_player[temp_player_id].shirt_name = self.player_shirt_name_entry.get()
        temp_list_player[temp_player_id].age.set_value(common_functions.intTryParse(self.player_age_entry.get()))

        if player_id < Player.first_edited_id:
            self.of.players.clear()
            self.of.players = temp_list_player[:]
            self.of.set_players_names()
        else:
            self.of.edited_players.clear()
            self.of.edited_players = temp_list_player[:]
            self.of.set_edited_players_names()
        
        self.refresh_gui(idx)
        self.window.destroy()

    def refresh_gui(self,item_idx=None):
        """
        Updates every gui element that use the playerlist 
        """
        self.apply_player_filter()
        if item_idx!=None:
            # After we clic on the button we lost the item selection so with this we solve it
            self.players_list_box.select_set(item_idx)

    def publish(self):
        self.players_list_box.place(x=5, y=30)
        self.players_list_box_sb.place(x=190, y=52.5, height=500)
        self.player_info_label.place(x=210, y=30)
        self.players_filter_combobox.place(x=5, y=5)
        self.order_by_name_button.place(x=70,y=544)















