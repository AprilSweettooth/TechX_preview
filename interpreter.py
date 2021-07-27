def interpreter(code):
    var = []
    answer = []
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    def operation(value_list, operator):
        if isinstance(value_list[0], str):
            for x in range(0, len(var)):
                if value_list[0] == var[x][0]:
                    value_list[0] = var[x][1]
        if isinstance(value_list[1], str):
            for y in range(0, len(var)):
                if value_list[1] == var[y][0]:
                    value_list[1] = var[y][1]
        if operator == "+":
            return int(value_list[0]) + int(value_list[1])
        if operator == "-":
            return int(value_list[0]) - int(value_list[1])
        if operator == "*":
            return int(value_list[0]) * int(value_list[1])
        if operator == "/":
            return int(value_list[0]) / int(value_list[1])

    def set(new_value):
        change = False
        for x in range(0, len(var)):
            if new_value[0] == var[x][0]:
                var[x][1] = new_value[1]
                change = True
        if change is False:
            var.append(new_value)

    def get_value(name):
        if any(x in name for x in numbers):
            answer.append(int(name))
        else:
            for x in range(0, len(var)):
                if name == var[x][0]:
                    answer.append(int(var[x][1]))

    li = list(code.split("\n"))
    for i in range(0, len(li)):
        if "=" in li[i]:
            def is_operator(operator):
                if "mul" in operator or "div" in operator or "sub" in operator or "add" in operator:
                    return True
                else:
                    return False
            if is_operator(li[i]) is False:
                lines = "".join(li[i].split())
                var_name, var_value = lines.split("=")[0], lines.split("=")[1]
                v = [var_name, var_value]
                set(v)
            else:
                operation_line = "".join(li[i].split())
                result = operation_line.split("=")[0]
                if "sub" in operation_line:
                    value = [li[i].split()[-2], li[i].split()[-1]]
                    result_value = operation(value, "-")
                    v = [result, result_value]
                    set(v)
                elif "add" in operation_line:
                    value = [li[i].split()[-2], li[i].split()[-1]]
                    result_value = operation(value, "+")
                    v = [result, result_value]
                    set(v)
                elif "div" in operation_line:
                    value = [li[i].split()[-2], li[i].split()[-1]]
                    result_value = int(operation(value, "/"))
                    v = [result, str(result_value)]
                    set(v)
                elif "mul" in operation_line:
                    value = [li[i].split()[-2], li[i].split()[-1]]
                    result_value = operation(value, "*")
                    v = [result, result_value]
                    set(v)
        else:
            output = li[i].replace("output", "")
            output = output.split()
            get_value(output[0])
    print(answer)


interpreter('a = 5\nb = 10\nc = add a b\noutput c\noutput b')
interpreter('  my_var   =29\nout= 1\nc =  add my_var out\noutput    c')
interpreter('output   15\nfoo = div 35 7\noutput foo')
interpreter('a = 2\noutput a\na = mul a a\noutput a\na = mul a a\noutput a')
interpreter('var = 10\ntest=20  \nw=sub test var\noutput w\noutput w')

# answers
'''
[15, 10]
[30]
[15, 5]
[2, 4, 16]
[10, 10]
'''