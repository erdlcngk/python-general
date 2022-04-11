## Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata hata mesajları verin
def factorial(value):
    counter = 1
    result = 1

    if(int(value) >= 0):
            while counter <= int(value):
                result = result * counter
                counter += 1
    else:
        return "Girdiğiniz 0'dan küçük olamaz."


    return result
try:
    factorial_number = input("Lütfen bir değer girdiniz: ")
    print(factorial(factorial_number))
except:
    print("Hatalı bir girdi yaptınız")