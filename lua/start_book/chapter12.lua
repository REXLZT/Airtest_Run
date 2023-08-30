--本篇幅用于展示如何自定义打印table，采用递归的思想 出处：https://blog.csdn.net/albertsh/article/details/52333953
local function dumptree(obj, width) --还是习惯性加

    -- 递归打印函数
    local dump_obj;
    local end_flag = {};

    local function make_indent(layer, is_end)
        local subIndent = string.rep("  ", width)
        local indent = "";
        end_flag[layer] = is_end;
        local subIndent = string.rep("  ", width)
        for index = 1, layer - 1 do
            if end_flag[index] then
                indent = indent.." "..subIndent
            else
                indent = indent.."|"..subIndent
            end
        end

        if is_end then --判断是否为最后一元素，用于加上那两个奇怪的符号
            return indent.."└"..string.rep("─", width).." "
        else
            return indent.."├"..string.rep("─", width).." "
        end
    end

    local function make_quote(str)
        str = string.gsub(str, "[%c\\\"]", {
            ["\t"] = "\\t",
            ["\r"] = "\\r",
            ["\n"] = "\\n",
            ["\""] = "\\\"",
            ["\\"] = "\\\\",
        })
        return "\""..str.."\""
    end

    local function dump_key(key)
        if type(key) == "number" then
            return key .. "] "
        elseif type(key) == "string" then
            return tostring(key).. ": "
        end
    end

    local function dump_val(val, layer)
        if type(val) == "table" then
            return dump_obj(val, layer)
        elseif type(val) == "string" then
            return make_quote(val)
        else
            return tostring(val)
        end
    end

    local function count_elements(obj)
        local count = 0
        for k, v in pairs(obj) do
            count = count + 1
        end
        return count
    end

    dump_obj = function(obj, layer)
        if type(obj) ~= "table" then
            return count_elements(obj)
        end

        layer = layer + 1
        local tokens = {}
        local max_count = count_elements(obj)
        local cur_count = 1
        for k, v in pairs(obj) do
            local key_name = dump_key(k)
            if type(v) == "table" then
                key_name = key_name.."\n"
            end
            table.insert(tokens, make_indent(layer, cur_count == max_count) 
                .. key_name .. dump_val(v, layer))
            cur_count = cur_count + 1
        end

        -- 处理空table
        if max_count == 0 then
            table.insert(tokens, make_indent(layer, true) .. "{ }")
        end

        return table.concat(tokens, "\n")
    end

    if type(obj) ~= "table" then
        return "the params you input is "..type(obj)..
        ", not a table, the value is --> "..tostring(obj)
    end

    width = width or 2
    return "root-->"..tostring(obj).."\n"..dump_obj(obj, 0)
end



--下面是个给了个table来试??

local t = {
    a = 1,
    b = 2,
    [1] = 34,
    ["1"] =56,
    pos = {
        x = 100,
        y = 200,
        z = 400,
        target = {
            pos = {
                x = 666,
                y = 456,
            },
            src = "name",
            dest = nil,
            from = "china \n beijing"
        }
    },  
    [88] = 88888,
    [9.7] = 22222,
    func = function()
        print("this is a function")
    end,
    ["key"] = "value",
    [98] = {
        name = "albert",
        age = "18",
    },
    ["98"] = {},
}

-- 调用函数运行
print(dumptree(t))

print("├├├├")--孩得是gbk用着顺手
