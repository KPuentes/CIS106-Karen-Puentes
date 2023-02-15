#input phase
fc = float(input("Enter total fixed costs:$"))
ppu = float(input("Enter price per unit:$"))
cpu = float(input("Enter cost per unit:$"))
#process phase
breakeven = fc / (ppu - cpu)
#output phase
print("The breakeven point is at", breakeven)