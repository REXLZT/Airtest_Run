local _M = {}

_M.VERSION = "1.0"

_M.getName = function()
	return "get"
end

-- 定义一个常量
_M.constant = "这是一个常量"
 
-- 定义一个函数
function _M.func1()
    io.write("这是一个公有函数！\n")
end
 
local function func2()
    print("这是一个私有函数！")
end
 
function _M.func3()
    func2()
end
 
return _M

