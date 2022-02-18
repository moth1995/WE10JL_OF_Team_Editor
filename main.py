from tkinter import messagebox, ttk, filedialog, Tk, Menu, Frame, Label, IntVar, Checkbutton, Button, Entry

from editor.option_file import OptionFile

from gui.club_tab import ClubTab
from gui.shop_tab import ShopTab
from gui.stadium_league_tab import StadiumLeagueTab

from swap_teams import swap_teams_data
from player_data import get_stats, first_unused, first_edited_id, total_edit, national_teams, total_players
from export_csv import write_csv
from import_csv import load_csv
from of_crypt import of_encrypter, of_decrypter
from teams import get_players_clubs, get_formation_generic, set_formation_generic, first_club_team_id, last_club_team_id

def export_formation_btn_action():
    try:
        root.temp_file = filedialog.asksaveasfile(initialdir=".",title="Save formation", mode='wb', filetypes=(("Bin files","*.bin"),("All files", "*")), defaultextension=".bin")
        if root.temp_file is None:
            return
        with open(root.temp_file.name, "wb") as binary_file:
            binary_file.write(get_formation_generic(of, teamform_cmb.current()))
        messagebox.showinfo(title=appname,message="Formation file created!")
    except OSError as err:
        #print("OS error: {0}".format(err))
        messagebox.showerror(title=appname,message="OS error: {0}".format(err))

def import_formation_btn_action():
    try:
        root.temp_file = filedialog.askopenfilename(initialdir=".",title="Select your formation file", filetypes=(("Bin files","*.bin"),("All files", "*")))
        if root.temp_file is None:
            return
        with open(root.temp_file, "rb") as binary_file:
            set_formation_generic(of, teamform_cmb.current(), bytearray(binary_file.read()))
        messagebox.showinfo(title=appname,message="Formation imported!")
        #save_btn_action()
    except OSError as err:
        #print("OS error: {0}".format(err))
        messagebox.showerror(title=appname,message="OS error: {0}".format(err))

def decrypt_btn_action():
    root.temp_file = filedialog.asksaveasfile(initialdir=".",title="Create your decrypted OF", mode='wb', filetypes=(("Bin files","*.bin"),("All files", "*")), defaultextension=".bin")
    if of_decrypter(of, root.temp_file.name):
        messagebox.showinfo(title=appname,message="Decrypted OF created!")
    else:
        messagebox.showerror(title=appname,message="Error while creating file, please run as admin")

def encrypt_btn_action():
    messagebox.showinfo(title=appname,message="Please take in mind that this will overwrite the data from the OF selected at start with the data from decrypted OF!")
    root.temp_file = filedialog.askopenfilename(initialdir=".",title="Select your decrypted OF", filetypes=(("Bin files","*.bin"),("All files", "*")))
    if root.temp_file!="":
        if of_encrypter(root.temp_file, of):
            messagebox.showinfo(title=appname,message="OF encrypted!")
        else:
            messagebox.showerror(title=appname,message="Error while reading file, please run as admin")

def export_all_to_csv():
    #print(csv_team_cmb.current())
    option_selected = csv_team_cmb.current()
    if option_selected ==0:
        #print(extra_players_check.get())
        players_ids=[*range(1, first_unused, 1)]
        if extra_players_check.get():
            players_ids=[*range(1, total_players, 1)]+[*range(first_edited_id, first_edited_id + total_edit, 1)]
        all_data=[]
        for player in players_ids:
            all_data.append(get_stats(player, of))
        root.new_file = filedialog.asksaveasfile(initialdir=".",title="Create your CSV file", mode='w', filetypes=(("CSV files","*.csv"),("All files", "*")), defaultextension=".csv")
        if root.new_file is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        if write_csv(root.new_file.name, all_data):
            messagebox.showinfo(title=appname,message="CSV file created!")
        else:
            messagebox.showerror(title=appname,message="Error while creating CSV file, please run as admin")
    elif first_club_team_id <= option_selected - 1 <= last_club_team_id:
        players_ids=get_players_clubs(of,option_selected - 1)
        #print(players_ids)
        all_data=[]
        for player in players_ids:
            if player==0: continue
            all_data.append(get_stats(player, of))
        root.new_file = filedialog.asksaveasfile(initialdir=".",title="Create your CSV file", mode='w', filetypes=(("CSV files","*.csv"),("All files", "*")), defaultextension=".csv")
        if root.new_file is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        if write_csv(root.new_file.name,all_data):
            messagebox.showinfo(title=appname,message="CSV file created!")
        else:
            messagebox.showerror(title=appname,message="Error while creating CSV file, please run as admin")
    else:
        messagebox.showerror(title=appname,message="Please select an option!")

