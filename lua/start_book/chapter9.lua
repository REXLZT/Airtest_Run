-- - ​	`setmetatable(table, metatable)`：此方法用于为一个表设置元表。
-- -   `getmetatable(table)`：此方法用于获取表的元表对象。

local mytable = {}      --先来个表
local mymetatable = {}  --再来个元表
setmetatable(mytable, mymetatable)  --为该表设置元表
print(setmetatable(mytable,mymetatable)) --这里的输出和表的内存地址是一样的，所以说确实是获取到了
print(mytable)
print(mymetatable)


--或者来个简单的写法
local easymytable = setmetatable({}, {})
easymytable= {10,11}
local temp=getmetatable(easymytable)
print("easymytable=",temp)



-- 计算集合的并集实例
local set1 = {10,40}
local set2 = {10,20,30}

setmetatable(set1, {
	__add = function(self, another)
		local res = {}
		local set = {}
		
		for k,v in pairs(self) do set[v] = true end -- 防止集合元素重复
		for k,v in pairs(another) do set[v] = true end -- 防止集合元素重复
		
		for k,v in pairs(set) do table.insert(res, k) end
		
		return res
	end
})

local set3 = set1 + set2
for k,v in pairs(set3) do print(v) end 



mytable = setmetatable({key1 = "value1"}, {
    __newindex = function(self, key, value)
          rawset(self, key, "\""..value.."\"")
  
    end
  })
  
  mytable.key1 = "new value"
  mytable.key2 = 4
  
  print(mytable.key1,mytable.key2)

-- --抄一下bn里面的remove,先屏蔽下咯，试试看其他的元方法先
-- -- 创建一个局部变量remove并赋值为table.remove的引用
-- local remove = table.remove

-- -- 返回一个带有两个方法的表，并设置元表
-- return setmetatable({
--   -- 定义flush方法，用于清空表t中的元素
--   flush = function(t)
--   for i=#t,1,-1 do t[i] = nil end
--   end,
--   -- 定义get方法，用于返回表t中最后一个元素
--   get = function(t)
--   return t[#t]
--   end
-- }, {
--   -- 定义元表的__call元方法
--   __call = function(t, zone)
--   -- 如果传入了zone参数，则将其添加到表t的末尾
--   if zone then
--     t[#t+1] = zone
--   else
--     -- 如果没有传入zone参数，则从表t中移除并返回最后一个元素
--     return (assert(remove(t), "empty zone stack"))
--   end
--   end
-- })


--下面是_index的调用
print("*******_index*********")
local t = {
    name = "hehe",
}

local mt = {
    __index = function(table, key)
        print("Even though you called a field that doesn't exist, it's okay, I can detect it." .. key);
        --虽然你调用了我不存在的字段，不过没关系，我能探测出来：
    end
}
setmetatable(t,mt);

print(t.money); --但还是会有nil啊


-- 当调用table中不存在的字段时，会调用table元表的__index元方法，这个刚刚我们已经说过了。

-- 但是，如果这个__index元方法是一个table的话，那么，就会在这个table里查找字段，并调用。
print("A clear example")

local t2 = {
    name = "hehe",
}

local mt2 = {
    __index = {
        money = "900,0000",
    }
}
setmetatable(t2,mt2);

print(t2.money);

--下面的是用一个table给另一个table赋值
print("****_newindex*******")
local Man = {
    name = "none",
}

local other = {
    name = "just a table"
}

local t3 = {};

local mt3 = {
    __index = Man,
    __newindex = other
}

setmetatable(t3, mt3);

print("other`name,before:" .. other.name);
print("t3`name:" .. t3.name);
t3.name = "boy";
print("other`name,after:" .. other.name);
--当给t3的name字段赋值后，other的name字段反而被赋值了，而t3的name字段仍然没有发生变化。为什么嘞，实际上t1的name字段还是不存在的，它只是通过__index找到了smartMan的name字段
print("t3`name:" .. t3.name);
--我们给t3的name赋值的时候，实际上是给other的name赋值了

