def swap_case(s):
    # s="HeLlo"
    for ch in s:
        # ch='HeLlo'
        if ch.isupper(): #H
            print(ch.lower(),end='')#hl
        else:
            print(ch.upper(),end='')#ELO
    return 

if __name__ == '__main__':
    # s = input()
    s="HeLlo"
    result = swap_case(s)