def import_all_from_csv():
    root.csv_file = filedialog.askopenfilename(initialdir=".",title="Select your CSV file", filetypes=(("CSV files","*.csv"),("All files", "*")))
    if root.csv_file!="":
        if load_csv(of, root.csv_file):
            #of.save_option_file()
            messagebox.showinfo(title=appname,message="CSV file imported")
        else:
            messagebox.showerror(title=appname,message="Error while importing CSV file")

#this is a function to update the list in the combobox
def swap_list_positions(teams_list, pos1, pos2): 
    teams_list[pos1], teams_list[pos2] = teams_list[pos2], teams_list[pos1] 
    return teams_list

def swap_btn_action():
    global teams_list
    if ((first_club_team_id <= team_a_cmb.current() <= last_club_team_id) and (first_club_team_id <= team_b_cmb.current() <= last_club_team_id)):
        if swap_teams_data(of.data, team_a_cmb.current(), team_b_cmb.current(), swap_kits_check.get()):
            teams_list=swap_list_positions(teams_list, team_a_cmb.current(), team_b_cmb.current())
            team_a_cmb.config(values=teams_list)
            team_b_cmb.config(values=teams_list)
            messagebox.showinfo(title=appname,message="Teams swapped!")        
        else:
            messagebox.showerror(title=appname,message="Can't swap the same team!!!")
    else:
        messagebox.showerror(title=appname,message="Can't swap Nations and Club teams!!!")
    
def save_btn_action():
    try:
        of.save_option_file()
        messagebox.showinfo(title=appname,message=f"All changes saved at {of.file_location}")
    except EnvironmentError as e: # parent of IOError, OSError *and* WindowsError where available
        messagebox.showerror(title=appname,message=f"Error while saving, error type={e}, try running as admin")

def save_as_btn_action():
    try:
        save_as = filedialog.asksaveasfile(initialdir=".",title=appname, mode='wb', filetypes=([("All files", "*")]), defaultextension=of.extension)
        if save_as is None:
            return
        of.save_option_file(save_as.name)
        messagebox.showinfo(title=appname,message=f"All changes saved at {of.file_location}")
    except EnvironmentError as e: # parent of IOError, OSError *and* WindowsError where available
        messagebox.showerror(title=appname,message=f"Error while saving, error type={e}, try running as admin")

def refresh_gui():
    csv_team_list = ["---ALL PLAYERS---"] + of.teams.teams_list
    csv_team_cmb['value'] = csv_team_list
    team_a_cmb['value'] = of.teams.teams_list
    team_b_cmb['value'] = of.teams.teams_list
    teamform_cmb['value'] = of.teams.teams_list
    teamform_cmb.current(0)

def show_thanks():
    messagebox.showinfo(title=appname, message="Thanks to PeterC10 for python de/encrypt code for OF,\nYerry11 for png import/export, Aurelio José Parra Morales for players nationalities")

def on_tab_change(event):
    tab = event.widget.tab('current')['text']
    if tab == 'Clubs':
        clubs_tab.refresh_gui()
    elif tab == 'Swap Teams' or tab == 'Export/Import CSV' or tab == 'Extra':
        refresh_gui()

