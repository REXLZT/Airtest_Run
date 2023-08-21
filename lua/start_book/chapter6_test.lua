local m = require("lua.start_book.mymodule") --给加载的模块定义一个别名变量m，方便调用
--用require来加载，用官方的提示就是 “You can treat `import` as `require` by setting"
print(m.VERSION)
print(m.getName())

--试下函数的调用
print(m.constant)
m.func3()
--这里还是得用公共方法fun3()去调用fun2()

