sheep_size = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Linh and these are my ship sizes")
print(sheep_size)

biggest = max(sheep_size)
print("Now my biggest sheep has size", biggest, "let's shear it")

index = sheep_size.index(biggest)
sheep_size[index] = 8
print("After shearing, here is my flock")
print(sheep_size)

sheep_size_len = len(sheep_size)
for i in range(len(sheep_size)):
    sheep_size[i] += 50
print("One month has passes, now here is my flock")
print(sheep_size)

