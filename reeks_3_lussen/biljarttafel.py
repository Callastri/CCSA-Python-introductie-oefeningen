h = int(input())
b = int(input())

x, y = 0, 0
dx, dy = 1, 1

while True:
  afstand_x = b - x if dx == 1 else x
  afstand_y = h - y if dy == 1 else y

  stap = min(afstand_x, afstand_y)

  x += dx * stap
  y += dy * stap

  if afstand_x == afstand_y:
    links_rechts = 'linker' if x == 0 else 'rechter'
    onder_boven = 'onder' if y == 0 else 'boven'
    print(f"{links_rechts}{onder_boven}pocket ({x}, {y})")
    break
  elif afstand_x < afstand_y:
    band = 'linkerband' if x == 0 else 'rechterband'
    dx = -dx
  else:
    band = 'onderband' if y == 0 else 'bovenband'
    dy = -dy
  print(f"{band} ({x}, {y})")
