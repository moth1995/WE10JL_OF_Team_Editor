def get_players_nations(of, team_id):
    players=[]
    for i in range (0, 23):
        players.append(int.from_bytes(of.data[nations_players_relink_offset + (i * 2) + (team_id * nations_players_relink_size) : nations_players_relink_offset + (i * 2) + 2  + (team_id * nations_players_relink_size)], byteorder='little'))
    return players

def get_players_clubs(of, team_id):
    team_id-=64
    players=[]
    for i in range (0, 32):
        players.append(int.from_bytes(of.data[clubs_players_relink_offset + (i * 2) + (team_id * clubs_players_relink_size) : clubs_players_relink_offset + (i * 2) + 2 + (team_id * clubs_players_relink_size)], byteorder='little'))
    return players

def get_players_ml(of):
    players=[]
    for i in range (0, 32):
        players.append(int.from_bytes(of.data[ml_players_relink_offset + (i * 2) : ml_players_relink_offset + (i * 2) + 2], byteorder='little'))
    return players

def get_formation(of, team_id):
    if 0 <= team_id <= 63:
        formation_data = of.data[nations_formation_data_offset + (team_id * formation_data_size) : nations_formation_data_offset + formation_data_size + (team_id * formation_data_size) ]
    elif 64 <= team_id <= 201:
        formation_data = of.data[clubs_formation_data_offset + ((team_id - 64) * formation_data_size) : clubs_formation_data_offset + formation_data_size + ((team_id - 64) * formation_data_size) ]
    return formation_data

def get_formation_generic(of, team_id):
    if 0 <= team_id <= 63:
        formation_data = of.data[nations_formation_data_offset + (team_id * formation_data_size) + 3 : nations_formation_data_offset + formation_data_size + (team_id * formation_data_size) ]
    elif 64 <= team_id <= 201:
        formation_data = of.data[clubs_formation_data_offset + ((team_id - 64) * formation_data_size) + 3: clubs_formation_data_offset + formation_data_size + ((team_id - 64) * formation_data_size) ]
    return formation_data

def set_formation(of, team_id, formation_data):
    if 0 <= team_id <= 63:
        for i, byte in enumerate(formation_data):
            of.data[nations_formation_data_offset+(team_id*formation_data_size) + i] = byte
    elif 64 <= team_id <= 201:
        for i, byte in enumerate(formation_data):
            of.data[clubs_formation_data_offset+((team_id - 64)*formation_data_size) + i] = byte

def set_formation_generic(of, team_id, formation_data):
    if 0 <= team_id <= 63:
        for i, byte in enumerate(formation_data):
            of.data[nations_formation_data_offset + 3 + (team_id*formation_data_size) + i] = byte
    elif 64 <= team_id <= 201:
        for i, byte in enumerate(formation_data):
            of.data[clubs_formation_data_offset+ 3 + ((team_id - 64)*formation_data_size) + i] = byte

first_nat_team_id = 0
last_nat_team_id = 63
first_club_team_id = 64
last_club_team_id = 211

nations_players_relink_offset = 683296
nations_players_relink_size = 46
clubs_players_relink_offset = 686654
clubs_players_relink_size = 64
nations_jersey_number_offset = 676624
nations_jersey_number_size = 23
clubs_jersey_number_offset = 678303
clubs_jersey_number_size = 32
clubs_names_offset = 773820
clubs_names_size = 48
three_letter_clubs_name_offset = 773869
three_letter_clubs_name_size = 3
nations_formation_data_offset = 696640
clubs_formation_data_offset = 719936
formation_data_size = 364
nations_kits_data_offset = 786856
clubs_kits_data_offset = 809384
nations_kits_data_size = 352
clubs_kits_data_size = 544

ml_players_relink_offset = 696126
