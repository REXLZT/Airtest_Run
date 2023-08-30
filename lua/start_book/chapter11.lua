--本篇幅用于学习lua的debug调试，嗯 快完结了才开始学调试，不愧是我
local function newCounter ()
    local n = 0
    local k = 0
    return function ()
      k = n
      n = n + 1
      return n
      end
  end
  
local  counter = newCounter ()
  print(counter())
  print(counter())
  
  local i = 1
  local spx =0

  repeat
    local name, val = debug.getupvalue(counter, i)
    if name then
      print ("index", i, name, "=", val)
          if(name == "n") then
                  debug.setupvalue (counter,2,10)
          end
      i = i + 1
      local j = i +1+i 
      print("j:",j)
      spx = j+1+i+j --这里打个断点

      print("spx:",spx)
    end -- if
  until not name
  
  print(counter())
  