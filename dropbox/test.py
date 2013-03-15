def helper(in_list, func):
    out_list = []
    for idx, val in enumerate(in_list):
        if in_list[idx+1] < len(in_list)-1 and in_list[idx+1] is not str(func):
            out_list.append(val)
        else:
            out_list.append(val func out_list[idx+2])
            in_list = out_list.append([idx:])
    return out_list

def sum_list(in_list):
    no_mult = helper(in_list, "*")
    no_add = helper(no_mult, "+")
    return no_add

def translate(in_string):
    out_list = []
    temp = ""
    for i in range(0, len(in_string)-1):
        if in_string[i] is "+" or if i is "*":
            out_list.append(int(temp))
            temp = ""
            out_list.append(in_string[i])
        else:
            temp += in_string[i]
    sum_list(out_list.append(int(temp)))

            
