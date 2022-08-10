import random

def generate_random():
    
    binary_list = ''
    for i in range(4):
        t = random.randint(0,1)

        binary_list += str(t)

    print(binary_list)
    print(int(binary_list))


generate_random()