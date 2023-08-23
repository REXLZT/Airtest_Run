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
-------------------------------------
---Sample A
print("SELF sample")
local tA = {a = 1, b = 2}
function tA.Add(self)
    return (self.a + self.b)
end
print(tA.Add(tA))

-------------------------------------
---Sample B
local tB = {a = 1, b = 2}
function tB:Add()
    return (self.a + self.b)
end
print(tB:Add())