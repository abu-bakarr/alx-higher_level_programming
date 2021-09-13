#!/usr/bin/python3
def element_at(my_list, idx):
    v_return = "None"
    if (idx < 0):
        return(v_return)
    else:
        if (idx >= len(my_list)):
            return(v_return)
        else:
            return(my_list[idx])
