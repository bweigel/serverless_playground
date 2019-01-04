from fn.other_module import plus2


def handler(evt, ctx):
    res = plus2(5)
    print("Hello World! I am Function 1!")
    print(f"5 + 2 = {res}")


def handler2(evt, ctx):
    res = 2*5
    print("Hello World! I am Function 1!")
    print(f"5 * 2 = {res}")
