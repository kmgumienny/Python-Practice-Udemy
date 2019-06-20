def average(first_calue, *args, last_value):
    print(type(args))
    print("*args is {}:".format(args))
    print("*args is:", *args)
    mean = 0
    for arg in args:
        mean += arg
    return  mean / len(args)


#print(average(1,2,3,4))


def build_tuple(*args):
    # tpl = ()
    # for arg in args:
    #     tpl = tpl + (arg,)
    # return tpl
    return args


print(build_tuple(1, 2, 3, 4, 5, 6, 7, 8, 9))
print(build_tuple("earth", "fire", "air", "water"))

def print_backwards(*args, **kwargs):
    for word in args[::-1]:
        print(word[::-1], end= ' ', **kwargs)

with open('backwards.txt', 'w') as backwards:
    print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", file=backwards)
