binary_str = "1011001"
k=3
rotated = binary_str[-k:] + binary_str[:-k]
decimal_value = int(rotated, 2)
print(decimal_value)
