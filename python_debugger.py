import pdb
'''Python Debugger'''
x = [1,3,4]
y = 2
z = 3

result = y + z
print(result)
result2 = y+x
print(result2)

# Set a trace using Python Debugger
# This will basically pause the code at the point of the trace and check if anything is wrong
pdb.set_trace()
