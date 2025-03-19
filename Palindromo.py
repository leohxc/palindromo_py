# Palíndromo
def palindromo():
    palabrauno = input("Ingrese una palabra: ")
    print(f"La palabra {palabrauno} es palíndromo: {palabrauno == palabrauno[::-1]}")
palindromo()