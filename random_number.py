import random

def generate_random_to_base10():
    
    binary_list = ''
    for i in range(4):
        t = random.randint(0,1)

        binary_list += str(t)
    last = len(binary_list)-1
    sum = 0
    for i in range(0, len(binary_list)):
        digit = int(binary_list[i])
        exponent = last - i
        multiplier = 2 ** exponent
        integer = digit * multiplier
        sum += integer
    print('binary list: ',binary_list)
    print('base 10: ',sum)


generate_random_to_base10()