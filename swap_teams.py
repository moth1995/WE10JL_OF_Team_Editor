from COFPES_OF_Editor_7.editor.option_file import OptionFile
from teams import *

def read_data(array,pos,grab):
    return array[pos : pos + grab]

def encrypt_and_save(of):
    try:
        #print("Saving option file...")
        of.save_option_file()
        #print("Option file saved.")
        return True
    except EnvironmentError: # parent of IOError, OSError *and* WindowsError where available
        return False

def swap_teams_data(data,team_a_id,team_b_id, kits_flag):
    team_a_id-=64
    team_b_id-=64
    #print(type(team_a_id))
    #print(type(team_b_id))
    if team_a_id==team_b_id:
        return False
    team_a_players_relink = read_data(data,clubs_players_relink_offset+(team_a_id*clubs_players_relink_size),clubs_players_relink_size)
    team_b_players_relink = read_data(data,clubs_players_relink_offset+(team_b_id*clubs_players_relink_size),clubs_players_relink_size)

    team_a_jersey_number = read_data(data,clubs_jersey_number_offset+(team_a_id*clubs_jersey_number_size),clubs_jersey_number_size)
    team_b_jersey_number = read_data(data,clubs_jersey_number_offset+(team_b_id*clubs_jersey_number_size),clubs_jersey_number_size)

    team_a_name=read_data(data,clubs_names_offset+(team_a_id*clubs_names_size),clubs_names_size)
    team_b_name=read_data(data,clubs_names_offset+(team_b_id*clubs_names_size),clubs_names_size)

    #print(team_a_name.decode('utf8'))
    #print(team_b_name.decode('utf8'))

    team_a_three_letter_name=read_data(data,three_letter_clubs_name_offset+(team_a_id*clubs_names_size),three_letter_clubs_name_size)
    team_b_three_letter_name=read_data(data,three_letter_clubs_name_offset+(team_b_id*clubs_names_size),three_letter_clubs_name_size)

    #print(team_a_three_letter_name.decode('utf8'))
    #print(team_b_three_letter_name.decode('utf8'))

    team_a_formation_data = read_data(data,clubs_formation_data_offset+(team_a_id*formation_data_size),formation_data_size)
    team_b_formation_data = read_data(data,clubs_formation_data_offset+(team_b_id*formation_data_size),formation_data_size)

    team_a_kits_data = read_data(data,clubs_kits_data_offset+(team_a_id*clubs_kits_data_size),clubs_kits_data_size)
    team_b_kits_data = read_data(data,clubs_kits_data_offset+(team_b_id*clubs_kits_data_size),clubs_kits_data_size)


    for i, byte in enumerate(team_a_players_relink):
        data[clubs_players_relink_offset+(team_b_id*clubs_players_relink_size) + i] = byte
    for i, byte in enumerate(team_b_players_relink):
        data[clubs_players_relink_offset+(team_a_id*clubs_players_relink_size) + i] = byte

    for i, byte in enumerate(team_a_jersey_number):
        data[clubs_jersey_number_offset+(team_b_id*clubs_jersey_number_size) + i] = byte
    for i, byte in enumerate(team_b_jersey_number):
        data[clubs_jersey_number_offset+(team_a_id*clubs_jersey_number_size) + i] = byte

    for i, byte in enumerate(team_a_name):
        data[clubs_names_offset+(team_b_id*clubs_names_size) + i] = byte
    for i, byte in enumerate(team_b_name):
        data[clubs_names_offset+(team_a_id*clubs_names_size) + i] = byte


    for i, byte in enumerate(team_a_three_letter_name):
        data[three_letter_clubs_name_offset+(team_b_id*clubs_names_size) + i] = byte
    for i, byte in enumerate(team_b_three_letter_name):
        data[three_letter_clubs_name_offset+(team_a_id*clubs_names_size) + i] = byte

    for i, byte in enumerate(team_a_formation_data):
        data[clubs_formation_data_offset+(team_b_id*formation_data_size) + i] = byte
    for i, byte in enumerate(team_b_formation_data):
        data[clubs_formation_data_offset+(team_a_id*formation_data_size) + i] = byte

    if kits_flag:
        for i, byte in enumerate(team_a_kits_data):
            data[clubs_kits_data_offset+(team_b_id*clubs_kits_data_size) + i] = byte
        for i, byte in enumerate(team_b_kits_data):
            data[clubs_kits_data_offset+(team_a_id*clubs_kits_data_size) + i] = byte

    return True

def swap_nations_data(data,team_a_id,team_b_id, kits_flag):
    #print(type(team_a_id))
    #print(type(team_b_id))
    if team_a_id==team_b_id:
        return False
    team_a_players_relink = read_data(data,nations_players_relink_offset+(team_a_id*nations_players_relink_size),nations_players_relink_size)
    team_b_players_relink = read_data(data,nations_players_relink_offset+(team_b_id*nations_players_relink_size),nations_players_relink_size)

    team_a_jersey_number = read_data(data,nations_jersey_number_offset+(team_a_id*nations_jersey_number_size),nations_jersey_number_size)
    team_b_jersey_number = read_data(data,nations_jersey_number_offset+(team_b_id*nations_jersey_number_size),nations_jersey_number_size)

    # Nations names are located in the exe! you must change them with T&S Editor
    
    team_a_formation_data = read_data(data,nations_formation_data_offset+(team_a_id*formation_data_size),formation_data_size)
    team_b_formation_data = read_data(data,nations_formation_data_offset+(team_b_id*formation_data_size),formation_data_size)

    team_a_kits_data = read_data(data,nations_kits_data_offset+(team_a_id*nations_kits_data_size),nations_kits_data_size)
    team_b_kits_data = read_data(data,nations_kits_data_offset+(team_b_id*nations_kits_data_size),nations_kits_data_size)


    for i, byte in enumerate(team_a_players_relink):
        data[nations_players_relink_offset+(team_b_id*nations_players_relink_size) + i] = byte
    for i, byte in enumerate(team_b_players_relink):
        data[nations_players_relink_offset+(team_a_id*nations_players_relink_size) + i] = byte

    for i, byte in enumerate(team_a_jersey_number):
        data[nations_jersey_number_offset+(team_b_id*nations_jersey_number_size) + i] = byte
    for i, byte in enumerate(team_b_jersey_number):
        data[nations_jersey_number_offset+(team_a_id*nations_jersey_number_size) + i] = byte

    for i, byte in enumerate(team_a_formation_data):
        data[nations_formation_data_offset+(team_b_id*formation_data_size) + i] = byte
    for i, byte in enumerate(team_b_formation_data):
        data[nations_formation_data_offset+(team_a_id*formation_data_size) + i] = byte

    if kits_flag:
        for i, byte in enumerate(team_a_kits_data):
            data[nations_kits_data_offset+(team_b_id*nations_kits_data_size) + i] = byte
        for i, byte in enumerate(team_b_kits_data):
            data[nations_kits_data_offset+(team_a_id*nations_kits_data_size) + i] = byte

    return True

#Offsets definition
clubs_names_size = 88
