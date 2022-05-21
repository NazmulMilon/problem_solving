'''def show_excitement():
    # Your code goes here!
    str = "I am super excited for this course!"
    return (str+ " ")*5


print(show_excitement())'''


def show_excitement(str,n):
    if(n==0):
        return str
    else:
        #return the str N times
        return str*n


str="I am super excited for this course!"

print(show_excitement(str,5))
