def main(array, k):
    items = set()
    for elem in array:
        if k - elem in items:
            return True
        items.add(elem)
        
    return False


print(main([], 17))
print(main([10, 15, 3, 7], 17))
print(main([10, 15, 3, 4], 17))

assert not main([], 17)
assert main([10, 15, 3, 7], 17)
assert not main([10, 15, 3, 4], 17)
