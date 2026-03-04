# 1
def a(son):
    if son > 0:
       return "Musbat"
    else:
        return "Manfi yoki 0 "


x = -10
res = a(x)
print(f"{x} soni {res}")


y = 27
re = a(y)
print(f"{y} soni {res}")


# 2
def a(son):
    if son % 2 == 0:
        return "True"
    else:
        return "False"


res = a(10)
print(res)


res1 = a(21)
print(res1)


# 3
def a(son):
    if son > 100:
        return "Katta"
    else:
        return "kichik"

res = a(99)
print(res)

res1 = a(101)
print(res1)


# 4
def a(son):
    if son > 100:
        return "Katta"
    else:
        return "Teng emas"

res = a(99)
print(res)

res1 = a(101)
print(res1)


# 5
def ruxsat(yosh):
    if yosh >= 18:
        return "Ruxsat berildi"
    else:
        return "Ruxsat berilmadi"

res = (ruxsat(19))
print(res)


res1 = (ruxsat(15))
print(res1)
