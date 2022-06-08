import option_file_data

class Emblem:
    total_128 = 50
    total_16 = total_128 * 2
    total = total_128 + total_16
    idx_table_adr = option_file_data.OF_BLOCK[8] + 4
    idx_table_size = 2 + total + 8
    empty_idx_value = 0x99
    start_address = idx_table_adr + idx_table_size

    #837628 + 160

    #startaddb = 837788 + (5184 * 50)
    #The emblem image with and height (64px x 64px).
    width = 64
    height = 64
    #The hi-res indexed-color image format (8 bits-per-pixel).
    bpp_128 = 8
    #The low-res indexed-color image format (4 bits-per-pixel).
    bpp_16 = 4
    #A hi-res club emblem data record length (5184 bytes).
    size_128 = 5184
    #A low-res club emblem data record length (2176 bytes).
    size_16 = 2176
    palette_size_16 = 1 << bpp_16
    palette_size_128 = 1 << bpp_128
    palette_pes_size_16 = bpp_16 * palette_size_16
    palette_pes_size_128 = bpp_128 * palette_size_128
