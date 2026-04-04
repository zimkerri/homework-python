def kopaytma(*sonlar):
    natija = 1
    for son in sonlar:
        natija *= son
    return natija

print(kopaytma(2, 3, 4))
def talaba_info(ism, familiya, **malumotlar):
    talaba = {
        "ism": ism,
        "familiya": familiya
    }
    talaba.update(malumotlar)
    return talaba

print(talaba_info("Ali", "Valiyev", yosh=20, kurs=2))


def total_price(*narxlar, **kwargs):
    jami = sum(narxlar)

    if "discount" in kwargs:
        chegirma = kwargs["discount"]
        jami -= jami * chegirma / 100

    return jami


print(total_price(10000, 20000, 15000, discount=10))  
def join_words(*sozlar, **kwargs):
    sep = kwargs.get("sep", " ")
    return sep.join(sozlar)

print(join_words("Python", "is", "awesome", sep="-"))
