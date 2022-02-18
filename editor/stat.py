from .utils.common_functions import zero_fill_right_shift

class Stat:
    def __init__(self, option_file, player,offset, shift, mask, name):
        self.option_file = option_file
        self.player = player
        self.offset = offset
        self.shift = shift
        self.mask = mask
        self.name = name

    def get_value(self):
        i = self.player.start_address + 48 + self.player.idx * 124 + self.offset
        if self.player.idx > self.player.total_players:
            i = self.player.start_address_edited + 48 + (self.player.idx - self.player.first_edited_id) * 124 + self.offset
        j = (self.option_file.data[i]) << 8 | (self.option_file.data[(i - 1)])
        j = zero_fill_right_shift(j,self.shift)
        j &= self.mask
        self.normalize(j)
        return j

    def set_value(self, new_value):
        i = self.player.start_address + 48 + (self.player.idx * 124) + self.offset
        if (self.player.idx > self.player.total_players):
            i = self.player.start_address_edited + 48 + ((self.player.idx - self.player.first_edited_id) * 124) + self.offset
        j = (self.option_file.data[i]) << 8 | (self.option_file.data[(i - 1)])
        k = 0xFFFF & (self.mask << self.shift ^ 0xFFFFFFFF)
        j &= k
        new_value &= self.mask
        new_value <<= self.shift
        new_value = j | new_value
        self.option_file.data[(i - 1)] = (new_value & 0xFF)
        self.option_file.data[i] = (zero_fill_right_shift(new_value,8))

    def normalize(self,j):
        pass