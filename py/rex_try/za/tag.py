def function(*args):
    print(args)
#*args，原来打包成元组使用
 
function(1,2,3)
print(1)

def fun2(*args):
    print(type(args))

fun2(123)


def function3(**kwargs):
    print(kwargs, type(kwargs))
#打包成字典
 
function3(a=1)