
def decor(result_function):
    def Distinction(marks):
        for m in marks:
            if m>=75:
                print("You Got Distinction")
        return result_function(marks)
    return Distinction

@decor
def result(marks):
    for m in marks:
        if m>=33:
            pass   
        else:
            print("FAIL")
            break
    else:
        print("PASS")
result([33,35,34,35,34])
