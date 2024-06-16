x = input("kola, spring, sprit, water, xl: ")
if x == "kola":
    print(9)
    a = int(input("enter namber shekel: "))
    b = int(input("enter namber shnekel: "))
    c = int(input("enter namber 5 shekel: "))
    d = int(input("enter namber 10 shekel: "))
    sum_ = a + b * 2 + c * 5 + d * 10
    excess = sum_ - 9
elif x == "spring":
    print(8)
    a = int(input("enter namber shekel: "))
    b = int(input("enter namber shnekel: "))
    c = int(input("enter namber 5 shekel: "))
    d = int(input("enter namber 10 shekel: "))
    sum_ = a + b * 2 + c * 5 + d * 10
    excess = sum_ - 8
elif x == "sprit":
    print(8)
    a = int(input("enter namber shekel: "))
    b = int(input("enter namber shnekel: "))
    c = int(input("enter namber 5 shekel: "))
    d = int(input("enter namber 10 shekel: "))
    sum_ = a + b * 2 + c * 5 + d * 10
    excess = sum_ - 8
elif x == "water":
    print(5)
    a = int(input("enter namber shekel: "))
    b = int(input("enter namber shnekel: "))
    c = int(input("enter namber 5 shekel: "))
    d = int(input("enter namber 10 shekel: "))
    sum_ = a + b * 2 + c * 5 + d * 10
    excess = sum_ - 5
elif x == "xl":
    print(5)
    a = int(input("enter namber shekel: "))
    b = int(input("enter namber shnekel: "))
    c = int(input("enter namber 5 shekel: "))
    d = int(input("enter namber 10 shekel: "))
    sum_ = a + b * 2 + c * 5 + d * 10
    excess = sum_ - 5
else:
    print("error")
    quit()
print(excess)
eser_shekel = excess // 10
hamesh_shekel = (excess - eser_shekel * 10) // 5
shnekel = (excess - eser_shekel * 10 - hamesh_shekel * 5) // 2
shekel = (excess - eser_shekel * 10 - hamesh_shekel * 5 - shnekel * 2) // 1
print("eser_shekel:", eser_shekel)
print("hamesh_shekel:", hamesh_shekel)
print("shnekel:", shnekel)
print("shekel:", shekel)
print("tenk you bro")
