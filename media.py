print("----------------------------")
print("=====*SISTEMA DE NOTAS*=====")
print("----------------------------")

n1 = float(input("Digite a primeira nota: "))
while n1 > 10.0:
    n1 = float(input("Nota inválida, Digite novamente a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
while n2 > 10.0:
    n2 = float(input("Nota inválida, Digite novamente a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
while n3 > 10.0:
    n3 = float(input("Nota inválida, Digite novamente a terceira nota: "))

media = (n1+n2+n3)/3

if media >= 7.0:
    print(f"Aprovado! sua média foi: {media}")
elif media < 7.0 and media >= 3.5:
    print(f"Você irá realizar a 4ª prova, pois sua media foi: {media}")
    n4 = float(input("Digite a nota da prova final: "))
    final =(media+n4)/2
    if final > 5.0:
        print("Aprovado!")
    else:
        print("Reprovado!")
else:
    print(f"Reprovado! sua média foi: {media}")




