from multiprocessing import Pool

def f(x):
    print(x + ' lol')

l=['1','2', '3']
if __name__ == '__main__':
    p = Pool(5)
    print(p.map(f, l))
