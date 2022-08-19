for test_case in range(1, int(input())+1):
    N = int(input())
    card = input().split()
    perfact_suffle_card = []
    half = N//2
    if N % 2 == 1:
        for idx in range(half):
            perfact_suffle_card.append(card[idx])
            perfact_suffle_card.append(card[idx + half + 1])
        perfact_suffle_card.append(card[half])
    else:
        for idx in range(half):
            perfact_suffle_card.append(card[idx])
            perfact_suffle_card.append(card[idx + half])
    print(f'#{test_case}', *perfact_suffle_card)