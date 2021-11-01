#A tool to calculate how many files are contained in each folder including subfiles and directories as well
#its ususal easier using recursive function than for or while loop

#Another IT example of recursive function is anything that deal with gruops of users that can contain other group
#We see this alot in administrative tools like Active directory and LDAP
#Its important to call out that they is a maximum recursive function call you can call out,
#In python by default its 1000 times 

def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)

factorial(1000)