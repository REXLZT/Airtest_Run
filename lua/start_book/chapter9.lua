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


--抄一下bn里面的remove
-- 创建一个局部变量remove并赋值为table.remove的引用
local remove = table.remove

-- 返回一个带有两个方法的表，并设置元表
return setmetatable({
  -- 定义flush方法，用于清空表t中的元素
  flush = function(t)
  for i=#t,1,-1 do t[i] = nil end
  end,
  -- 定义get方法，用于返回表t中最后一个元素
  get = function(t)
  return t[#t]
  end
}, {
  -- 定义元表的__call元方法
  __call = function(t, zone)
  -- 如果传入了zone参数，则将其添加到表t的末尾
  if zone then
    t[#t+1] = zone
  else
    -- 如果没有传入zone参数，则从表t中移除并返回最后一个元素
    return (assert(remove(t), "empty zone stack"))
  end
  end
})
