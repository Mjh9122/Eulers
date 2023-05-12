import poker.card
import poker.hand

with open('../Eulers-/txts/poker.txt') as poker_file:
    hands = poker_file.read().split('\n')
    print(hands[0])
    for h in hands:
        h = h.split(' ')
        lowers = []
        for card in h:
            lowers.append(card[0] + card[1].lower())
        h1 = lowers[:5]
        h2 = lowers[5:]
        print(h1)