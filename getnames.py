from editor.option_file import OptionFile

def get_of_names(of):

    club_names_list=[]
    for x in range(len(of.clubs)):
        club = of.clubs[x]
        club_names_list.append(club.name)
    return (club_names_list)
