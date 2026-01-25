class Player:
    def __init__(self, name: str, score: int) -> None:
        self.name = name
        self.score = score

    def __repr__(self) -> str:
        return f"Player({self.name}, {self.score})"

    def comparator(a, b):
        # First compare using scores
        if a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        else:
            # Compare by name if scores are tied
            if a.name < b.name:
                return -1
            elif a.name > b.name:
                return 1
            else:
                return 0
