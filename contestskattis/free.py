
max_so_far = None
while True:
    n = input()
    if n=="$":
        break
    n = int(n)
    if (max_so_far is None) or (n >max_so_far):
        max_so_far= n

print("The maxium number is ",max_so_far)