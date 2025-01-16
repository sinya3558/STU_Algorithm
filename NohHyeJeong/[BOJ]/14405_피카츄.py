S = input() 
pikachu = ['pi', 'ka', 'chu']
is_worked = 1

def cut_word(string, is_worked):    
    for i in pikachu:
        if string.startswith(i):
            string = string[len(list(i)):]
            is_worked = 1
            break
        else:
            is_worked = 0
            pass
    return string, is_worked


while is_worked:
    S, is_worked = cut_word(S, is_worked)

    
if len(S) == 0:
    print('YES')
else:
    print('NO')
    
