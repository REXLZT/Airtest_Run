local foo={}
--先把表给定义了

function foo.bar(a, b, c)
        print("a,b,c",a,b,c)
-- body ...
end
--不过对于这样子定义出来的函数，不能再使用 `local` 修饰符了，因为不存在定义新的局部变量了。

local f=foo.bar("laia","laib","laic")
print("output",f)

--给foo加更多的方法
function foo.method1()
    -- ...
  end

  function foo.method2(x)
    -- ... 
  end

  foo.method1()

  foo.method2(10)

--   这样一来,foo表就像一个对象,它包含多个相关方法。我们可以通过foo.method()的方式来调用这些方法。


local function test_var()
	return 1,2,3
end

local x,_,y = test_var()
print(x,y) -- 1	3

-- print("下面的是函数的动态调用")
-- --说白了就是go的虚变量，这个还是好理解的，以单个下划线（“_”） 来命名，用它来丢弃不需要的数值，仅仅起到占位的作用
-- function do_action(func, ...)
-- 	local args = {...} or {} -- 防止为nil
-- 	func(unpack(args, 1, table.maxn(args))) -- 如果实参中确定没有nil空洞（nil值被夹在非空值之间），可以只写第一个参数 
-- end

-- local function add(x, y)
-- 	print(x+y)
-- end
	
-- local function add2(x, y, z)
-- 	print(x+y+z)
-- end

-- do_action(add, 1, 1)
-- do_action(add2, 1, 1, 1)

print("可变参数的例子")
function average(...)
    result = 0
    local arg={...}    --> arg 为一个表，局部变量
    for i,v in ipairs(arg) do   
       result = result + v
    end
    print("总共传入 " .. select("#",...) .. " 个数")
    -- 使用 select("#",...) 来获取可变参数的数量
    print("ALL IN   " .. #arg .. " number")
    --使用三点 ... 表示函数有可变的参数
    return result /#arg
    --牛的 算是看懂的 /标识除法，#arg是获取可变参数，所以说这就直接拿到了平均值了
 end
 
print("AVG",average(10,5,3,4,5,6))

print("函数的动态调用")

function printarg(c,d)
    print(c,d)
end

function callback(fn,args)
    fn(unpack(args))
end