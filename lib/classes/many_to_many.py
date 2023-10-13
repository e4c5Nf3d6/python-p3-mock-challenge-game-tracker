class Game:
    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if hasattr(self, "title"):
            raise Exception('title cannot be changed')
        elif isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise Exception('title must be a non-empty string')

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list(set([result.player for result in Result.all if result.game == self]))

    def average_score(self, player):
        scores = [result.score for result in Result.all if result.game == self and result.player == player]
        if scores:
            return sum(scores) / len(scores)
        else:
            return 0

class Player:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception('username must be a string between 2 and 16 characters')

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list(set([result.game for result in Result.all if result.player == self]))

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return len([result for result in Result.all if result.player == self and result.game == game])
    
    @classmethod
    def highest_scored(cls, game):
        players = list(set([result.player for result in Result.all]))
        if players:
            highest_scored_player = players[0]
            for player in players:
                if game.average_score(player) > game.average_score(highest_scored_player):
                    highest_scored_player = player
            return highest_scored_player
        return None

class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if hasattr(self, 'score'):
            raise Exception('score cannot be changed')
        elif isinstance(score, int) and 1 <= score <= 5000:
            self._score = score
        else:
            raise Exception('score must be an integer between 1 and 5000')
        
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game