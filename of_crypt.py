
def of_encrypter(temp_file, of):
# Here we read decrypted Option File and copy all the data to the original Option File
    try:
        with open(temp_file, "rb") as binary_file:
            of.data = bytearray(binary_file.read())
            # Save/encrypt the option file
            #print("Saving option file...")
            of.save_option_file()
            #print("Option file saved.")
        return True
    except EnvironmentError: # parent of IOError, OSError *and* WindowsError where available
        #print("Error while reading/saving the file, please run as admin")
        return False

def of_decrypter(of, temp_file):
    try:
        with open(temp_file, "wb") as binary_file:
            binary_file.write(of.data)
        #print("Option File decrypted")
        return True
    except EnvironmentError: # parent of IOError, OSError *and* WindowsError where available
        #print("Error while creating the file, please run as admin")
        return False