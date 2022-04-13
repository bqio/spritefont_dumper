from dxtkfont import Dxtkfont
from prettytable import PrettyTable
from os import path
from sys import argv, exit

if len(argv) < 2 or len(argv) > 2:
  print("Use: dump.py <spritefont_file>")
  exit()

try:
  f = Dxtkfont.from_file(argv[1])
  t = PrettyTable(['Char', 'Hex', 'Left', 'Top', 'Right', 'Bottom', 'X Offset', 'Y Offset', 'X Advance'])
  for glyph in f.glyphs:
    t.add_row([chr(glyph.char), hex(glyph.char), glyph.left, glyph.top, glyph.right, glyph.bottom, glyph.x_offset, glyph.y_offset, glyph.x_advance])

  with open('{}.txt'.format(path.basename(argv[1]).split(".")[0]), "w", encoding="utf-8") as f:
    f.write(t.get_string())
  print("Done")
except:
  print("Invalid spritefont")
  exit()