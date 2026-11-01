def rol(value, positions):
    value &= 0xFF

    print("ROL process:")
    for i in range(positions):
        msb = (value >> 7) & 1
        value = ((value << 1) | msb) & 0xFF
        print("Step", i + 1, ":", format(value, '08b'))

    return value


def rcl(value, carry, positions):
    value &= 0xFF

    print("RCL process:")
    print("Initial Carry:", carry)

    for i in range(positions):
        msb = (value >> 7) & 1
        value = ((value << 1) | carry) & 0xFF
        carry = msb

        print("Step", i + 1, ":", format(value, '08b'),
              "Carry:", carry)

    return value, carry


binary = "10110110"
value = int(binary, 2)

# (a) ROL by 2 positions
print("(a) ROL 10110110 by 2")
print("Original:", binary)

result = rol(value, 2)

print("Final Result:", format(result, '08b'))
print()


# (b) RCL by 2 positions
print("(b) RCL 10110110 by 2")
print("Original:", binary)

initial_carry = 0
result, final_carry = rcl(value, initial_carry, 2)

print("Final Result:", format(result, '08b'))
print("Final Carry :", final_carry)
