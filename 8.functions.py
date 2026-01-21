#default arguments
def greeting(name="Rafi"):
    print("Hi im , ", name)

greeting("Lamia")
greeting()

#if num of parameters are unknown
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")


#lamda function: single line function
fun = lambda a,b : a + b
print(fun(5,11))