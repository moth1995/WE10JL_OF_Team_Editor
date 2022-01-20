from .utils.common_functions import zero_fill_right_shift


def get_points(ba):
    return (ba[54] << 16) + (ba[53] << 8) + (ba[52])

def set_points(new_points,ba):
    if 0 <= new_points <= 99999:
        ba[52] = (new_points & 0xFF)
        ba[53] = zero_fill_right_shift((new_points & 0xFF00), 8)
        ba[54] = zero_fill_right_shift((new_points & 0xFF0000), 16)
        #need to search this
        ba[5212] = (new_points & 0xFF);
        ba[5213] = zero_fill_right_shift((new_points & 0xFF00) , 8)
        ba[5214] = zero_fill_right_shift((new_points & 0xFF0000) , 16)
        return get_points(ba)
    else:
        raise ValueError("Points value must be between 0 and 99999")

def lock_shop(ba):
    for i in range(5144,5170):
        ba[i] = 0
    ba[56] = 1
    return "Shop locked!"

def unlock_shop(ba):
    for i in range(20):
        ba[5144 + i] = 255
    ba[5164] = 254
    ba[5165] = 255
    ba[5166] = 255
    ba[5167] = 127
    ba[5168] = 15
    ba[5169] = 63
    ba[56] = 98
    return "Shop unlocked!"

def get_background(ba):
    return ba[5224]

def set_background(ba, val):
    if 0<=val<= 62:
        ba[5224] = val
        return "Main Menu BG Changed!"
    else:
        raise ValueError("Out of range value")
