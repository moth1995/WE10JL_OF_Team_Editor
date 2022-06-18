from tkinter import Button,  Frame, Label, Listbox, Scrollbar
from tkinter.ttk import Combobox

from editor import OptionFile, Player, common_functions
from .player_stats_window import PlayerStatsWindow

class PlayersTab(Frame):

    order_by_name = False

    def __init__(self, master, option_file:OptionFile, w, h, appname):
        super().__init__(master,width=w,height=h)
        self.of = option_file
        self.appname = appname
        self.player_filter_list = self.of.nations + ["Shop", "ML Youth", "ML Old", "Unused Players", "Edited Players", "All Players"]
        self.players_filter_combobox = Combobox(self, state="readonly", value=self.player_filter_list, width=30)
        self.players_filter_combobox.set("All Players")
        self.players_filter_combobox.bind(
            '<<ComboboxSelected>>', 
            lambda event: self.apply_player_filter()
        )
        self.players_filter_combobox.bind(
            '<Key>', 
            lambda event: common_functions.find_in_combobox(
                event,
                self.players_filter_combobox,
                self.players_filter_combobox["values"],
            )
        )

        self.players_list_box = Listbox(self, height = 31, width = 30, exportselection=False)
        self.players_list_box.bind('<Double-1>',lambda event: self.on_lb_double_click())
        self.players_list_box.bind('<<ListboxSelect>>',lambda event: self.on_lb_click())
        self.players_list_box_sb = Scrollbar(self.master, orient="vertical") 
        self.players_list_box_sb.config(command = self.players_list_box.yview)
        self.players_list_box.config(yscrollcommand = self.players_list_box_sb.set)
        # Loading all players into the listbox
        self.apply_player_filter()

        self.order_by_name_button = Button(
            self, 
            text="Order by A-Z", 
            command=lambda: self.on_order_by_clic()
        )

        self.player_info_label = Label(
            self, 
            text="", 
            width=30, 
            height=50, 
            anchor="nw",
            justify="left",
            background="black", 
            foreground="white",
        )

        #self.bind("<Motion>", lambda e: self.find_widget_placing(e, self.order_by_name_button))

    def on_lb_double_click(self):
        """
        Creates a new window showing selected player attributes
        """
        if len(self.players_list_box.curselection()) == 0:
            return
        item_idx = self.players_list_box.get(0, "end").index(self.players_list_box.get(self.players_list_box.curselection()))
        player = self.of.get_player_by_name(self.players_list_box.get(self.players_list_box.curselection()))
        psw = PlayerStatsWindow(self, player, self.of.nations)
        psw.mainloop()
        self.of.set_players_names()
        self.of.set_edited_players_names()
        self.players_list_box.delete(item_idx,item_idx)
        self.players_list_box.insert(item_idx, player.name)
        self.players_list_box.select_set(item_idx)


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
        elif filter_selected in self.of.nations:
            player_list = [
                self.of.players[i].name 
                for i in range(1, len(self.of.players)) 
                if self.of.players[i].nation() == filter_selected
            ] + [
                self.of.edited_players[i].name
                for i in range(len(self.of.edited_players))
                if self.of.edited_players[i].nation() == filter_selected
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
        if len(self.players_list_box.curselection()) == 0:
            return

        #item_idx = self.players_list_box.get(0, "end").index(self.players_list_box.get(self.players_list_box.curselection())) + 1
        player = self.of.get_player_by_name(self.players_list_box.get(self.players_list_box.curselection()))
        #print(f"player id antes de la condicion: {player_id}")
        #print(player_id)
        player_info = f"""Player id: {player.idx} 
        
        Name: {player.name}
        
        Shirt Name: {player.shirt_name} 
        
        Nationality: {player.nation()}

        Age: {player.basic_settings.age()}

        """.replace("        ", "")
        self.player_info_label.config(text=player_info)

    def publish(self):
        self.players_list_box.place(x = 5, y = 30)
        self.players_list_box_sb.place(x = 190, y =52.5 , height = 500)
        self.player_info_label.place(x = 210, y = 30)
        self.players_filter_combobox.place(x = 5, y = 5)
        self.order_by_name_button.place(x = 70, y = 544)















