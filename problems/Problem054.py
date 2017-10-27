def main():
    with open('inputs\p054_poker.txt') as file:
        contents = [line.rstrip().split() for line in file.readlines()]
    
    p1_count = 0
    for hand in contents:
        player1 = hand[:len(hand) // 2]
        player2 = hand[len(hand) // 2:]
        
        rank1 = rank(player1)
        rank2 = rank(player2)
        
        if rank1 > rank2:
            p1_count += 1
            
    print(p1_count)
    
def rank(hand):
    values = get_values(hand)
    suits = [card[1] for card in hand]
    
    # check for straight
    ordered_values = sorted(values)
    straight = True
    for i in range(1, len(values)):
        if ordered_values[i] != ordered_values[i-1] + 1:
            straight = False
            break
    
    # check for flush/straight flush/royal flush
    if len(set(suits)) == 1:
        if straight:
            return 8 + (min(values) / 100)
        else:
            return 5 + get_value_dump(values)
    elif straight:
        return 4 + (min(values) / 100)
            
    # check for any kinds of repeated cards
    if len(set(values)) < 5:
        pair_count = 0
        pairs = []
        for v in set(values):
            if values.count(v) == 4:
                return 7 + (v / 100) + (get_value_dump(values) / 100)
            elif values.count(v) == 3 and len(set(values)) == 2:
                return 6 + (v / 100) + (get_value_dump(values) / 100)
            elif values.count(v) == 3:
                return 3 + (v / 100) + (get_value_dump(values) / 100)
            elif values.count(v) == 2:
                pair_count += 1
                pairs.append(v)
        pairs = sorted(pairs, reverse=True)
        if pair_count == 2:
            return 2 + (pairs[0] / 100) + (pairs[1] / 10000) + (get_value_dump(values) / 10000)
        elif pair_count == 1:
            return 1 + (pairs[0] / 100) + (get_value_dump(values) / 100)
    else:
        return get_value_dump(values)

# Returns the part of the rank after the decimal point, based on the cards not in a pair/three of a kind/etc
# Values list must be sorted ascending
def get_value_dump(values):
    rank = '0.'
    for v in sorted(values, reverse=True):
        if v < 10:
            rank += '0' + str(v)
        else:
            rank += str(v)
    return float(rank)
        
def get_values(hand):
    values = [card[0] for card in hand]
    
    # turn all values into ints
    for i in range(len(values)):
        if values[i].isdigit():
            values[i] = int(values[i])
        elif values[i] == 'T':
            values[i] = 10
        elif values[i] == 'J':
            values[i] = 11
        elif values[i] == 'Q':
            values[i] = 12
        elif values[i] == 'K':
            values[i] = 13
        elif values[i] == 'A':
            values[i] = 14
            
    return values
            
if __name__ == '__main__':
    main()