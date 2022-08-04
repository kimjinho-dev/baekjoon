xA, yA, xB, yB, xC, yC = map(int, input().split())

if xA == xB:
    AB_slope = 'col'
    AB_length = abs(yA - yB)
elif yA == yB:
    AB_slope = 'row'
    AB_length = abs(xA - xB)
else:
    AB_slope = (xA - xB) / (yA - yB)
    AB_length = ((xA - xB) ** 2 + (yA - yB) ** 2) ** (1 / 2)

if xB == xC:
    BC_slope = 'col'
    BC_length = abs(yB - yC)
elif yB == yC:
    BC_slope = 'row'
    BC_length = abs(xB - xC)
else:
    BC_slope = (xB - xC) / (yB - yC)
    BC_length = ((xB - xC) ** 2 + (yB - yC) ** 2) ** (1 / 2)

if xC == xA:
    CA_slope = 'col'
    CA_length = abs(yC - yA)
elif yC == yA:
    CA_slope = 'row'
    CA_length = abs(xC - xA)
else:
    CA_slope = (xC - xA) / (yC - yA)
    CA_length = ((xC - xA) ** 2 + (yC - yA) ** 2) ** (1 / 2)

A_lenght = AB_length + CA_length
B_lenght = AB_length + BC_length
C_lenght = BC_length + CA_length
lenghts = [A_lenght, B_lenght, C_lenght]

if AB_slope == BC_slope:
    print(-1.0)
else:
    print((max(lenghts) - min(lenghts)) * 2)