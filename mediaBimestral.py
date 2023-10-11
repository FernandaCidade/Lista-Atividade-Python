#Faça um Programa que peça as 4 notas bimestrais e mostre a média.


print ("Bem-vindo ao calculo Bimestral");

primeiraNota = float(input("Digite a primeira nota: "));
segundaNota = float(input("Digite a segunda nota: "));
terceiraNota = float(input("Digite a terceira nota: "));
quartaNota = float(input("Digite a quarta nota: "));

soma = (primeiraNota + segundaNota + terceiraNota + quartaNota)/4;

print("A média bimestral é: ",soma);
