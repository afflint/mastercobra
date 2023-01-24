
def change_char(name, new_char, wrong_char_pos=0):
    new_name = name[:wrong_char_pos] + new_char + \
               name[wrong_char_pos+1:]
    return new_name, name
