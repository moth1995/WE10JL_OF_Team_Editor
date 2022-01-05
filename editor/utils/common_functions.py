def bytes_to_int(ba, a):
    ia = [ba[a + i] for i in range(4)]
    return ia[0] | (ia[1] << 8) | (ia[2] << 16) | (ia[3] << 24)


def zero_fill_right_shift(val, n):
    return (val % 0x100000000) >> n


#Added by moth_1995
#used on get_values
def to_int(b):
	i = b
	if i < 0:
		i = i + 256
	return i

#used on set_values

def to_byte(i):
    b = b''
    print(i)
    if i > 127:
        b = (i - 256)
        print("entered into condition")
        print(b)
    else :
        print("is not bigger than 127")
        b = (i)
        print(b)
    return b
