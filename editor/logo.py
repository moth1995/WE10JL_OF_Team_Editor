class Logo:
    start_address = 788972
    total = 80
    header_size = 32
    size = 608
    dimension = 32
    bpp = 4
    palette_size = 1 << bpp
    palette_pes_size = bpp * palette_size

    def __init__(self, option_file, idx):
        self.option_file = option_file
        self.idx = idx
        self.set_addresses()
        self.set_logo()
        self.set_pes_palette()
        self.set_pes_idat()

    def set_addresses(self):
        """
        Set the following logo addresses:

        - logo
        """
        self.header_address = self.start_address + (self.idx * self.size)
        self.logo_address = self.header_address + self.header_size

    def set_logo(self):
        """
        Generates a bytearray with the logo data
        """
        self.header = self.option_file.data[self.header_address : self.header_address + self.header_size]
        self.logo = self.option_file.data[self.logo_address : self.header_address + self.size]

    def set_pes_palette(self):
        """
        Set the "PES" palette which is a combination of rgb palette + transparency
        """
        self.pes_palette = self.logo[: self.palette_pes_size]

    def set_pes_idat(self):
        """
        Set the "PES" idat which is a png idat decompress
        """
        self.pes_idat = self.logo[self.palette_pes_size :]

    def enable_logo(self):
        self.header[0] = 1

    def delete_logo(self):
        self.header = bytearray(self.header_size)
        self.logo = bytearray(self.size - self.header_address)