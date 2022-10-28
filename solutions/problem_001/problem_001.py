def main(array, k):
    set_array = set(array)
    for elem in array:
        if k - elem in array:
            return True
    return False


print(main([], 17))
print(main([10, 15, 3, 7], 17))
print(main([10, 15, 3, 4], 17))

assert not main([], 17)
assert main([10, 15, 3, 7], 17)
assert not main([10, 15, 3, 4], 17)
