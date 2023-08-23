---用元表的__index元方法来实现对象的继承关系，将对象与模块关联
-- 创建一个空表作为模块的主体
local _M = {}

-- 创建一个元表用于存储数据
_M.mt = {}

-- 设置数据的方法
_M.set = function(self, key ,value)
  self.mt[key] = value
end

-- 获取数据的方法
_M.get = function(self, key)
  return self.mt[key]
end

-- 获取所有数据的方法
_M.getall = function(self)
  return self.mt
end

-- 创建一个新对象的方法
_M.new = function(self)
  -- 使用元表将对象与模块关联
  return setmetatable({}, {__index = _M })
end

-- 返回模块
return _M

--ai传功版本
