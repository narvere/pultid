pult_desriction = 'https://pulty.tv/images/products/watermark/55b5298133649.jpg'
addr = '/image/'
print(addr+pult_desriction.split('/')[-1])
#
# if 'пульт' in pult_desriction:
#     pult_desriction = pult_desriction.replace("пульт", " пульт ")
# if 'Пульт' in pult_desriction:
#     pult_desriction = pult_desriction.replace("Пульт", " Пульт ")
# if 'Данный' in pult_desriction:
#     pult_desriction = pult_desriction.replace("Данный", " Данный ")
# if 'домашний' in pult_desriction:
#     pult_desriction = pult_desriction.replace("домашний", " домашний ")
#
#
# if len(pult_desriction) > 0:
#     pult_desriction = pult_desriction.split()
#     pult_desriction[0] = pult_desriction[0].title()
#     if pult_desriction[0] == 'Bbk':
#         pult_desriction[0].upper()
#     pult_desriction = " ".join(pult_desriction)
# if ' , ' in pult_desriction:
#     pult_desriction = pult_desriction.replace(" , ", ", ")
# if " ." or " . " in pult_desriction:
#     pult_desriction = pult_desriction.replace(" .", ". ")
#
#     pult_desriction = " ".join(pult_desriction.split())

# if pult_desriction[0].islower():
#     pult_desriction.title()

print(pult_desriction)
