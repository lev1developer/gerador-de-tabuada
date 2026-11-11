import time

print("Bem-vindo ao gerador de tabuada!")
time.sleep(1.5)

tabuada = int(input("Digite um número para ver a tabuada: "))
print(f"Tabuada do {tabuada}:")

for i in range(1, 11):
    print(f"{tabuada} x {i} = {tabuada * i}")



