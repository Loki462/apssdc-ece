##### Constructer:
#it's a special method executes at the time of object creation...
#def __init__(self)
class student:
    def __init__(self,name,branch):
        print('constructer executed...')
        self.name = name
        self.branch = branch
    def Details(self):
        print('Hello:',self.name)
        print('Branch:',self.branch)
        print('Method execution...')
name = input('enter a name:')
branch = input('enter a branch:')
s = student(name,branch)
s.Details()
def add (a,b):
    return a+b
a = int(input('Enter a value:'))
b = int(input('Enter b value:'))
c = add(a,b)
print(c)
