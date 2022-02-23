import io
from PIL import Image, ImageTk
import zlib

class PNG:
    PNG_SIGNATURE = bytearray([137, 80, 78, 71, 13, 10, 26, 10])
    IHDR_LENGTH = bytearray((13).to_bytes(4, byteorder='big', signed=False))
    IHDR = bytearray([73,72,68,82])
    PLTE = bytearray([80,76,84,69])
    TRNS = bytearray([116,82,78,83])
    IDAT = bytearray([73,68,65,84])
    IEND_LENGTH = bytearray(4)
    IEND = bytearray([73,69,78,68])
    iend_crc32 = bytearray(zlib.crc32(IEND).to_bytes(4, byteorder='big', signed=False))
    iend_chunk = IEND_LENGTH + IEND + iend_crc32

    def __init__(self, pes_img):
        self.pes_img = pes_img
        self.png_from_pes_img16()

    def png_from_pes_img16(self):
        """
        Returns a PNG image from a pes image
        """
        IHDR_DATA = bytearray(self.pes_img.dimension.to_bytes(4, byteorder='big', signed=False)) +  bytearray(self.pes_img.dimension.to_bytes(4, byteorder='big', signed=False)) + bytearray([self.pes_img.bpp, 3, 0, 0, 0])
        ihdr_crc32 = bytearray(zlib.crc32(self.IHDR + IHDR_DATA).to_bytes(4, byteorder='big', signed=False))
        ihdr_chunk = self.IHDR_LENGTH + self.IHDR + IHDR_DATA + ihdr_crc32
        palette_data = self.pes_palette_to_RGB()
        plte_lenght = bytearray(len(palette_data).to_bytes(4, byteorder='big', signed=False))
        plte_crc32 = bytearray(zlib.crc32(self.PLTE + palette_data).to_bytes(4, byteorder='big', signed=False))
        plt_chunk = plte_lenght + self.PLTE + palette_data + plte_crc32
        trns_data = self.pes_trns_to_alpha()
        trns_lenght = bytearray(len(trns_data).to_bytes(4, byteorder='big', signed=False))
        trns_crc32 = bytearray(zlib.crc32(self.TRNS+trns_data).to_bytes(4, byteorder='big', signed=False))
        trns_chunk = trns_lenght + self.TRNS + trns_data + trns_crc32
        idat_data = self.pes_px_to_idat()
        idat_lenght = bytearray(len(idat_data).to_bytes(4, byteorder='big', signed=False))
        idat_crc32 = bytearray(zlib.crc32(self.IDAT + idat_data).to_bytes(4, byteorder='big', signed=False))
        idat_chunk = bytearray(idat_lenght + self.IDAT + idat_data + idat_crc32)
        self.png = self.PNG_SIGNATURE + ihdr_chunk + plt_chunk + trns_chunk + idat_chunk + self.iend_chunk

    def png_bytes_to_tk_img(self):
        return ImageTk.PhotoImage(Image.open(io.BytesIO(self.png)).convert("RGBA"))


    def pes_palette_to_RGB(self):
        palette_data = bytearray()
        for j in range(0, len(self.pes_img.pes_palette), 4):
            palette_data += self.pes_img.pes_palette[j : j + 3]
        return palette_data

    def pes_trns_to_alpha(self):
        trns_data = bytearray()
        for j in range(3, len(self.pes_img.pes_palette), 4):
            trns_data += self.pes_img.pes_palette[j : j + 1]
        return trns_data

    def pes_px_to_idat(self):
        idat_uncompress = bytearray()
        for j in range(0, len(self.pes_img.pes_idat), self.pes_img.palette_size):
            idat_uncompress += b'\x00' + self.pes_img.pes_idat[j : j + self.pes_img.palette_size]
        return bytearray(zlib.compress(idat_uncompress))