appname='JL WE10 OF Team Editor'
root = Tk()
root.title(appname)
w = 800 # width for the Tk root
h = 600 # height for the Tk root
# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
#Once it start it will ask to select the option file
root.filename=""
root.filename = filedialog.askopenfilename(initialdir=".",title="Select your option file", filetypes=([("JL WE10 PS2 Option File", ".psu .xps"), ("All files", "*")]))
if root.filename!="":
    isencrypted = messagebox.askyesno(title=appname, message="Is your option file encrypted?")
    of = OptionFile(root.filename,isencrypted)

    # CODE BELOW WAS DONE ONLY FOR DEBUGGING, IF YOU WANT TO FIND THE SHIFT AND MASK FOR A STAT
    # YOU JUST NEED TO PASS PLAYER IDS THAT YOU WILL USE TO COMPARE AND WRITE THE POSSIBLE VALUES IN THE LIST CALLED TEST

    '''
    players_ids=[*range(1, 5000, 1)]+[*range(32768, 32952, 1)]
    all_data=[]
    for player_id in players_ids:
        all_data.append(int(get_value(of,player_id,12, 6, 1, "Head overall position")))


    #validate=[*range(0, 8, 1)]#+[*range(0, 6, 1)]
    #validate = [0,1,2,3,4,5,6]
    #validate = [6,5,4,3,2,1,0]
    validate = [0, 0, 1, 0, 0, 1, 1, 1]
    #validate = [63,62,0]
    print(validate)
    test=[]

    for shift in range(0,65536):
        #print (f"the mask is {mask}")
        for mask in range(0,65536):
            #if mask==2047:
            #    print("llegamos al punto conocido")
            #mask=12
            offset = 12
            stat_name = ""
            test.append((get_value(of,1,offset, shift, mask, stat_name) ))
            test.append((get_value(of,2,offset, shift, mask, stat_name) ))
            test.append((get_value(of,3,offset, shift, mask, stat_name) ))
            
            test.append((get_value(of,4,offset, shift, mask, stat_name) ))
            
            test.append((get_value(of,5,offset, shift, mask, stat_name) ))
            test.append((get_value(of,6,offset,shift, mask, stat_name) ))
            
            

            test.append((get_value(of,7,offset, shift, mask, stat_name) ))
            test.append((get_value(of,8,offset, shift, mask, stat_name) ))
            
            #test.append((get_value(of,690,offset, shift, mask, stat_name) ))
            #test.append((get_value(of,4473,offset, shift, mask, stat_name) ))
            #test.append((get_value(of,1485,offset, shift, mask, stat_name) ))
            
            #test.append((get_value(of,4521,offset, shift, mask, stat_name) ))
            #test.append((get_value(of,1229,offset, shift, mask, stat_name) ))
            #test.append((get_value(of,690,offset, shift, mask, stat_name) ))
            #test.append((get_value(of,4029,offset, shift, mask, stat_name) ))

            if test == validate:
                print(shift, mask)
            test=[]
    '''
    # Creating a menu for a better and nice gui
    my_menu=Menu(root)
    root.config(menu=my_menu)
    file_menu = Menu(my_menu, tearoff=0)
    help_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Save", command=save_btn_action)
    file_menu.add_command(label="Save as", command=save_as_btn_action)
    file_menu.add_command(label="Exit", command=root.quit)
    my_menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About...", command=show_thanks)

    tabs_container=ttk.Notebook(root)
    swap_teams_tab=Frame(tabs_container, width=w, height=h)
    csv_tab=Frame(tabs_container, width=w, height=h)
    tabs_container.bind('<Button-1>', lambda e: refresh_gui())
    extra_tab=Frame(tabs_container, width=w, height=h)
    #clubs_tab = Frame(tabs_container, width=w, height=h)
    clubs_tab = ClubTab(tabs_container,of, w, h, appname)
    #stadium_league_tab = Frame(tabs_container, width=w, height=h)
    stadium_league_tab = StadiumLeagueTab(tabs_container,of, w, h, appname)
    #shop_tab = Frame(tabs_container, width=w, height=h)
    shop_tab = ShopTab(tabs_container,of, w, h, appname)
    copyright_lbl=Label(root, text="By PES Indie Team")
    #thanks_lbl=Label(root, text="Thanks to PeterC10 for python de/encrypt code for OF,\nYerry11 for png import/export, Aurelio José Parra Morales for players nationalities")

    #Swap teams tab

    team_a_lbl=Label(swap_teams_tab, text="Team A")
    team_b_lbl=Label(swap_teams_tab, text="Team B")
    team_a_cmb=ttk.Combobox(swap_teams_tab, state="readonly", value=of.teams.teams_list, width=30)
    team_b_cmb=ttk.Combobox(swap_teams_tab, state="readonly", value=of.teams.teams_list, width=30)
    swap_kits_check = IntVar()
    swap_kits_check.set(0)
    swap_kits_check_btn = Checkbutton(swap_teams_tab, text="Swap OF kits", variable=swap_kits_check)
    swap_teams_btn=Button(swap_teams_tab, text="Swap teams", command=lambda: swap_btn_action())
    #save_changes_btn=Button(swap_teams_tab, text="Save changes", command=lambda: save_btn_action())

    #CSV tab

    csv_team_cmb = ttk.Combobox(csv_tab, state="readonly", value=of.teams.csv_team_list, width=30)
    csv_team_cmb.current(0)
    csv_team_cmb.bind('<Button-1>', lambda e: refresh_gui())
    extra_players_check = IntVar()
    extra_players_check.set(1)
    extra_players = Checkbutton(csv_tab, text="Include Unused and Edited players", variable=extra_players_check)
    create_csv_btn = Button(csv_tab, text="Create CSV", command=lambda: export_all_to_csv())
    import_csv_btn = Button(csv_tab, text="Import CSV", command=lambda: import_all_from_csv())

    #Extra tab

    stat_test_entry = Entry (extra_tab) 
    test_print_btn=Button(extra_tab, text="Print stat test!", command=lambda: print(all_data[int(stat_test_entry.get())-1]))
    crypt_lbl=Label(extra_tab, text="Option File cryptology", font = "bold")
    decrypt_of_btn=Button(extra_tab, text="Decrypt", command=lambda: decrypt_btn_action())
    encrypt_of_btn=Button(extra_tab, text="Encrypt", command=lambda: encrypt_btn_action())
    teamform_lbl=Label(extra_tab, text="Formations options", font = "bold")
    teamform_cmb = ttk.Combobox(extra_tab, state="readonly", value=of.teams.teams_list, width=30)
    teamform_cmb.current(0)
    exp_formation_btn = Button(extra_tab, text="Export team\nformation", command=lambda: export_formation_btn_action())
    imp_formation_btn = Button(extra_tab, text="Import team\nformation", command=lambda: import_formation_btn_action())

    # Clubs tab


    #Stadium and Leagues tab

    #Shop tab
    
    #Swap team tab placing

    team_a_lbl.place(x=200, y=60)
    team_b_lbl.place(x=420, y=60)
    team_a_cmb.place(x=200, y=100)
    team_b_cmb.place(x=420, y=100)
    swap_kits_check_btn.place(x=460, y=160)
    swap_teams_btn.place(x=380, y=160)
    #save_changes_btn.place(x=376, y=200)
    copyright_lbl.place(x=0, y=570)
    #thanks_lbl.place(x=480, y=560)

    #CSV tab placing

    csv_team_cmb.place(x=280, y=120)
    extra_players.place(x=280, y=150)
    create_csv_btn.place(x=300, y=200)
    import_csv_btn.place(x=380, y=200)
    # Extra tab placing

    #stat_test_entry.place(x=200, y=70)
    #test_print_btn.place(x=200, y=100)
    teamform_lbl.place(x=280, y=70)
    teamform_cmb.place(x=280, y=120)
    exp_formation_btn.place(x=300, y=150)
    imp_formation_btn.place(x=380, y=150)
    crypt_lbl.place(x=280,y=220)
    decrypt_of_btn.place(x=300, y=280)
    encrypt_of_btn.place(x=380, y=280)

    # Clubs tab placing

    clubs_tab.publish()

    # Stadium Leagues tab placing

    stadium_league_tab.publish()

    # Shop tab placing

    shop_tab.publish()

    #Placing tabs and container in the root

    tabs_container.pack()
    swap_teams_tab.pack(fill="both", expand=1)
    csv_tab.pack(fill="both", expand=1)
    extra_tab.pack(fill="both", expand=1)
    clubs_tab.pack(fill="both", expand=1)
    stadium_league_tab.pack(fill="both", expand=1)
    shop_tab.pack(fill="both", expand=1)

    tabs_container.add(swap_teams_tab, text="Swap Teams")
    tabs_container.add(csv_tab, text="Export/Import CSV")
    tabs_container.add(extra_tab, text="Extra")
    tabs_container.add(clubs_tab, text="Clubs")
    tabs_container.add(stadium_league_tab, text="Stadiums & Leagues")
    tabs_container.add(shop_tab, text="Shop")

    tabs_container.bind('<<NotebookTabChanged>>', on_tab_change)

    root.resizable(False, False)
    root.mainloop()
else:
    root.destroy()
