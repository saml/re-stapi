global_l = []

def deco(l):
    new_l = l
    l = []
    print('deco', new_l)
    def pred():
        print('pred', new_l)
    def wrapped(fn):
        global_l.append(pred)
        return fn
    return wrapped

@deco([1,2,3])
def f():
    print('f')

for pred in global_l:
    pred()
