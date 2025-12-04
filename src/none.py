def wrong():
    l = [[None]*3]*3
    l[0][0] = 1
    print(l)


'''выведет [[1, None, None], [1, None, None], [1, None, None]]'''


def right():
    l = [[None]*3 for i in range(3)]
    l[0][0] = 1
    print(l)


'''выведет [[1, None, None], [None, None, None], [None, None, None]]'''

'''* создаёт поверхностную копию.
В первом случае все три строки это ссылки на один и тот же список в памяти. 
Когда меняешь l[0][0], меняются все строки, потому что это один объект
[[None]*3 for i in range(3)] создаёт три разных списка в памяти.'''
wrong()
right()
