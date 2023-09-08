def polindrom(tekst):
    if len(tekst) == 1:
        return True
    elif tekst[0] != tekst[-1]:
        return False
    else:
        return polindrom(tekst[1:-1])

print(polindrom('adaf'))