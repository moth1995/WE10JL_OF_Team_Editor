TOTAL = 38
BASE_NAME_LEN = 20
START_ADDRESS = 13574
MAX_LEN = 61
SIZE = BASE_NAME_LEN + 1 + MAX_LEN + 2;

def get_offset(league):
    return START_ADDRESS + league * SIZE

def get_name(ba, league):
    return ba[get_offset(league) + BASE_NAME_LEN + 1: get_offset(league) + BASE_NAME_LEN + 1 + MAX_LEN].partition(b"\0")[0].decode('utf-8')

def get_leagues_list(ba):
    return [get_name(ba,i)for i in range(TOTAL)]

def set_name(ba, league, new_name):
    if 0 < len(new_name) < MAX_LEN:
        new_name = new_name[: MAX_LEN]
        league_name_bytes = [0] * MAX_LEN
        new_name_bytes = str.encode(new_name, "utf-8","ignore")
        league_name_bytes[: len(new_name_bytes)] = new_name_bytes
        for i, byte in enumerate(league_name_bytes):
            ba[get_offset(league) + BASE_NAME_LEN + 1 + i] = byte
        return "League name changed!"
    else:
        raise ValueError("League name can't be empty or bigger than 60 characters")