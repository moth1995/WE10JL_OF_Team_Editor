from tkinter import Button, Checkbutton, Entry, IntVar, Label, Spinbox, Toplevel
from tkinter.ttk import Combobox

from editor import Player, common_functions
from .paste_psd import paste_psd

class PlayerStatsWindow(Toplevel):

    def __init__(self, master, player:Player, nations):
        Toplevel.__init__(self, master)
        w = 850 # width for the Tk root
        h = 750 # height for the Tk root
        ws = self.winfo_screenwidth() # width of the screen
        hs = self.winfo_screenheight() # height of the screen
        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        # set the dimensions of the screen 
        # and where it is placed
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.player_idx_label = Label(self, text="Player ID")
        self.player_idx_label.grid(row=0, column=0, sticky="e")
        self.player_idx_entry = Entry(self, width=6)
        self.player_idx_entry.delete(0,'end')
        self.player_idx_entry.insert(0,player.idx)
        self.player_idx_entry.configure(state="disabled")
        self.player_idx_entry.grid(row=0, column=1, sticky="w")

        self.player_name_label = Label(self, text="Player Name")
        self.player_name_label.grid(row=1, column=0, sticky="e")
        self.player_name_entry = Entry(self, width=20)
        self.player_name_entry.focus_force()
        self.player_name_entry.delete(0,'end')
        self.player_name_entry.insert(0,player.name)
        self.player_name_entry.grid(row=1, column=1, sticky="w")

        self.player_shirt_name_label = Label(self, text="Player Shirt Name")
        self.player_shirt_name_label.grid(row=2, column=0, sticky="e")
        self.player_shirt_name_entry = Entry(self, width=20)
        self.player_shirt_name_entry.delete(0,'end')
        self.player_shirt_name_entry.insert(0,player.shirt_name)
        self.player_shirt_name_entry.grid(row=2, column=1, sticky="w")

        self.player_callname_label = Label(self, text=player.callname.name)
        self.player_callname_label.grid(row=3, column=0, sticky="e")
        self.player_callname_entry = Entry(self, width=6)
        self.player_callname_entry.delete(0,'end')
        self.player_callname_entry.insert(0,player.callname())
        self.player_callname_entry.grid(row=3, column=1, sticky="w")

        self.player_nationality_label = Label(self, text=player.nation.name)
        self.player_nationality_label.grid(row=4, column=0, sticky="e")
        self.player_nationality_combobox = Combobox(self, state="readonly", value=nations, width=20)
        self.player_nationality_combobox.set(player.nation())
        self.player_nationality_combobox.grid(row=4, column=1, sticky="w")

        self.player_age_label = Label(self, text=player.basic_settings.age.name)
        self.player_age_label.grid(row=5, column=0, sticky="e")
        self.player_age_int_var = IntVar()
        self.player_age_spinbox = Spinbox(self, from_= 15, to = 46, textvariable=self.player_age_int_var, width = 5)
        #self.player_age_spinbox.delete(0,'end')
        #self.player_age_spinbox.insert(0,player.basic_settings.age())
        self.player_age_int_var.set(player.basic_settings.age())
        self.player_age_spinbox.grid(row=5, column=1, sticky="w")

        self.player_stronger_foot_label = Label(self, text=player.basic_settings.stronger_foot.name)
        self.player_stronger_foot_label.grid(row=6, column=0, sticky="e")
        self.player_stronger_foot_combobox = Combobox(self, state="readonly", value=["R","L"], width=20)
        self.player_stronger_foot_combobox.set(player.basic_settings.stronger_foot())
        self.player_stronger_foot_combobox.grid(row=6, column=1, sticky="w")

        self.player_injury_label = Label(self, text=player.basic_settings.injury.name)
        self.player_injury_label.grid(row=7, column=0, sticky="e")
        self.player_injury_combobox = Combobox(self, state="readonly", value=["C", "B", "A",], width=20)
        self.player_injury_combobox.set(player.basic_settings.injury())
        self.player_injury_combobox.grid(row=7, column=1, sticky="w")

        self.player_style_of_dribble_label = Label(self, text=player.basic_settings.style_of_dribble.name)
        self.player_style_of_dribble_label.grid(row=8, column=0, sticky="e")
        self.player_style_of_dribble_combobox = Combobox(self, state="readonly", value=list(range(1,5)), width=20)
        self.player_style_of_dribble_combobox.set(player.basic_settings.style_of_dribble())
        self.player_style_of_dribble_combobox.grid(row=8, column=1, sticky="w")

        self.player_free_kick_type_label = Label(self, text=player.basic_settings.free_kick_type.name)
        self.player_free_kick_type_label.grid(row=9, column=0, sticky="e")
        self.player_free_kick_type_combobox = Combobox(self, state="readonly", value=list(range(1,17)), width=20)
        self.player_free_kick_type_combobox.set(player.basic_settings.free_kick_type())
        self.player_free_kick_type_combobox.grid(row=9, column=1, sticky="w")

        self.player_penalty_kick_label = Label(self, text=player.basic_settings.penalty_kick.name)
        self.player_penalty_kick_label.grid(row=10, column=0, sticky="e")
        self.player_penalty_kick_combobox = Combobox(self, state="readonly", value=list(range(1,9)), width=20)
        self.player_penalty_kick_combobox.set(player.basic_settings.penalty_kick())
        self.player_penalty_kick_combobox.grid(row=10, column=1, sticky="w")

        self.player_drop_kick_style_label = Label(self, text=player.basic_settings.drop_kick_style.name)
        self.player_drop_kick_style_label.grid(row=11, column=0, sticky="e")
        self.player_drop_kick_style_combobox = Combobox(self, state="readonly", value=list(range(1,5)), width=20)
        self.player_drop_kick_style_combobox.set(player.basic_settings.drop_kick_style())
        self.player_drop_kick_style_combobox.grid(row=11, column=1, sticky="w")

        self.player_goal_celebration_1_label = Label(self, text=player.basic_settings.goal_celebration_1.name)
        self.player_goal_celebration_1_label.grid(row=12, column=0, sticky="e")
        self.player_goal_celebration_1_combobox = Combobox(self, state="readonly", value=["No"] + list(range(1,77)), width=20)
        self.player_goal_celebration_1_combobox.current(player.basic_settings.goal_celebration_1())
        self.player_goal_celebration_1_combobox.grid(row=12, column=1, sticky="w")

        self.player_goal_celebration_2_label = Label(self, text=player.basic_settings.goal_celebration_2.name)
        self.player_goal_celebration_2_label.grid(row=13, column=0, sticky="e")
        self.player_goal_celebration_2_combobox = Combobox(self, state="readonly", value=["No"] + list(range(1,77)), width=20)
        self.player_goal_celebration_2_combobox.current(player.basic_settings.goal_celebration_2())
        self.player_goal_celebration_2_combobox.grid(row=13, column=1, sticky="w")

        self.player_growth_type_label = Label(self, text=player.basic_settings.growth_type.name)
        self.player_growth_type_label.grid(row=14, column=0, sticky="e")
        self.player_growth_type_entry = Entry(self, width=6)
        self.player_growth_type_entry.delete(0,'end')
        self.player_growth_type_entry.insert(0,player.basic_settings.growth_type())
        self.player_growth_type_entry.grid(row=14, column=1, sticky="w")

        player_appearance_label = Label(self, text="Quick Appearance Menu")
        player_appearance_label.grid(row=16, column=0, sticky="nwse", columnspan=2)

        self.player_height_label = Label(self, text=player.appearance.height.name)
        self.player_height_label.grid(row=17, column=0, sticky="e")
        self.player_height_entry = Entry(self, width=6)
        self.player_height_entry.delete(0,'end')
        self.player_height_entry.insert(0,player.appearance.height())
        self.player_height_entry.grid(row=17, column=1, sticky="w")

        self.player_weight_label = Label(self, text=player.appearance.weight.name)
        self.player_weight_label.grid(row=18, column=0, sticky="e")
        self.player_weight_entry = Entry(self, width=6)
        self.player_weight_entry.delete(0,'end')
        self.player_weight_entry.insert(0,player.appearance.weight())
        self.player_weight_entry.grid(row=18, column=1, sticky="w")

        self.player_skin_colour_label = Label(self, text=player.appearance.skin_colour.name)
        self.player_skin_colour_label.grid(row=19, column=0, sticky="e")
        self.player_skin_colour_combobox = Combobox(self, state="readonly", value=["1", "2", "3", "4",], width=20)
        self.player_skin_colour_combobox.set(player.appearance.skin_colour())
        self.player_skin_colour_combobox.grid(row=19, column=1, sticky="w")
        self.player_face_label = Label(self, text=player.appearance.face.name)
        self.player_face_label.grid(row=20, column=0, sticky="e")
        self.player_face_combobox = Combobox(self, state="readonly", value=["BUILD", "ORIGINAL", "PRESET",], width=20)
        self.player_face_combobox.set(player.appearance.face())
        self.player_face_combobox.grid(row=20, column=1, sticky="w")

        self.player_face_idx_label = Label(self, text=player.appearance.face_idx.name)
        self.player_face_idx_label.grid(row=21, column=0, sticky="e")
        self.player_face_idx_int_var = IntVar()
        self.player_face_idx_spinbox = Spinbox(self, from_= 1, to = 4096, textvariable=self.player_face_idx_int_var, width = 5)
        #self.player_face_idx_spinbox.delete(0,'end')
        #self.player_face_idx_spinbox.insert(0,player.basic_settings.age())
        self.player_face_idx_int_var.set(player.appearance.face_idx())
        self.player_face_idx_spinbox.grid(row=21, column=1, sticky="w")

        self.player_hair_idx_label = Label(self, text=player.appearance.hair.name)
        self.player_hair_idx_label.grid(row=22, column=0, sticky="e")
        self.player_hair_idx_entry = Entry(self, width=6)
        self.player_hair_idx_entry.delete(0,'end')
        self.player_hair_idx_entry.insert(0,player.appearance.hair())
        self.player_hair_idx_entry.grid(row=22, column=1, sticky="w")

        """
        self.player_hair_type_label = Label(self, text="Hair Type")
        self.player_hair_type_label.grid(row=22, column=0, sticky="e")
        self.player_hair_type_combobox = Combobox(
            self, 
            state="readonly", 
            value=[
                "BALD", "BUZZ CUT", "VERY SHORT 1", "VERY SHORT 2", 
                "STRAIGHT 1", "STRAIGHT 2", "CURLY 1", "CURLY 2", 
                "PONYTAIL 1", "PONYTAIL 2", "DREADLOCKS", "PULLED BACK", 
                "SPECIAL HAIRSTYLES",
            ],
            width=20
        )
        self.player_hair_type_combobox.bind('<<ComboboxSelected>>', lambda event: self.hairstyle_options(player))
        self.player_hair_type_combobox.set(player.appearance.hair()[0])
        self.player_hair_type_combobox.event_generate('<<ComboboxSelected>>')
        self.player_hair_type_combobox.grid(row=22, column=1, sticky="w")
        """

        self.apply_button = Button(self, text="Apply", command=lambda: self.update_player_data(player))
        self.apply_button.grid(row=29, column=0)
        self.cancel_button = Button(self, text="Cancel", command=lambda :self.stop_window())
        self.cancel_button.grid(row=29, column=1)
        self.psd_button = Button(self, text = "PSD Paste", command= lambda : paste_psd(self, self.selection_get(selection = "CLIPBOARD"), nations))
        self.psd_button.grid(row=29, column=7)

        column_2_row_counter = 0
        self.abilities_entries = {}
        for ability in player.abilities:

            lb = Label(self, text=ability.name)
            lb.grid(row=column_2_row_counter, column=2, sticky="e")

            e = Entry(self, width=3)
            e.delete(0, 'end')
            e.insert(0, ability())
            e.grid(row=column_2_row_counter, column=3, sticky="e")
            self.abilities_entries[ability.name] = e

            column_2_row_counter+=1

        self.abilities_1_8_entries = {}

        for ability in player.abilities_1_8:

            lb = Label(self, text=ability.name)
            lb.grid(row=column_2_row_counter, column=2, sticky="e")

            e = Entry(self, width=3)
            e.delete(0,'end')
            e.insert(0,ability())
            e.grid(row=column_2_row_counter, column=3, sticky="e")
            self.abilities_1_8_entries[ability.name] = e

            column_2_row_counter+=1

        column_4_row_counter = 0
        self.special_abilities_status_var = {}
        for special_ability in player.special_abilities:

            lb = Label(self, text=special_ability.name)
            lb.grid(row=column_4_row_counter, column=4, sticky="e")

            self.special_abilities_status_var[special_ability.name]=IntVar(self, special_ability())
            chk = Checkbutton(self, variable=self.special_abilities_status_var[special_ability.name])
            chk.grid(row=column_4_row_counter, column=5, sticky="e")
            column_4_row_counter+=1

        self.player_favored_side_label = Label(self, text=player.position.favored_side.name)
        self.player_favored_side_label.grid(row=5, column=6, sticky="e")
        self.player_favored_side_combobox = Combobox(self, state="readonly", value=["R", "L", "B",], width=20)
        self.player_favored_side_combobox.set(player.position.favored_side())
        self.player_favored_side_combobox.grid(row=5, column=7, sticky="w")

        self.player_registered_position_label = Label(self, text=player.position.registered_position.name)
        self.player_registered_position_label.grid(row=6, column=6, sticky="e")
        self.player_registered_position_combobox = Combobox(
            self, 
            state="readonly", 
            value=[
                position.name 
                for i, position in enumerate(player.position)
                if i > 1
            ],
            width=25,
        )
        self.player_registered_position_combobox.current(player.position.registered_position())
        self.player_registered_position_combobox.grid(row=6, column=7, sticky="w")

        column_6_row_counter = 7
        self.positions_status_var = {}
        for i, position in enumerate(player.position):
            if i > 1:
                lb = Label(self, text=position.name)
                lb.grid(row=column_6_row_counter, column=6, sticky="e")

                self.positions_status_var[position.name]=IntVar(self, position())
                chk = Checkbutton(self, variable=self.positions_status_var[position.name])

                chk.grid(row=column_6_row_counter, column=7, sticky="nsew")
                column_6_row_counter+=1
        self.lift()
        self.grab_set()
        self.resizable(False, False)
        self.protocol('WM_DELETE_WINDOW', self.stop_window)
        #self.mainloop()

    def update_player_data(self, player:Player):
        player.name = self.player_name_entry.get()
        player.shirt_name = self.player_shirt_name_entry.get()
        player.callname.set_value(common_functions.intTryParse(self.player_callname_entry.get()))
        player.nation.set_value(self.player_nationality_combobox.get())
        player.basic_settings.age.set_value(common_functions.intTryParse(self.player_age_spinbox.get()))
        player.basic_settings.stronger_foot.set_value(self.player_stronger_foot_combobox.get())
        player.basic_settings.injury.set_value(self.player_injury_combobox.get())
        player.basic_settings.style_of_dribble.set_value(common_functions.intTryParse(self.player_style_of_dribble_combobox.get()))
        player.basic_settings.free_kick_type.set_value(common_functions.intTryParse(self.player_free_kick_type_combobox.get()))
        player.basic_settings.penalty_kick.set_value(common_functions.intTryParse(self.player_penalty_kick_combobox.get()))
        player.basic_settings.drop_kick_style.set_value(common_functions.intTryParse(self.player_drop_kick_style_combobox.get()))
        player.basic_settings.goal_celebration_1.set_value(self.player_goal_celebration_1_combobox.current())
        player.basic_settings.goal_celebration_2.set_value(self.player_goal_celebration_2_combobox.current())
        player.basic_settings.growth_type.set_value(common_functions.intTryParse(self.player_growth_type_entry.get()))

        player.appearance.height.set_value(common_functions.intTryParse(self.player_height_entry.get()))
        player.appearance.weight.set_value(common_functions.intTryParse(self.player_weight_entry.get()))
        player.appearance.skin_colour.set_value(common_functions.intTryParse(self.player_skin_colour_combobox.get()))
        player.appearance.face.set_value(self.player_face_combobox.get())
        player.appearance.face_idx.set_value(common_functions.intTryParse(self.player_face_idx_spinbox.get()))
        """
        player.appearance.hair.set_value(
            [
                self.player_hair_type_combobox.get(),
                common_functions.intTryParse(self.player_hair_shape_spinbox.get()),
                common_functions.intTryParse(self.player_hair_front_spinbox.get()),
                common_functions.intTryParse(self.player_hair_volume_spinbox.get()),
                common_functions.intTryParse(self.player_hair_darkness_spinbox.get()),
                common_functions.intTryParse(self.player_hair_bandana_type_spinbox.get()),
            ]
        )
        """
        player.appearance.hair.set_value(common_functions.intTryParse(self.player_hair_idx_entry.get()))
        for ability in player.abilities:
            ability.set_value(common_functions.intTryParse(self.abilities_entries.get(ability.name).get()))

        for ability in player.abilities_1_8:
            ability.set_value(common_functions.intTryParse(self.abilities_1_8_entries.get(ability.name).get()))

        for special_ability in player.special_abilities:
            special_ability.set_value(common_functions.intTryParse(self.special_abilities_status_var.get(special_ability.name).get()))

        player.position.favored_side.set_value(self.player_favored_side_combobox.get())
        player.position.registered_position.set_value(self.player_registered_position_combobox.current())
        
        for i, position in enumerate(player.position):
            if i > 1:
                position.set_value(common_functions.intTryParse(self.positions_status_var.get(position.name).get()))

        for flag in player.edited_flags:
            flag.set_value(1)

        self.stop_window()


    def stop_window(self):
        self.quit()
        self.destroy()




