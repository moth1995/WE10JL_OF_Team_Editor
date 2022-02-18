class Teams:
    def __init__(self, option_file):
        self.of = option_file
        self.national_teams = []
        self.club_teams_list = [club.name for club in self.of.clubs]
        self.teams_list=self.national_teams + self.club_teams_list
        self.csv_team_list = ["---ALL PLAYERS---"] + self.teams_list