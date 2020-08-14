import random
from pprint import pprint
from functools import cmp_to_key
import bisect


def compare_keys(elem1, elem2):
    key1, key2 = elem1[0], elem2[0]
    if len(key1) != len(key2):
        return -1 if len(key1) < len(key2) else 1
    else:
        return -1 if key1 < key2 else 1


def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1


# number_of_players = 3
number_of_players = int(input('Please, enter the number of players (maximum 26): '))
players = [*'ABCDEFGHIGKLMNOPQRSTUVWXYZ'[:number_of_players]]

subsets_points = {'': 0}
players_points = {player: 0 for player in players}
for i in range(1, 2**number_of_players):
    subset = []
    for player_number, player in enumerate(players):
        if i % (2**(player_number + 1)) >= 2**player_number:
            subset += player

    max_subsubset_points = 0
    subset_length = len(subset)
    for j in range(subset_length):
        subsubset_string = ''.join(subset[:j] + subset[j + 1:])
        subsubset_points = subsets_points[subsubset_string]
        if subsubset_points > max_subsubset_points:
            max_subsubset_points = subsubset_points

    subset_points = max_subsubset_points + random.randint(1, 100)
    subsets_points[''.join(subset)] = subset_points

    for j in range(subset_length):
        subsubset_string = ''.join(subset[:j] + subset[j + 1:])
        subsubset_points = subsets_points[subsubset_string]

        players_points[subset[j]] += (subset_points - subsubset_points) * (factorial(number_of_players - subset_length) * factorial(subset_length - 1))


for player in players_points:
    players_points[player] /= factorial(number_of_players)


print()
print('All players subsets and their points:')
subsets_points = dict(sorted(subsets_points.items(), key=cmp_to_key(compare_keys)))
for subset, subset_points in subsets_points.items():
    if subset != '':
        print(f'{subset}: {subset_points}')


print()
print('Players points:')
for player, points in players_points.items():
    print(f'{player}: {points}')
