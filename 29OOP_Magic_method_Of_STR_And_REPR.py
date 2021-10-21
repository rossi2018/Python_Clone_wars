#magic or dunder methods are names that are preceded and succeeded  by double underscores
#Example __repr__

# a=1
# print(str(a) + "11")

class CustomizedInteger:
    def __init__ (self,integer):
        self.integer=integer

    def __str__(self):
        if self.integer==4:
            return "Four"


    def __repr__(self):
        return f"CustomizedInteger ({self.integer})"


int1=CustomizedInteger(4)
print(int1)