
def x(lst):
    if(len(lst) == 0):
        return
    else:
        print(lst[0])
        return x(lst[1:])




if __name__ == '__main__':
    y = [1,2,3,4,5]
    z = {'a': 1, 'b':2}
    print(len(z))
    print(len(list(z)))
    x(y)