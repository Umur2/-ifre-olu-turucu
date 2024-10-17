import random
sifre ="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

soru = int(input('parolanız ne kadar uzun olsun'))

sifreler =''

for i in range(soru):
    sifreler += random.choice(sifre)
print(sifreler)   
