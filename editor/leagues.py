class League:

    TOTAL = 38
    BASE_NAME_LEN = 20
    START_ADDRESS = 13574
    MAX_LEN = 61
    SIZE = BASE_NAME_LEN + 1 + MAX_LEN + 2;

    def __init__(self,option_file, idx):
        self.idx = idx
        self.of = option_file

        self.get_offset()
        self.get_name()

    def get_offset(self):
        self.offset = self.START_ADDRESS + self.idx * self.SIZE

    def get_name(self):
        self.name = self.of.data[self.offset + self.BASE_NAME_LEN + 1: self.offset + self.BASE_NAME_LEN + 1 + self.MAX_LEN].partition(b"\0")[0].decode('utf-8',"ignore")

    def set_name(self, new_name):
        if 0 < len(new_name) < self.MAX_LEN:
            new_name = new_name[: self.MAX_LEN]
            league_name_bytes = [0] * self.MAX_LEN
            new_name_bytes = str.encode(new_name, "utf-8","ignore")
            league_name_bytes[: len(new_name_bytes)] = new_name_bytes
            for i, byte in enumerate(league_name_bytes):
                self.of.data[self.offset + self.BASE_NAME_LEN + 1 + i] = byte
            self.name = new_name
            return "League name changed!"
        else:
            raise ValueError("League name can't be empty or bigger than 60 characters")