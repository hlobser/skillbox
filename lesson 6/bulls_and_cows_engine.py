from random import randint

def guess_num():
    global hidden_num
    hidden_num = randint(1000, 9999)
    return hidden_num



def chech_num(num):
    bulls_num = 0
    cows_num = 0
    for i in range(4):
        if num[i] == str(hidden_num)[i]:
            bulls_num += 1
    for j in range(3):
        for k in range(j+1, 4):
            if num[j] == str(hidden_num)[k]:
                cows_num += 1
    result = {'bulls': bulls_num, 'cows': cows_num}
    return result
