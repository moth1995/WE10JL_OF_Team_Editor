from .stat import Stat

class Player:
    start_address = 39608
    start_address_edited = 16780
    #last_self.idx = 4872
    first_edited_id = 32768
    total_edit = 184
    first_unused = 4504
    total_players = 4540
    first_shop = 4157
    first_ml_youth = 4317
    first_ml_old = 4494

    def __init__(self,option_file, idx):
        self.idx = idx
        self.option_file = option_file
        self.name, self.shirt_name = self.get_names()
        self.callName = Stat(self.option_file, self, 1, 0, 65535, "Callname idx")
        self.nation = Stat(self.option_file, self, 65, 0, 127, "Nationality")
        self.foot = Stat(self.option_file, self, 5, 0, 1, "Foot")
        """
        if self.foot == 0:
            self.foot = "R"
        else:
            self.foot = "L"
        """
        self.injury = Stat(self.option_file, self, 33, 6, 3, "Injury T")
        
        """
        if self.injury == 2:
            self.injury = "A"
        elif self.injury == 1:
            self.injury = "B"
        else:
            self.injury = "C"
        """
        self.dribSty = Stat(self.option_file, self, 6, 0, 3, "Dribble Style")# + 1
        self.freekick = Stat(self.option_file, self, 5, 1, 15, "FK Style")# + 1
        self.pkStyle = Stat(self.option_file, self, 5, 5, 7, "PK Style")# + 1
        self.dkSty = Stat(self.option_file, self, 6, 2, 3, "DK Style")# + 1
        self.age = Stat(self.option_file, self, 65, 9, 31, "Age")# +15
        #self.goal_c1 = Stat(self.option_file,self,85-48, 1, 127, "GOAL CELEBRATION 1")
        #self.goal_c2 = Stat(self.option_file,self,86-48, 0, 127, "GOAL CELEBRATION 2")
        # self.option_filefset for growth type is rigth, but i cant get the proper value in any elif, also this value seems to be related to salary self.option_file player
        #self.growth_type= Stat(self.option_file,self,87-48,2, 3, "Growth type")
        
        # Position settings
        self.regPos = Stat(self.option_file, self, 6, 4, 15, "Registered position")
        self.gk = Stat(self.option_file, self, 7, 7, 1, "GK")
        self.cbwS = Stat(self.option_file, self, 7, 15, 1, "CWP")
        self.cbt = Stat(self.option_file, self, 9, 7, 1, "CBT")
        self.sb = Stat(self.option_file, self, 9, 15, 1, "SB")
        self.dm = Stat(self.option_file, self, 11, 7, 1, "DM")
        self.wb = Stat(self.option_file, self, 11, 15, 1, "WB")
        self.cm = Stat(self.option_file, self, 13, 7, 1, "CM")
        self.sm = Stat(self.option_file, self, 13, 15, 1, "SM")
        self.om = Stat(self.option_file, self, 15, 7, 1, "AM")
        self.wg = Stat(self.option_file, self, 15, 15, 1, "WG")
        self.ss = Stat(self.option_file, self, 17, 7, 1, "SS")
        self.cf = Stat(self.option_file, self, 17, 15, 1, "CF")
        self.favSidxe = Stat(self.option_file, self, 33, 14, 3, "Fav sidxe")
        """
        if self.favSidxe == 0:
            self.favSidxe = "R"
        elif self.favSidxe == 1:
            self.favSidxe = "L"
        else:
            self.favSidxe = "B"
        """
        # Abilities
        self.wfa = Stat(self.option_file, self, 33, 11, 7, "W Foot Acc")# + 1
        self.wff = Stat(self.option_file, self, 33, 3, 7, "W Foot Freq")# + 1
        self.attack = Stat(self.option_file, self, 7, 0, 127, "Attack")
        self.defence = Stat(self.option_file, self, 8, 0, 127, "Defense")
        self.balance = Stat(self.option_file, self, 9, 0, 127, "Balance")
        self.stamina = Stat(self.option_file, self, 10, 0, 127, "Stamina")
        self.speed = Stat(self.option_file, self, 11, 0, 127, "Speed")
        self.accel = Stat(self.option_file, self, 12, 0, 127, "Accel")
        self.response = Stat(self.option_file, self, 13, 0, 127, "Response")
        self.agility = Stat(self.option_file, self, 14, 0, 127, "Agility")
        self.dribAcc = Stat(self.option_file, self, 15, 0, 127, "Drib Acc")
        self.dribSpe = Stat(self.option_file, self, 16, 0, 127, "Drib Spe")
        self.sPassAcc = Stat(self.option_file, self, 17, 0, 127, "S Pass Acc")
        self.sPassSpe = Stat(self.option_file, self, 18, 0, 127, "S Pass Spe")
        self.lPassAcc = Stat(self.option_file, self, 19, 0, 127, "L Pass Acc")
        self.lPassSpe = Stat(self.option_file, self, 20, 0, 127, "L Pass Spe")
        self.shotAcc = Stat(self.option_file, self, 21, 0, 127, "Shot Acc")
        self.shotPow = Stat(self.option_file, self, 22, 0, 127, "Shot Power")
        self.shotTec = Stat(self.option_file, self, 23, 0, 127, "Shot Tech")
        self.fk = Stat(self.option_file, self, 24, 0, 127, "FK Acc")
        self.swerve = Stat(self.option_file, self, 25, 0, 127, "Swerve")
        self.heading = Stat(self.option_file, self, 26, 0, 127, "Heading")
        self.jump = Stat(self.option_file, self, 27, 0, 127, "Jump")
        self.tech = Stat(self.option_file, self, 29, 0, 127, "Tech")
        self.aggress = Stat(self.option_file, self, 30, 0, 127, "Aggression")
        self.mental = Stat(self.option_file, self, 31, 0, 127, "Mentality")
        self.consistency = Stat(self.option_file, self, 33, 0, 7, "Consistency")# + 1
        self.gkAbil = Stat(self.option_file, self, 32, 0, 127, "GK")
        self.team = Stat(self.option_file, self, 28, 0, 127, "Team Work")
        self.condition = Stat(self.option_file, self, 33, 8, 7, "Condition")# + 1
        
        # Special Abilities
        self.drib = Stat(self.option_file, self, 21, 7, 1, "Dribbling")
        self.dribKeep = Stat(self.option_file, self, 21, 15, 1, "Anti-Dribble")
        self.post = Stat(self.option_file, self, 29, 7, 1, "Post")
        self.posit = Stat(self.option_file, self, 23, 7, 1, "Positioning")
        self.reaction = Stat(self.option_file, self, 23, 15, 1, "Reaction")
        self.linePos = Stat(self.option_file, self, 29, 15, 1, "Line Position")
        self.midShot = Stat(self.option_file, self, 31, 7, 1, "Mid shooting")
        self.scorer = Stat(self.option_file, self, 27, 7, 1, "Scoring")
        self.play = Stat(self.option_file, self, 25, 7, 1, "Playmaking")
        self.passing = Stat(self.option_file, self, 25, 15, 1, "Passing")
        self.pk = Stat(self.option_file, self, 19, 7, 1, "Penalties")
        self.k11 = Stat(self.option_file, self, 27, 15, 1, "1-1 Scoring")
        self.longThrow = Stat(self.option_file, self, 37, 7, 1, "Long Throw")
        self.direct = Stat(self.option_file, self, 35, 0, 1, "1-T Pass")
        self.side = Stat(self.option_file, self, 31, 15, 1, "Side")
        self.centre = Stat(self.option_file, self, 19, 15, 1, "Centre")
        self.outside = Stat(self.option_file, self, 35, 1, 1, "Outside")
        self.man = Stat(self.option_file, self, 35, 2, 1, "Marking")
        self.dLine = Stat(self.option_file, self, 35, 5, 1, "D-L Control")
        self.slide = Stat(self.option_file, self, 35, 3, 1, "Sliding")
        self.cover = Stat(self.option_file, self, 35, 4, 1, "Cover")
        self.keeperPK = Stat(self.option_file, self, 35, 6, 1, "Penalty GK")
        self.keeper11 = Stat(self.option_file, self, 35, 7, 1, "1-on-1 GK")
        
        # Player appearence settings
        # Head
        
        # Face menu
        self.face_type = Stat(self.option_file,self,55, 0, 3, "face TYPE")
        """
        if self.face_type == 0:
            self.face_type = "BUILD"
        elif self.face_type == 1:
            self.face_type = "PRESET SPECIAL"
        elif self.face_type == 2:
            self.face_type = "PRESET NORMAL"
        else:
            self.face_type = "ERROR"
        """
        self.skin_colour = Stat(self.option_file,self, 41, 6, 3, "skin colour")# + 1
        #self.head_height = Stat(self.option_file,self, 91-48, 3, 15, "head height") - 7
        #self.head_widxth = Stat(self.option_file,self, 91-48, 7, 15, "head widxth") - 7
        self.face_idx = Stat(self.option_file,self, 53, 5, 511, "face idx")# + 1
        #self.head_ov_pos = Stat(self.option_file,self, 124-48,5, 7, "Head overall position") - 3
        
        # Brows menu
        #self.brows_type = Stat(self.option_file,self, 119-48, 5, 31, "Brows type") + 1
        #self.brows_angle = (Stat(self.option_file,self, 119-48, 2, 7, "Brown angle") - 3)*-1
        #self.brows_height = (Stat(self.option_file,self, 118-48, 4, 7, "Brown height") - 3)*-1
        #self.brows_spacing = (Stat(self.option_file,self, 118-48, 7, 7, "Brown spacing") - 3)*-1
        
        # Eyes menu
        #self.eyes_type = Stat(self.option_file,self, 116-48, 3, 31, "Eyes type") + 1
        #self.eyes_position = (Stat(self.option_file,self, 117-48, 0, 7, "Eye Position")-3)*-1
        #self.eyes_angle = (Stat(self.option_file,self, 117-48, 3, 7, "Eye Angle") -3)*-1
        #self.eyes_lenght = (Stat(self.option_file,self, 117-48, 6, 7, "Eye Length") -3)*-1
        #self.eyes_widxth = (Stat(self.option_file,self, 118-48, 1, 7, "Eye Widxth") -3)*-1
        #self.eyes_c1 = Stat(self.option_file,self, 94-48, 9, 3, "Eyes colour 1") + 1
        #self.eyes_c2 = Stat(self.option_file,self, 95-48, 3, 15, "Eyes colour 2")
        """
        if self.eyes_c2 == 0:
            self.eyes_c2 = "BLACK 1"
        elif self.eyes_c2 == 1:
            self.eyes_c2 = "BLACK 2"
        elif self.eyes_c2 == 2:
            self.eyes_c2 = "DARK GREY 1"
        elif self.eyes_c2 == 3:
            self.eyes_c2 = "DARK GREY 2"
        elif self.eyes_c2 == 4:
            self.eyes_c2 = "BROWN 1"
        elif self.eyes_c2 == 5:
            self.eyes_c2 = "BROWN 2"
        elif self.eyes_c2 == 6:
            self.eyes_c2 = "LIGHT BLUE 1"
        elif self.eyes_c2 == 7:
            self.eyes_c2 = "LIGHT BLUE 2"
        elif self.eyes_c2 == 8:
            self.eyes_c2 = "BLUE 1"
        elif self.eyes_c2 == 9:
            self.eyes_c2 = "BLUE 2"
        elif self.eyes_c2 == 10:
            self.eyes_c2 = "GREEN 1"
        elif self.eyes_c2 == 11:
            self.eyes_c2 = "GREEN 2"
        else:
            self.eyes_c2 = "ERROR"
        """
        # Nose menu
        #self.nose_type = Stat(self.option_file,self,121-48, 0, 7, "Nose type") + 1
        #self.nose_height = (Stat(self.option_file,self,121-48, 6, 7, "Nose height") - 3)*-1
        #self.nose_widxth = (Stat(self.option_file,self,121-48, 3, 7, "Nose widxth") - 3)*-1
        
        # Cheeks menu
        #self.cheecks_type = Stat(self.option_file,self,120-48, 2, 7, "cheeks type") + 1
        #self.cheecks_shape = (Stat(self.option_file,self,120-48, 5, 7, "cheecks shape") - 3)*-1
        
        # Mouth menu
        #self.mouth_type = Stat(self.option_file,self,122-48, 1, 31, "mouth type") + 1
        #self.mouth_size = (Stat(self.option_file,self,123-48, 1, 7, "mouth type") - 3)*-1
        #self.mouth_position = (Stat(self.option_file,self,122-48, 6, 7, "mouth position") - 3)*-1
        
        # Jaw menu
        #self.jaw_type = Stat(self.option_file,self,123-48, 4, 7, "Jaw type") + 1
        #self.jaw_chin = (Stat(self.option_file,self,123-48, 7, 7, "Jaw chin") - 3)*-1
        #self.jaw_widxth = (Stat(self.option_file,self,124-48, 2, 7, "Jaw widxth") - 3)*-1

        # Hair menu
        # The variable below will get the Hairstyle idx but we have to return many other variables such a hair type, shape, front, volume, darkness and bandana
        # Millions self.option_file thanks to Pato_lucas18 for this code who save me from doom
        self.hair =  Stat(self.option_file,self,45, 0, 2047, "Hair idx")
        """
        # Bald
        if 0 <= self.hair <= 3:
            self.hair_type = "BALD"
            self.hair_shape = self.hair + 1
            self.hair_front = 1
            self.hair_volume = 1
            self.hair_darkness = 1
            self.hair_bandana = 1
        # Buzz cut
        elif 4 <= self.hair <= 83:
            self.hair_type = "BUZZ CUT"
            self.hair_shape = 1
            self.hair_front = 1
            self.hair_volume = 1
            self.hair_darkness = 0
            self.hair_bandana = 1
            for c in range(4, self.hair + 1):
                self.hair_darkness += 1
                if self.hair_darkness == 5:
                    self.hair_darkness = 1
                    self.hair_front += 1
                    if self.hair_front == 6:
                        self.hair_front = 1
                        self.hair_shape += 1
        # Very short 1
        elif 84 <= self.hair <= 107:
            self.hair_type = "VERY SHORT 1"
            self.hair_shape = 1
            self.hair_front = 0
            self.hair_volume = 1
            self.hair_darkness = 1
            self.hair_bandana = 1
            for c in range(84, self.hair +1 ):
                self.hair_front += 1
                if self.hair_front == 7:
                    self.hair_front = 1
                    self.hair_shape += 1
        # Very short 2
        elif 108 <= self.hair <= 152:
            self.hair_type = "VERY SHORT 2"
            self.hair_front = 0
            self.hair_volume = 1
            self.hair_darkness = 1
            self.hair_bandana = 1
            if self.hair >= 138:
                self.hair_shape = 4
                for c in range(138, self.hair + 1):
                    self.hair_front += 1
                    if self.hair_front == 6:
                        self.hair_front = 1
                        self.hair_shape += 1
            else:
                self.hair_shape = 1
                for c in range(108, self.hair + 1):
                    self.hair_front += 1
                    if self.hair_front == 11:
                        self.hair_front = 1
                        self.hair_shape += 1
        # Straight 1
        elif 153 <= self.hair <= 560:
            self.hair_type = "STRAIGHT 1"
            self.hair_shape = 1
            self.hair_front = 1
            self.hair_volume = 1
            self.hair_darkness = 1
            self.hair_bandana = 0
            for c in range(153, self.hair + 1):
                self.hair_bandana += 1
                if self.hair_bandana > 3 :
                    self.hair_volume += 1
                    self.hair_bandana = 1
                    if self.hair_volume == 4 :
                        self.hair_front += 1
                        self.hair_volume = 1
                        if self.hair_front == 17 :
                            self.hair_shape += 1
                            self.hair_front = 1
                    if self.hair_front >= 10:
                        self.hair_bandana = 4
        # Straight 2
        elif 561 <= self.hair <= 659:
            self.hair_type = "STRAIGHT 2"
            self.hair_shape = 1
            self.hair_front = 1
            self.hair_volume = 1
            self.hair_darkness = 1
            self.hair_bandana = 0
            for c in range(561, self.hair + 1):
                self.hair_bandana += 1
                if self.hair_bandana > 3:
                    self.hair_volume += 1
                    self.hair_bandana = 1
                    if self.hair_volume == 4:
                        self.hair_front += 1
                        self.hair_volume = 1
                        if self.hair_front == 8:
                            self.hair_shape += 1
                            self.hair_front = 1
                    if self.hair_front >= 3:
                        self.hair_bandana = 4
        # Curly 1
        elif 660 <= self.hair <= 863:
            self.hair_type = "CURLY 1"
            self.hair_shape = 1
            self.hair_front = 1
            self.hair_volume = 1
            self.hair_darkness = 1
            self.hair_bandana = 0
            for c in range(660, self.hair + 1):
                self.hair_bandana += 1
                if self.hair_bandana > 3 :
                    self.hair_volume += 1
                    self.hair_bandana = 1
                    if self.hair_volume == 4 :
                        self.hair_front += 1
                        self.hair_volume = 1
                        if self.hair_front == 8 :
                            self.hair_shape += 1
                            self.hair_front = 1
                    if self.hair_front >= 6:
                        self.hair_bandana = 4
        # Curly 2
        elif 864 <= self.hair <= 911:
            self.hair_type = "CURLY 2"
            self.hair_shape = 1
            self.hair_front = 1
            self.hair_volume = 0
            self.hair_darkness = 1
            self.hair_bandana = 1
            for c in range(864, self.hair + 1):
                self.hair_volume += 1
                if self.hair_volume == 3 :
                    self.hair_front += 1
                    self.hair_volume = 1
                    if self.hair_front == 7 :
                        self.hair_shape += 1
                        self.hair_front = 1
        # Ponytail 1
        elif 912 <= self.hair <= 947:
            self.hair_type = "PONYTAIL 1"
            self.hair_shape = 1
            self.hair_front = 1
            self.hair_volume = 0
            self.hair_darkness = 1
            self.hair_bandana = 1
            for c in range(912, self.hair + 1):
                self.hair_volume += 1
                if self.hair_volume == 4 :
                    self.hair_front += 1
                    self.hair_volume = 1
                    if self.hair_front == 5:
                        self.hair_shape += 1
                        self.hair_front = 1
        # Ponytail 2
        elif 948 <= self.hair <= 983:
            self.hair_type = "PONYTAIL 2"
            self.hair_shape = 1
            self.hair_front = 1
            self.hair_volume = 0
            self.hair_darkness = 1
            self.hair_bandana = 1
            for c in range(948, self.hair + 1):
                self.hair_volume += 1
                if self.hair_volume == 4 :
                    self.hair_front += 1
                    self.hair_volume = 1
                    if self.hair_front == 5:
                        self.hair_shape += 1
                        self.hair_front = 1
        # Dreadlocks
        elif 984 <= self.hair <= 1007:
            self.hair_type = "DREADLOCKS"
            self.hair_shape = 1
            self.hair_front = 1
            self.hair_volume = 0
            self.hair_darkness = 1
            self.hair_bandana = 1
            for c in range(984, self.hair + 1):
                self.hair_volume += 1
                if self.hair_volume == 3 :
                    self.hair_front += 1
                    self.hair_volume = 1
                    if self.hair_front == 5 :
                        self.hair_shape += 1
                        self.hair_front = 1
        # Pulled back
        elif 1008 <= self.hair <= 1025:
            self.hair_type = "PULLED BACK"
            self.hair_shape = 1
            self.hair_front = 0
            self.hair_volume = 1
            self.hair_darkness = 1
            self.hair_bandana = 1
            for c in range(1008, self.hair + 1):
                self.hair_front += 1
                if self.hair_front == 7:
                    self.hair_shape += 1
                    self.hair_front = 1
        # Special hair
        elif 1026 <= self.hair <= 2047:
            self.hair_type = "SPECIAL HAIRSTYLES"
            self.hair_shape = self.hair - 1025
            self.hair_front = 1
            self.hair_volume = 1
            self.hair_darkness = 1
            self.hair_bandana = 1        
        # Another case that should not happen... just to return a value :)
        else:
            self.hair_type = "OUT OF RANGE ERROR"
            self.hair_shape = self.hair
            self.hair_front = 1
            self.hair_volume = 1
            self.hair_darkness = 1
            self.hair_bandana = 1
        """
        # Hair colour menu
        #self.hair_colour_config = Stat(self.option_file, self, 94-48, 3, 63, "hair colour config") + 1
        #self.hair_rgb_r = (Stat(self.option_file, self, 102-48, 5, 63, "hair colour rgb R") - 63)*-1
        #self.hair_rgb_g = (Stat(self.option_file, self, 103-48, 3, 63, "hair colour rgb G") - 63)*-1
        #self.hair_rgb_b = (Stat(self.option_file, self, 104-48, 1, 63, "hair colour rgb B") - 63)*-1
        
        """
        # Hair bandana menu
        if self.hair_bandana==4:
            self.hair_bandana=1
        self.hair_bandana-=1
        """
        #self.hair_bandana_colour = Stat(self.option_file,self,109-48, 2, 7, "bandana colour") + 1
        # Cap menu
        #self.cap = Stat(self.option_file, self, 98-48, 6, 1, "cap")
        #self.cap_colour = Stat(self.option_file, self, 114-48, 3, 7, "cap colour") + 1
        # Facial hair menu
        #self.facial_hair_type = Stat(self.option_file,self,95-48, 7, 127, "facial hair")
        #self.facial_hair_colour = Stat(self.option_file,self,97-48, 0, 63, "facial hair colour") + 1
        # Sunglasses menu
        #self.sunglasses = Stat(self.option_file,self,97-48, 6, 3, "Sun glasses type")
        #self.sunglasses_colour = Stat(self.option_file,self,114-48, 0, 7, "Sun glasses colour") + 1
        
        # Physical settings
        self.height = Stat(self.option_file, self, 41, 0, 63, "Height")# + 148
        self.weight = Stat(self.option_file, self, 41, 8, 127, "Weight")
        """
        self.neck_length = Stat(self.option_file,self,105-48, 2, 15, "Neck Length") - 7
        self.neck_widxth = Stat(self.option_file,self,92-48, 3, 15, "Neck Widxth") - 7
        self.shoulder_height = Stat(self.option_file,self,109-48, 5, 15, "Shoulder Height") -7
        self.should_widxth = Stat(self.option_file,self,110-48, 1, 15, "Shoulder Widxth") - 7
        self.chest_measu = Stat(self.option_file,self,105-48, 6, 15, "Chest measurement") - 7
        self.waist_circu = Stat(self.option_file,self,106-48, 6, 15, "Waist Circ") -7
        self.arm_circu = Stat(self.option_file,self,106-48, 2, 15, "Arm Circumferemce") - 7
        self.leg_circu = Stat(self.option_file,self,107-48, 2, 15, "Leg Circumference") - 7
        self.calf_circu = Stat(self.option_file,self,107-48, 6, 15, "Calf Circ") - 7
        self.leg_length = Stat(self.option_file,self,108-48, 4, 15, "Leg Length") - 7
        body_parameters = [self.neck_length, self.neck_widxth, self.shoulder_height, self.should_widxth, self.chest_measu, self.waist_circu, self.arm_circu, 
        self.leg_circu, self.calf_circu, self.leg_length]
        self.body_type = body_types.index(body_parameters) + 1 if body_parameters in body_types else "Edited"
        """
        # Boots/Accesories
        """
        self.boot_type = Stat(self.option_file, self, 99-48, 9, 15, "boot type")
        self.boot_colour = Stat(self.option_file, self, 99-48, 13, 3, "boot COLOUR") + 1 
        self.neck_warm = Stat(self.option_file,self,98-48, 0, 1, "Neck Warmer")
        self.necklace_type = Stat(self.option_file,self,98-48, 1, 3, "Necklace type")
        self.necklace_colour = Stat(self.option_file,self,98-48, 3, 7, "Necklace colour") + 1
        self.wistband = Stat(self.option_file,self,98-48, 7, 3, "wistband")
        self.wistband_colour = Stat(self.option_file,self,99-48, 1, 7, "wistband colour") + 1
        self.friend_brace =  Stat(self.option_file,self,99-48, 3, 4, "friendship bracelate")
        self.friend_brace_colour =  Stat(self.option_file,self,99-48, 6, 7, "friendship bracelate colour") + 1
        self.gloves = Stat(self.option_file,self,104-48, 7, 1, "Gloves")
        self.finger_band = Stat(self.option_file,self,109-48, 0, 3, "Finger Band")
        self.shirt = Stat(self.option_file,self,92-48, 7, 1, "Shirt")
        self.sleeves =  Stat(self.option_file,self,96-48, 6, 3, "Sleeves")
        self.under_short =  Stat(self.option_file,self,100-48, 76, 1, "under short")
        self.under_short_colour =  Stat(self.option_file,self,101-48, 0, 7, "under short colour") + 1
        self.socks =  Stat(self.option_file,self,105-48, 0, 3, "Socks") + 1
        self.tape =  Stat(self.option_file,self,102-48, 4, 1, "Tape")
        """
    def get_names(self):
        #print(self.idx)
        name = "???"
        shirt_name = "???"
        name_bytes_length = 32
        player_offset = self.start_address + self.idx * 124
        if self.idx>self.total_players:
            player_offset = self.start_address_edited + ((self.idx - self.first_edited_id) * 124)
        if (
            self.idx > 0
            and (self.idx <= self.total_players or self.idx >= self.first_edited_id)
            and self.idx < self.first_edited_id + self.total_edit
        ):
            all_name_bytes = self.option_file.data[
                player_offset : player_offset + name_bytes_length
            ]
            try:
                name = all_name_bytes.decode('utf-16-le').encode('utf-8').partition(b"\0")[0].decode('utf-8')
                #name = "".join(map(chr, name))
            except:
                name = f"<Error {self.idx}>"
            

            if not name:
                no_name_prefixes = {
                    self.first_edited_id: "Edited",
                    self.first_unused: "Unused",
                    1: "Unknown",
                }

                for address, address_prefix in no_name_prefixes.items():
                    if self.idx >= address:
                        prefix = address_prefix
                        break

                name = f"{prefix} ({self.idx})"
            #get the shirt name
            shirt_name_address = player_offset + 32
            name_byte_array = self.option_file.data[
                shirt_name_address : shirt_name_address
                + name_bytes_length // 2
            ]
            shirt_name = name_byte_array.partition(b"\0")[0].decode('utf-8')
        return name, shirt_name

    def set_name(self, new_name):
        name_bytes_length = 32
        max_name_size = 15
        new_name = new_name[: max_name_size]
        if (new_name == "Unknown (" + str(self.idx) + ")" or new_name == "Edited (" + str(self.idx) + ")" or new_name == "Unused (" + str(self.idx) + ")" or new_name == ""):
            player_name_bytes=[0] * name_bytes_length
        else:
            player_name_bytes = [0] * name_bytes_length
            new_name_bytes = str.encode(new_name, "utf-16-le","ignore")
            player_name_bytes[: len(new_name_bytes)] = new_name_bytes
        player_offset = self.start_address + self.idx * 124
        if self.idx>self.total_players:
            player_offset = self.start_address_edited + ((self.idx - self.first_edited_id) * 124)
        if (
            self.idx > 0
            and (self.idx <= self.total_players or self.idx >= self.first_edited_id)
            and self.idx < self.first_edited_id + self.total_edit
        ):
            for i, byte in enumerate(player_name_bytes):
                self.option_file.data[player_offset + i] = byte

    def set_shirt_name(self, new_shirt_name):
        max_name_size = 15
        shirt_name_bytes_length = 16
        player_offset = self.start_address + self.idx * 124
        if self.idx>self.total_players:
            player_offset = self.start_address_edited + ((self.idx - self.first_edited_id) * 124)
        if (
            self.idx > 0
            and (self.idx <= self.total_players or self.idx >= self.first_edited_id)
            and self.idx < self.first_edited_id + self.total_edit
        ):

            shirt_name_address = player_offset + 32
            new_name = new_shirt_name[: max_name_size].upper()

            player_shirt_name_bytes = [0] * shirt_name_bytes_length
            new_name_bytes = str.encode(new_name,"utf-8")
            player_shirt_name_bytes[: len(new_name_bytes)] = new_name_bytes

            for i, byte in enumerate(player_shirt_name_bytes):
                self.option_file.data[shirt_name_address + i] = byte
