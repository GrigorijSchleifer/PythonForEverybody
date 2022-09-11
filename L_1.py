
# while loop with continue
while True:
    inp = input("> ")
    if inp == '#':
        print(f'first sign of the input is {inp[0]}')
        continue 
    if inp == 'done':
        print(inp)
        break


# codewars first method for chaining
def fct_one(x): 
    return x * 10
def fct_two(x): 
    return x * 10

functions_list = [fct_one, fct_two]

def chain(value, functions: list) -> int:
    for i in functions:
        value = i(value)
    return print(value)

chain(100, functions_list)