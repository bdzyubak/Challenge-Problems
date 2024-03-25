class RecentCounter:

    def __init__(self):
        self.recent = list()

    def ping(self, t: int) -> int:
        self.recent.append(t)
        while self.recent[0] < t - 3000:
            self.recent.pop(0)

        return len(self.recent)