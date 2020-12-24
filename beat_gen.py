#----Beat Generator----
#infinate Generator

#non generator example
def current_beat(max):
    max
    nums = (1,2,3,4)
    i = 0
    result = []
    while len(result) <= max:
        if i >= len(nums): i = 0
        result.append(nums[i])
        i += 1
    return result

print(current_beat(4))

#generator example
def current_beat2():
    nums = (1,2,3,4)
    i = 0 
    while True:
        if i >= len(nums): i = 0
        yield nums[i]
        i += 1

#---generator expressions---
def nums():
    for num in range(1,10):
        yield num
g = nums()
#refactor into expression
g2 = (num for num in range(1,10))
