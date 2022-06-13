from .appearance import Appearance
from .special_abilities import SpecialAbilities
from .abilities import Abilities, Abilities_1_8
from .positions import Position
from .basic_settings import BasicSettings
from .stat import Stat
from . import option_file_data

class Player:
    start_address = option_file_data.OF_BLOCK[4]
    start_address_edited = option_file_data.OF_BLOCK[3]
    size = 124
    name_encoding = "utf-16-le"
    shirt_encoding = "utf-8"
    max_name_size = 15
    name_bytes_length = 32
    shirt_name_bytes_length = 16
    first_edited_id = 32768
    total_edit = int(option_file_data.OF_BLOCK_SIZE[3] / size)
    first_unused = 4504
    total_players = int(option_file_data.OF_BLOCK_SIZE[4] / size)
    first_shop = 4157
    first_ml_youth = 4317
    first_ml_old = 4494

    def __init__(self,option_file, idx):
        self.idx = idx
        self.of = option_file
        self.set_name_from_bytes()
        self.set_shirt_name_from_bytes()
        self.callname = Stat(self, 1, 0, 65535, "Callname")
        self.nation = Stat(self, 65, 0, 127, "Nationality", 1)
        self.basic_settings = BasicSettings(self)
        self.position = Position(self)
        self.appearance = Appearance(self)
        self.abilities = Abilities(self)
        self.abilities_1_8 = Abilities_1_8(self)
        self.special_abilities = SpecialAbilities(self)

    @property
    def is_edit(self):
        """
        Return true if the player is an edit player.
        A player is deemed an edit player if its index number is greater than
        or equal to the first edit address.
        """
        return self.idx >= self.first_edited_id

    @property
    def offset(self):
        """
        Return player offset.
        """
        return (
            self.idx * self.size
            if not self.is_edit
            else (self.idx - self.first_edited_id) * self.size
        )

    @property
    def address(self):
        """
        Return player address.
        """
        return (
            self.start_address + self.offset
            if not self.is_edit
            else self.start_address_edited + self.offset
        )


    def set_name_from_bytes(self):
        """
        Set player name from relevant OF data bytes.
        """
        name = "???"
        if (
            self.idx > 0
            and (self.idx <= self.total_players or self.idx >= self.first_edited_id)
            and self.idx < self.first_edited_id + self.total_edit
        ):
            all_name_bytes = self.of.data[self.address : self.address + self.name_bytes_length]
            try:
                name = all_name_bytes.decode('utf-16-le').encode('utf-8').partition(b"\0")[0].decode('utf-8')
            except:
                name = f"Error (ID: {self.idx})"

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

        self.__name = name

    @property
    def name(self):
        """
        Return player name.
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Update player name with the supplied value.
        """
        new_name = name[: self.max_name_size]
        if (new_name == "Unknown (" + str(self.idx) + ")" 
            or new_name == "Edited (" + str(self.idx) + ")"
            or new_name == "Unused (" + str(self.idx) + ")" 
            or new_name == "Error (" + str(self.idx) + ")" 
            or new_name == ""):
            player_name_bytes=[0] * self.name_bytes_length
        else:
            player_name_bytes = [0] * self.name_bytes_length
            new_name_bytes = str.encode(new_name, "utf-16-le")
            player_name_bytes[: len(new_name_bytes)] = new_name_bytes

        for i, byte in enumerate(player_name_bytes):
            self.of.data[self.address + i] = byte

        self.__name = new_name

    def set_shirt_name_from_bytes(self):
        """
        Set player shirt name from relevant OF data bytes.
        """
        shirt_name_address = self.address + 32
        name_byte_array = self.of.data[
            shirt_name_address : shirt_name_address
            + self.shirt_name_bytes_length
        ]

        self.__shirt_name = name_byte_array.partition(b"\0")[0].decode()

    @property
    def shirt_name(self):
        """
        Return player shirt name.
        """
        return self.__shirt_name

    @shirt_name.setter
    def shirt_name(self, shirt_name:str):
        shirt_name_address = self.address + 32
        new_name = shirt_name[: self.max_name_size].upper()

        player_shirt_name_bytes = [0] * self.shirt_name_bytes_length
        new_name_bytes = str.encode(new_name)
        player_shirt_name_bytes[: len(new_name_bytes)] = new_name_bytes

        for i, byte in enumerate(player_shirt_name_bytes):
            self.of.data[shirt_name_address + i] = byte

        self.__shirt_name = new_name
