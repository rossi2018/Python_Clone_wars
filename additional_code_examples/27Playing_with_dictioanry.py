file_count={"jpg":10,"txt":14,"csv":2,"py":23}
print(file_count)
print(file_count["jpg"])
print("jpg" in file_count)
file_count["cfg"]=6
print(file_count)
file_count["csv"]=13
print(file_count)
del file_count["jpg"]
print(file_count)