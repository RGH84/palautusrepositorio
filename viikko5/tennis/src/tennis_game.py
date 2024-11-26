class TennisGame:
    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]
    DEUCE_SCORE = 3
    WINNING_DIFFERENCE = 2
    ADVANTAGE_DIFFERENCE = 1

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def is_tie(self):
        return self.m_score1 == self.m_score2

    def is_endgame(self):
        return self.m_score1 >= self.DEUCE_SCORE + 1 or self.m_score2 >= self.DEUCE_SCORE + 1

    def tie_score(self):
        if self.m_score1 < self.DEUCE_SCORE:
            return f"{self.SCORE_NAMES[self.m_score1]}-All"
        return "Deuce"

    def endgame_score(self):
        difference = self.m_score1 - self.m_score2
        if difference == self.ADVANTAGE_DIFFERENCE:
            return "Advantage player1"
        elif difference == -self.ADVANTAGE_DIFFERENCE:
            return "Advantage player2"
        elif difference >= self.WINNING_DIFFERENCE:
            return "Win for player1"
        return "Win for player2"

    def regular_score(self):
        return f"{self.SCORE_NAMES[self.m_score1]}-{self.SCORE_NAMES[self.m_score2]}"

    def get_score(self):
        if self.is_tie():
            return self.tie_score()
        elif self.is_endgame():
            return self.endgame_score()
        return self.regular_score()
