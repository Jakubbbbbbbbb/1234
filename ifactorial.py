def ifactorial():
    n=float(input("Podaj liczbę z której policzymy silnię:"))
    x=1
    nsilnia=1
    while x<(n+1):
        nsilnia=x*nsilnia
        x=x+1
    print(f"Silnia n wynosi: {nsilnia:.2f}")
ifactorial()
        
