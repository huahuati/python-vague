class Grandfather(object):
    mylist = []
    def __init__(self):
        pass
class Father(Grandfather):
    pass

Grandfather.mylist = [1, 2, 3, 4]
print(Grandfather.mylist)
print(Father.mylist)
Father.mylist = ['a']
Grandfather.mylist = ['b']
print(Father.mylist)
print(Grandfather.mylist)
print(Father.mylist)
'''
    从上面的实验可以看出，子类继承父类后，初始状态下，继承了父类的属性。
    当在子类中修改继承过来的类属性时，并不会修改父类的同名类属性。
以后只要是通过子类访问该属性，访问的都是子类的属性；
    通过父类修改了父类属性后，子类访问该属性时，会访问父类修改后的属性值。
前提是子类没有对该属性重新赋值过，如果子类修改过该属性，则会遵循上面的规则
'''