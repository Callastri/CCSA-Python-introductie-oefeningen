t = float(input())

a, b, c = 0, 0, 0
temp1 = 0
temp2 = 0

for i in range(0.01, t):
    a = i
    temp1 = t - a
    print(f"€{temp1:.2f} = €{t:.2f} - €{a:.2f}")
    while b >= a and b < t and b <= 3.00:
      c = temp1 - b
      print(f"€{c:.2f} = €{temp1:.2f} - €{b:.2f}")

      sum = a + b + c
      print(f"€{sum:.2f} = €{a:.2f} + €{b:.2f} + €{c:.2f}")

      multi = a * b * c
      print(f"€{multi:.2f} = €{a:.2f} x €{b:.2f} x €{c:.2f}")


      if sum == multi:
          print(f"€{a:.2f} + €{b:.2f} + €{c:.2f} = €{a:.2f} x €{b:.2f} x €{c:.2f} = €{t:.2f}")
      else:
        b += 0.01
        print(f"b = €{b:.2f}")
      
    a += 0.01  