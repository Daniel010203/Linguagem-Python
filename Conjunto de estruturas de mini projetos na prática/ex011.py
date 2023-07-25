#Faça um programa que leia a largura e a altura de uma parede em metros,calcule sua área e a quantidade de tinta necessária para pinta-la.Cada litro de tinta pinta apenas 2m².
l = float(input("Qual a largura da parede? "))
a = float(input("Qual a altura da parede? "))
area = l * a
print("Sua parede tem a dimensão de {}x{} e sua área é de {}m²".format(l,a,area))
t = (l*a)/2
print("Para pintar essa parede,você precisará de {}l de tinta.".format(t))
