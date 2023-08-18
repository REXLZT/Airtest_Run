function test1(x, y)
    return x+y;
	-- print(x+y)
	-- 后面的print如果不注释，会报错
end

function test2(x, y)
	if x > y then
		return x
	else
		return y
	end
	print("end") -- 此处的print不注释不会报错，因为return只出现在前面显式的语句块
end

-- function test3(x, y)
-- 	print(x+y)
-- 	do return end
-- 	print(x) -- 此处的print不注释不会报错，因为return由do...end语句块包含。这一行语句永远不会执行到
-- end

test1(10,11)
print("test2")
p= test2(12,11)
print("chulai",p)
print("test3")
-- test3(10,11)


---for数字型，下面是格式
-- for var = begin, finish, step do
-- 	--body
-- end
-- - `var` 从 `begin` 变化到 `finish`，每次变化都以 `step` 作为步长递增 `var`
-- - `begin`、`finish`、`step` 三个表达式只会在循环开始时执行一次 
-- - 第三个表达式 `step`是可选的，默认为 `1`
-- - 控制变量 `var` 的作用域仅在 `for` 循环内，需要在外面控制，则需将值赋给一个新的变量 
-- - 循环过程中不要改变控制变量的值，那样会带来不可预知的影响

sum = 0
for i=0,10,1 do
	sum = sum + i
end
print(sum) -- 5050




---for泛型，下面是格式 
-- 打印数组a的所有值  
-- for i,v in ipairs(a) do 
-- 	print(v) 
-- end  
---i`是数组索引值，`v`是对应索引的数组元素值。`ipairs`是`Lua`提供的一个迭代器函数，用来迭代数组。 
days = {
	"Monday",
	"Tuesday",
	"Wednesday",
	"Thursday",
	"Friday",
}

for k,v in ipairs(days) do
	print(k,v)
end