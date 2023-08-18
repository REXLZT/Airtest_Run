foo = function ()
    return 
end

function maxNumber(a, b)
    
	if a > b then
		return a
	else
		return b
	end
end


local testFunc = maxNumber

local foo = testFunc

print(foo)

print(testFunc(1000,100));