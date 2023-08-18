print("thread create")
a = 1314
fun = function()
	print("abc")
end

co = coroutine.create( fun )
print(type(co))
co1 = coroutine.status( co )
print(co1)
co = coroutine.running( fun )
co2 = coroutine.status( co )
print(co2)

print("start po time")

local function fun2(a)
    print("a=",a)
    -- coroutine.yield( a )
    --这里挂起和不挂起貌似不影响
end

po = coroutine.wrap( fun2 )
--po果然是返回个函数，而且通过实现变量的传递
-- coroutine.yield( po )
print (type(po))
--local po1 = coroutine.status( po )
po(a)

--coroutine.wrap返回的是一个函数，而不是协程本身，因此需要通过调用该函数来执行协程，并使用coroutine.running函数来获取当前正在运行的协程


-- co = coroutine.create(fun)
-- --协程的本质是一个线程对象
-- print(co)
-- print(type(co))				--thread

-- --coroutine.wrap()
-- co2 = coroutine.wrap(fun)
-- print(co2)
-- print(type(co2))			--function

-- print("thread run")
-- --第一种方式 对应的 是通过 create创建的协程
-- coroutine.resume(co)
-- --第二种方式
-- co2()

-- print("thread guaqi")
