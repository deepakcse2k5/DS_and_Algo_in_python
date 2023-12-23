
def power(base,expo):
    assert base>=0 and expo>=0 and int(base)== base and int(expo)==expo,"base and expo should be positive integer"
    if expo==0:
        return 1
    elif expo==1:
        return base
    return base*power(base,expo-1)



print(power(2,5))