BITS = 8
MIN = -128
MAX = 127


def to_binary(n):
    return format(n & 0xFF, '08b')


def binary_to_signed(b):
    value = int(b, 2)
    if value & 0x80:
        value -= 256
    return value


def add_binary(a, b):
    result = (a + b) & 0xFF
    return format(result, '08b')


def signed_operation(a, b, operator):
    if operator == '+':
        result = a + b
    else:
        result = a - b

    binary_result = to_binary(result)
    signed_result = binary_to_signed(binary_result)

    overflow = result < MIN or result > MAX

    print("Operand 1 :", to_binary(a))
    print("Operand 2 :", to_binary(b))
    print("Operation  :", operator)
    print("Result     :", binary_result)
    print("Decimal    :", signed_result)
    print("Overflow   :", "Yes" if overflow else "No")
    print()


print("(a) 45 - (+19)")
signed_operation(45, 19, '-')

print("(b) (-35) - (-12)")
signed_operation(-35, -12, '-')
