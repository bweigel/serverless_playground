from fn.other_module import plus2


def lambda_handler(evt, ctx):
    res = plus2(5)
    print("Hello World! I am Function 2!")
    print(f"5 + 2 = {res}")
