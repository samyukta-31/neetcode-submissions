class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # from math import ceil
        # speed = 1 # minimum possible

        # while True:
        #     total_time = 0
        #     for pile in piles:
        #         total_time += ceil(pile / speed)
        #     if total_time <= h:
        #         return speed
        #     speed += 1

        # return speed

        # speed = 1

        l, r = 1, max(piles)
        min_speed = r # max possible

        while l <= r:
            speed = (l + r)//2

            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / speed)
            if total_time <= h:
                min_speed = min(min_speed, speed)
                r = speed - 1
            else:
                l = speed + 1
        return min_speed
