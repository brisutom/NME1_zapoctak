# autor: Tomáš Brisučiak
# úloha č. 738408, generování náhodných čísel podle zadaného rozdělení
import math
import random
import matplotlib.pyplot as plt

pi = math.pi


def zadani():
    zadana_fce = math.exp  # math.cos, math.sin, math.exp, math.log, math.atan apod.
    # alternativně zadání anonymní funkcí
    # zadanaFce = lambda x: math.exp(x)/(1+math.exp(x))
    a = -pi/2
    c = pi/2

    maximum = najdi_maximum(zadana_fce, a, c)

    i = 0
    nahodna_cisla = []

    with open('nahodnaCisla.txt', 'w') as soubor:
        while i < 10000:
            nahodne = najdi_nahodne(zadana_fce, maximum, a, c)
            nahodna_cisla.append(nahodne)
            soubor.write(str(nahodne) + "\n")
            i += 1

    plt.hist(nahodna_cisla, bins=30)
    plt.show()


def najdi_maximum(zadana_fce, a, c):
    # maximum zadane funkce je ekvivalentni minimu (-1)*fce
    f = lambda x: (-1) * zadana_fce(x)
    argmax = zlaty_rez(f, a, c)
    maximum = zadana_fce(argmax)
    return maximum


def zlaty_rez(f, a, c):
    presnost = 0.001
    w = (3-math.sqrt(5))/2  # hodnota zlateho rezu, resp. 1/phi^2

    b = a + w*(c-a)  # tip na bod b

    while (c-a) > presnost:
        if (b-a)/(c-a) < 0.5:
            d = a + (1-w)*(c-a)
        else:
            d = b
            b = a + w*(c-a)

        if f(a) >= f(b) and f(b) <= f(d):
            c = d
        else:
            a = b
            b = d

    return (c+a)/2


def najdi_nahodne(zadana_fce, maximum, a, c):
    while True:
        x = random.uniform(a, c)
        y = random.uniform(0, maximum)

        if y < zadana_fce(x):
            return x


if __name__ == "__main__":
    zadani()
