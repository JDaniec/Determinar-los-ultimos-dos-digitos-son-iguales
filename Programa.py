print("----------------------------------------------------------------------------------------")
print("--------------Determinar si los ultimo digitos de un numero son iguales-----------------")
print("----------------------------------------------------------------------------------------")


# input

n = int(input("Digite un numero: "))

#processing
if -10 <= n <= 10:
    rta = "El numero no tiene mas de dos digitos"

else:
    d = n % 100
    f = d % 10
    g = d // 10
    if f == g:
        rta = "Los ultimos dos digitos son iguales"

    else:
        rta = "Los ultimos dos digitos no son iguales"

 # output
print("--------------------------")
print(str(rta))



