def energy(m, v, g, h):
    """Функция, определяющая полную
       механическую энергию тела
    """
    E=(m*v**2/2+m*g*h)
    from const import g
m=3
h=4
v=5
tab=energy/(m, v, g, h)
    print(tab)