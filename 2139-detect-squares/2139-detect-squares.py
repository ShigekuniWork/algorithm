class DetectSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
            px, py = point
            res = 0

            for x, y in list(self.ptsCount.keys()):
                dx, dy = x - px, y - py
                
                if abs(dx) != abs(dy) or dx == 0:
                    continue
                
                point_C = (px, y)
                point_D = (x, py)
                
                res += self.ptsCount[(x, y)] * self.ptsCount[point_C] * self.ptsCount[point_D]
                
            return res
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)