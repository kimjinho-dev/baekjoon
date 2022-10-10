for test_case in range(1, 1+int(input())):
    N = int(input())
    result = 0
    atoms = [list(map(int, input().split())) for _ in range(N)]
    d = [(0, 0.5), (0, -0.5), (-0.5, 0), (0.5, 0)]

    while len(atoms) >= 2:
        for i in range(len(atoms)):
            atoms[i][0] += d[atoms[i][2]][0]
            atoms[i][1] += d[atoms[i][2]][1]

        pos = {}
        for atom in atoms:
            try:
                pos[(atom[0], atom[1])].append(atom)
            except Exception:
                pos[(atom[0], atom[1])] = [atom]

        atoms = []
        for key in pos:
            if len(pos[key]) >= 2:
                for atom in pos[key]:
                    result += atom[3]
            else:
                if -1000 <= pos[key][0][0] <= 1000 and -1000 <= pos[key][0][1] <= 1000:
                    atoms.append(pos[key][0])

    print(f'#{test_case}', result)