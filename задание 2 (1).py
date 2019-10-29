

def mass(a):
    """ Функция, которая перемножает все 
        элементы входного массива
    """
    s = 1
    for i in range(1, len(a), 1):
        s = s*a[i]
        print(s)
        
    return s

N = range(1, 10, 1)
print(mass(N))
 
    