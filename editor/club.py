class Club:
    total = 162
    start_address = 680400
    size = 92
    max_name_size = 48

    def __init__(self, option_file, idx):
        self.option_file = option_file
        self.idx = idx
        
        self.set_addresses()
        self.set_name()

    def set_addresses(self):
        """
        Set the following club addresses:

        - Name
        """
        self.name_address = self.start_address + (self.idx * self.size)

    def set_name(self):
        """
        Set club name from relevant OF data bytes.
        """
        name_byte_array = self.option_file.data[
            self.name_address : self.name_address + (self.max_name_size + 1)
        ]
        try:
            self.name = name_byte_array.partition(b"\0")[0].decode('utf8')
        except:
            self.name = f"<Encoding Error Team {self.idx + 64}>"

    def update_name(self, name):
        """
        Update club name with the supplied value.
        """
        new_name = name[: self.max_name_size]

        club_name_bytes = [0] * (self.max_name_size + 1)
        new_name_bytes = str.encode(new_name,"utf-8")
        club_name_bytes[: len(new_name_bytes)] = new_name_bytes

        for i, byte in enumerate(club_name_bytes):
            self.option_file.data[self.name_address + i] = byte

        self.name = new_name
