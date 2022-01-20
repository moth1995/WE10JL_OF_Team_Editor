TOTAL = 64
START_ADDRESS = 9544
MAX_LEN = 61
SW_ADDR = START_ADDRESS + MAX_LEN * TOTAL
END_ADDR = SW_ADDR + TOTAL


def get_offset(stadium):
    return START_ADDRESS + stadium * MAX_LEN

def get_name(ba, stadium):
    return ba[get_offset(stadium): get_offset(stadium) + MAX_LEN].partition(b"\0")[0].decode('utf-8')

def get_stadium_list(ba):
    return [get_name(ba,i)for i in range(TOTAL)]

def set_name(ba, stadium, new_name):
    if 0 < len(new_name) < MAX_LEN:
        new_name = new_name[: MAX_LEN]
        stadium_name_bytes = [0] * MAX_LEN
        new_name_bytes = str.encode(new_name, "utf-8","ignore")
        stadium_name_bytes[: len(new_name_bytes)] = new_name_bytes
        for i, byte in enumerate(stadium_name_bytes):
            ba[get_offset(stadium) + i] = byte
        ba[SW_ADDR+stadium] = 1
        return "Stadium name changed!"
    else:
        raise ValueError("Stadium name can't be empty or bigger than 60 characters")