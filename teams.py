from editor.club import Club

def get_players_clubs(of, team_id):
    team_id-=first_club_team_id
    players=[]
    for i in range (0, 32):
        players.append(int.from_bytes(of.data[clubs_players_relink_offset + (i * 2) + (team_id * clubs_players_relink_size) : clubs_players_relink_offset + (i * 2) + 2 + (team_id * clubs_players_relink_size)], byteorder='little'))
    return players

def get_players_ml(of):
    players=[]
    for i in range (0, 32):
        players.append(int.from_bytes(of.data[ml_players_relink_offset + (i * 2) : ml_players_relink_offset + (i * 2) + 2], byteorder='little'))
    return players

def get_shop_players(of):
    players=[]
    for i in range (0, shop_players_size/2):
        players.append(int.from_bytes(of.data[shop_players_offset + (i * 2) : shop_players_offset + (i * 2) + 2], byteorder='little'))
    return players


def get_formation(of, team_id):
    if first_club_team_id <= team_id <= last_club_team_id:
        formation_data = of.data[clubs_formation_data_offset + ((team_id - first_club_team_id) * formation_data_size) : clubs_formation_data_offset + formation_data_size + ((team_id - first_club_team_id) * formation_data_size) ]
    return formation_data

def get_formation_generic(of, team_id):
    if first_club_team_id <= team_id <= last_club_team_id:
        formation_data = of.data[clubs_formation_data_offset + ((team_id - first_club_team_id) * formation_data_size) + 3: clubs_formation_data_offset + formation_data_size + ((team_id - first_club_team_id) * formation_data_size) ]
    return formation_data

def set_formation(of, team_id, formation_data):
    if first_club_team_id <= team_id <= last_club_team_id:
        for i, byte in enumerate(formation_data):
            of.data[clubs_formation_data_offset+((team_id - first_club_team_id)*formation_data_size) + i] = byte

def set_formation_generic(of, team_id, formation_data):
    if first_club_team_id <= team_id <= last_club_team_id:
        for i, byte in enumerate(formation_data):
            of.data[clubs_formation_data_offset+ 3 + ((team_id - first_club_team_id)*formation_data_size) + i] = byte

first_club_team_id = 0
last_club_team_id = Club.total

clubs_players_relink_offset = 609502 #not really sure
clubs_players_relink_size = 64
clubs_jersey_number_offset = 603615
clubs_jersey_number_size = 32
clubs_names_offset = Club.start_address
clubs_names_size = Club.size
three_letter_clubs_name_offset = 680449
three_letter_clubs_name_size = 10
clubs_formation_data_offset = 620448
formation_data_size = 370
clubs_kits_data_offset = 699548
clubs_kits_data_size = 552 # not really sure 162 teams only?

ml_players_relink_offset = 619870
shop_players_offset = 619998
shop_players_size = 366