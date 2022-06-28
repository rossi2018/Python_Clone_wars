#Inner functions, also known as nested functions, are functions that you define inside other functions. 
#In Python, this kind of function has direct access to variables and names defined in the enclosing function. 
#Inner functions have many uses, most notably as closure factories and decorator functions

# One other pretty cool reason for nesting functions is the idea of a closure. This means that the nested or 
# inner function remembers the state of its enclosing scope when called. Thus, anything defined locally in the 
# enclosing scope is available to the inner function even when the outer function has finished execution.

def three_shouts(word1,word2,word3):
    """ Return a tuple of strings
    concatenated with '!!!'"""
    def inner(word):
        """Return a string concatenated with '!!!'"""
        return word + '!!!'

    #Return a tuple of strings
    return(inner(word1),inner(word2),inner(word3))

print(three_shouts('a','b','c'))

#second example
# Define echo
def echo(n):
    """Return the inner_echo function."""

    # Define inner_echo
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word

    # Return inner_echo
    return inner_echo

# Call echo: twice
twice = echo(2)

# Call echo: thrice
thrice = echo(3)

# Call twice() and thrice() then print
print(twice('hello '), thrice('hello '))
