
def str_counter(string):
    
    for sym in set(string):
        counter = 0
        for sub_sym  in string:
            if sym == sub_sym:
                counter += 1
        print(sym, counter)

str_counter('aaaaa aaaa aa  aaabc')
