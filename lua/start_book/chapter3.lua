--运算符系列
print(2^100)
print(22%20) --取模

-- - a and b 如果 a 为 nil，则返回 a，否则返回 b;
-- - a or b 如果 a 为 nil，则返回 b，否则返回 a。
a = 1
b = 2
c = nil

print(a and b)

print(c and a)

print(a and c)

print(b and a) --这里为啥会返回1（即b），因为and连接多个操作数时，表达式的返回值就是从左到右第一个为假的值，若所有操作数值都不为假，则表达式的返回值为最后一个操作数

d = 3
e = 4
f= nil
g= nil

print(d or e)

print(e or f) 

print(d or f)

print(f or g or c or a) --or连接多个操作数时，表达式的返回值就是从左到右第一个不为假的值，若所有操作数值都为假，则表达式的返回值为最后一个操作数

-- a and b or c  类似于 c的表达式 a ? b : c： max = (a > b) and a or b
-- 有个安全返回的写法 (a and b) or c
-- 下面是示例
local a = true
local b = "Hello"
local c = "World"

local result = (a and b) or c
print(result)  -- 输出 "Hello"

a = false
result = (a and b) or c
print(result)  -- 输出 "World"

b = false
result = (a and b) or c
print(result)  -- 输出 "false"



