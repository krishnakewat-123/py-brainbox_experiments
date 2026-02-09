print("1. Creating a tuple using parentheses")
tuple1 = (10, 20, 30)
print("Tuple 1:", tuple1)

print("\n2. Creating a tuple without parentheses (tuple packing)")
tuple2 = 40, 50, 60
print("Tuple 2:", tuple2)

print("\n3. Creating a single-element tuple")
tuple3 = (100,)   # comma is important
print("Tuple 3:", tuple3)

print("\n4. Creating a tuple using tuple() constructor")
tuple4 = tuple([1, 2, 3, 4])
print("Tuple 4:", tuple4)

print("\n5. Creating a tuple using range()")
tuple5 = tuple(range(1, 6))
print("Tuple 5:", tuple5)

print("\n6. Creating a tuple with mixed data types")
tuple6 = (1, "Python", 3.14, True)
print("Tuple 6:", tuple6)
