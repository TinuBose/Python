class Time:
    __hour = 0
    __minute = 0
    __seccond = 0

    def __init__(self, h, m, s):
        self.__hour = h
        self.__minute = m
        self.__second = s

    def __add__(self, t):
        return self.__hour + t.__hour, self.__minute + t.__minute, self.__second + t.__second


t = Time(2, 5, 6)
t1 = Time(1, 2, 3)
t3 = t1 + t
print(t3)
