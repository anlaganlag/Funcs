from collections import defaultdict
class UndergroundSystem:
    def __init__(self):
        self.loc = {}
        self.time = {}
        self.start= defaultdict(float)
        self.end= defaultdict(float)
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.loc[id] = stationName
        self.time[id] = t
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        k = (self.loc[id], stationName)
        dur = t - self.time[id]
        del self.loc[id]
        del self.time[id]
        self.start[k] += dur
        self.end[k] +=1
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        k = (startStation, endStation)
        return self.start[k]/self.end[k]
