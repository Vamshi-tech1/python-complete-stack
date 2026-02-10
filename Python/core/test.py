x=10 # global variable
def fun(): #creating a function
    x=20 # local variable
    def fun1(): #creating a function inside another function
        print(x)
    fun1() # calling fun1 function
fun() # calling Fun function # 10
print(x) # 10
