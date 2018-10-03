

def equacao2grau(a=1, b=1, c=1):
    delta = b**2 - (4 * a * c)
    x1 = -b + (delta ** 0.5) / (2 * a)
    x2 = -b - (delta ** 0.5) / (2 * a)
    return x1, x2