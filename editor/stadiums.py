class Stadium:

    TOTAL = 64
    MAX_LEN = 61
    SW_ADDR = START_ADDRESS + (MAX_LEN * TOTAL)
    END_ADDR = SW_ADDR + TOTAL

    def __init__(self,option_file, idx):
        self.idx = idx
        self.of = option_file
        self.get_offset()
        self.get_name()

    def get_offset(self):
        self.offset = self.START_ADDRESS + self.idx * self.MAX_LEN

    def get_name(self):
        self.name = self.of.data[self.offset : self.offset + self.MAX_LEN].partition(b"\0")[0].decode('utf-8',"ignore")

    def set_name(self, new_name):
        if 0 < len(new_name) < self.MAX_LEN:
            new_name = new_name[: self.MAX_LEN]
            stadium_name_bytes = [0] * self.MAX_LEN
            new_name_bytes = str.encode(new_name, "utf-8","ignore")
            stadium_name_bytes[: len(new_name_bytes)] = new_name_bytes
            for i, byte in enumerate(stadium_name_bytes):
                self.of.data[self.offset + i] = byte
            self.of.data[self.SW_ADDR+self.idx] = 1
            self.get_name()
            self.of.set_stadiums_names()
            return "Stadium name changed!"
        else:
            raise ValueError("Stadium name can't be empty or bigger than 60 characters")
