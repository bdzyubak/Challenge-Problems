# The LeagueTable class tracks the score of each player in a league. After each game, the player records their score with the record_result function.
#
# The player's rank in the league is calculated using the following logic:
#
# The player with the highest score is ranked first (rank 1). The player with the lowest score is ranked last.
# If two players are tied on score, then the player who has played the fewest games is ranked higher.
# If two players are tied on score and number of games played, then the player who was first in the list of players is ranked higher.
# Implement the player_rank function that returns the player at the given rank.

from collections import Counter
from collections import OrderedDict


class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])

    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score

    def player_rank(self, rank):
        print(self.standings)
        ranking = sorted(self.standings, key=lambda p: (
            -self.standings[p]['score'], self.standings[p]['games_played'],
            self.standings[p]['pos']))
        return ranking[rank - 1]


table = LeagueTable(['Mike', 'Chris', 'Arnold'])
table.record_result('Mike', 2)
table.record_result('Mike', 3)
table.record_result('Arnold', 5)
table.record_result('Chris', 5)
assert table.player_rank(1) == "Chris"
print('Tests passed.')
