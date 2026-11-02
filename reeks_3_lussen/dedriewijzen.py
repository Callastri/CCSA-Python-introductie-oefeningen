t = float(input())
T= round (t * 100)  # bedrag omrekenen naar een geheel getal in centen om een forlus te kunnen gebruiken.


for A in range(1, T // 3 + 1):     
  # A begint bij 1 want een product met 0 zou altijd 0 geven als resultaat
  # A gaat tot T // 3 want A kan maximum 1/3 zijn van de som
  for B in range(A, (T - A) // 2 + 1):
    # B begint bij A en gaat tot maximum T - A
    C = T - A - B  # het resultlaat van C is van de som
    if A * B * C == T * 10000:     # el getal is 100 keer groter, dus 100 × 100 × 100
      a, b, c, = A / 100, B / 100, C / 100
      print(f"€{a:.2f} + €{b:.2f} + €{c:.2f} = €{a:.2f} x €{b:.2f} x €{c:.2f} = €{t:.2f}")

