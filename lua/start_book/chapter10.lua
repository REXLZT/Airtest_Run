--本章为简单的面向对象的调用例子 
local cache = require "lua.start_book.cache"
local c = cache:new()
--创建个对象
local b = cache:new()
--再创个b对象
c:set("name", "lua")
b:set("name","lua2")
--所以说如果set没定义的话，貌似是会被后续新对象给强上了的
c:set("year", 2023)
local op=b:get("name")
print(op)
-- print(c:get("name"))
-- print(c:get("year"))

-- for k,v in pairs(c:getall()) do
-- 	print(k,v)
-- end

--`setmetatable` 将 `_M` 作为新建表的原型，所以在自己的表内找不到所调用方法和变量的时候，便会到 `__index` 所指定的 `_M` 类型中去寻找。


--下面尝试解释下self对象的意义
-- 对于self的解释：表拥有一个标识：self。self类似于this指针，大多数面向对象语言都隐藏了这个机制，在编码时不需要显示的声明这个参数，就可以在方法内使用this（例如C++和C#）。
-- 在lua中，提供了冒号操作符来隐藏这个参数
-- 1、对于方法定义来说，会增加一个额外的隐藏形参（self）；

-- 2、对于方法调用来说，会增加一个额外的实参（表自身）
-------------------------------------
---Sample A
print("***slef****")
local t = {a = 2 , b = 1,c = 10}
--使用:自定义函数
function t:add()
    
    local m=self.a*self.b
    
    local n=self.a+self.b
    self.a=self.c+self.a
    local v=n+m
  return v
end
--使用.自定义函数
function t.sub(parT)
  return parT.a - parT.b
end
--通过:调用，会隐式将self传入进去
print(t:add())
--通过.来调用，则必须传入参数，否则报nil错误
print(t.add(t))
--通过.来调用，则必须传入参数，否则报nil错误
print(t.sub(t))
--通过:来调用，则会隐藏将self传入
print(t:sub())