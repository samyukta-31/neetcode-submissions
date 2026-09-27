class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = []
        inds = []
        days = [0]*len(temperatures)
        for curr_i, temp in enumerate(temperatures):
            while temps and temp > temps[-1]:
                temps.pop()
                prev_i = inds.pop()
                days[prev_i] = curr_i - prev_i
            temps.append(temp)
            inds.append(curr_i)
        
        return days
            

