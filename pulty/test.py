str = 'BBK DK1004S'

if "Возможная" in str:
    print(str[:str.index("Возможная")])
elif "Данный пульт" in str:
    print(str[:str.index("Данный пульт")])
else:
    print("str")





# print(str[:str.index("Возможная" or "Данный пульт")])