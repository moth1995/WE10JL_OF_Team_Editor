from .utils.common_functions import zero_fill_right_shift
from .nationalities import get_nation, get_nation_idx
class Stat:
    start_address = 48
    def __init__(self, option_file, player,offset, shift, mask, name, type=None):
        self.option_file = option_file
        self.player = player
        self.offset = offset
        self.shift = shift
        self.mask = mask
        self.name = name
        self.type = type
        self.get_value()

    @property
    def address(self):
        return self.player.address + self.start_address + self.offset

    def get_value(self):
        #i = self.player.start_address + 48 + self.player.idx * 124 + self.offset
        #if self.player.idx > self.player.total_players:
            #i = self.player.start_address_edited + 48 + (self.player.idx - self.player.first_edited_id) * 124 + self.offset
        j = (self.option_file.data[self.address]) << 8 | (self.option_file.data[(self.address - 1)])
        j = zero_fill_right_shift(j,self.shift)
        j &= self.mask
        if self.type is not None:
            j = self.normalize(j)
        self.__value = j

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if self.type is not None:
            new_value = self.denormalize(new_value)
        #i = self.player.start_address + 48 + (self.player.idx * 124) + self.offset
        #if (self.player.idx > self.player.total_players):
            #i = self.player.start_address_edited + 48 + ((self.player.idx - self.player.first_edited_id) * 124) + self.offset
        j = (self.option_file.data[self.address]) << 8 | (self.option_file.data[(self.address - 1)])
        k = 0xFFFF & (self.mask << self.shift ^ 0xFFFFFFFF)
        j &= k
        new_value &= self.mask
        new_value <<= self.shift
        new_value = j | new_value
        self.option_file.data[(self.address - 1)] = (new_value & 0xFF)
        self.option_file.data[self.address] = (zero_fill_right_shift(new_value,8))
        self.get_value()

    def normalize(self,val):
        def foot_fav_side():
            return foot_fav_side_list[val]

        def nation():
            return get_nation(val)

        def hair():
            return val

        def injury():
            return injury_list[val]

        def eyes_colour_2():
            return eyes_colour_2_list[val]

        def face_type():
            return face_type_list[val]

        def yes_no():
            return no_yes_list[val]

        if isinstance(self.type, str):
            return eval(self.type.format(stat=val, normalize=True))

        mycase = {
            0 : foot_fav_side,
            1 : nation,
            2 : hair,
            3 : injury,
            4 : eyes_colour_2,
            5 : face_type,
            6 : yes_no,
        }
        myfunc = mycase[self.type]
        return myfunc()
        #raise NotImplementedError

    def denormalize(self, val):
        def foot_fav_side():
            return foot_fav_side_list.index(val)

        def nation():
            return get_nation_idx(val)

        def hair():
            return val

        def injury():
            return injury_list.index(val)

        def eyes_colour_2():
            return eyes_colour_2_list.index(val)

        def face_type():
            return face_type_list.index(val)

        def yes_no():
            return no_yes_list.index(val)

        if isinstance(self.type, str):
            return eval(self.type.format(stat=val, normalize=False))

        mycase = {
            0 : foot_fav_side,
            1 : nation,
            2 : hair,
            3 : injury,
            4 : eyes_colour_2,
            5 : face_type,
            6 : yes_no,
        }
        myfunc = mycase[self.type]
        return myfunc()
        #raise NotImplementedError
    
    #def __call__(self):
        #return self.value


injury_list = ["C", "B", "A",]
foot_fav_side_list = ["R", "L", "B",]
face_type_list = ["BUILD", "ORIGINAL", "PRESET",]
no_yes_list = ["NO", "YES",]
eyes_colour_2_list = [
    "BLACK 1", "BLACK 2", "DARK GREY 1", 
    "DARK GREY 2", "BROWN 1", "BROWN 2", 
    "LIGHT BLUE 1", "LIGHT BLUE 2", "BLUE 1", 
    "BLUE 2", "GREEN 1", "GREEN 2",
]


