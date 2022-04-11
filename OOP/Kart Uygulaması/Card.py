class Card:

    def __init__(self,type, value):
        self.type = type
        self.value = value
        # self.type = type
        # self.value = value

    def kartiGetir(self):

        return f"{self.type} {self.value}"

    # def __repr__(self):
    #     return f"{self.type} {self.value}"

# kartiGetir() methodu yerine __repr__ methodu da kullanılabilir. __repr__ methodu sayesinde obje çağırıldığında ram'deki adresi
# dönmek yerine doğrudan return olarak ayarlanmış değer dönecektir.
