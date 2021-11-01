file_count={"jpg":10,"txt":14,"csv":2,"py":23}
for extension in file_count:
    print(extension)

#Use item method to access the key, value pairs in the dictionary

for ext,amount in file_count.items():
    print("There are {} files with the .{} extension" .format(amount,ext)) 

#When you are interested with the key or value only use the method

print(file_count.keys())
print(file_count.values())

for value in file_count.values():
    print(value)