def func1():
    for x in range(1,10):
        if(x%2==0):
            yield x

def func2():
    ret = []
    for x in range(1,10):
        if(x%2==0):
            ret.append(x)
    return ret

print([x for x in func1()])
print(func2())

list1 = [1,2,3,4]
list2 = [10,20,30,40]
list3 = [10,20,30,40]

def func3(l):
    print(id(l))
    l.append(5)
    print(id(l))
    print(l)

def func4(l):
    print(id(l))
    l=[100,200,300]
    print(id(l))
    print(l)

print(list1)
func3(list1)
print(list1)

print(list2)
func4(list2)
print(list2)
print(id(list2), id(list3))

list4 = [1,-1,2,13,3,1]
set1 = set([1,2,3,4])
dict1 = {'a' : 1, 'b' : 2, 3 : 4}
print(id(list4), id(list(list4)))
print(id(set1), id(set(set1)))
print(id(dict1),id(dict(dict1)))

def func5(*args):
    sum=0
    for arg in args:
        sum=sum+arg
    return sum

print(func5(1,2,3,4,5))

def func6(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

func6(cd=2, ab="abcdef")
