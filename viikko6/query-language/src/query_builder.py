from matchers import And, HasAtLeast, PlaysIn, Not, All, HasFewerThan, Or


class QueryBuilder:
    def __init__(self, matcher=None):
        self.matcher = matcher or All()

    def plays_in(self, team):
        return QueryBuilder(And(self.matcher, PlaysIn(team)))

    def has_at_least(self, value, attribute):
        return QueryBuilder(And(self.matcher, HasAtLeast(value, attribute)))

    def has_fewer_than(self, value, attribute):
        return QueryBuilder(And(self.matcher, HasFewerThan(value, attribute)))

    def one_of(self, *matchers):
        return QueryBuilder(Or(*matchers))

    def build(self):
        return self.matcher
