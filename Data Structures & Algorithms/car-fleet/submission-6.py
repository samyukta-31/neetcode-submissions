class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = []
        times = []
        for i in range(0,len(position)):
            combined.append((position[i], speed[i]))
        combined.sort(reverse = True)

        for i in range(len(combined)):
            # print(times)
            time = (target - combined[i][0])/combined[i][1]
            if times:
                prev_time = times[-1]
                if time > prev_time:
                    fleets += 1
                    times.append(time)
            else:
                times.append(time)
                fleets = 1
        # print(combined)
        return fleets
        
        
        
        # fleet_set = set()
        # times = []
        # fleets = 0
        # for i in range(len(position)):
        #     distance = target - position[i]
        #     time = distance / speed[i]
        #     if time not in fleet_set:
        #         fleet_set.add(time)
        #         fleets += 1
        #     times.append(time)
        # print(times)
        #     # times.append(time)
        # remove = 0
        # print(fleets)
        # for i in range(0,len(position)-1):
        #     for j in range(i+1, len(position)):
        #         # print(position[i], position[j])
        #         if (position[i] > position[j] and times[i] > times[j]) or (position[j] > position[i] and times[j] > times[i]):
        #             remove += 1
        # print(fleets, remove)
        # return max(fleets - remove, 1)

                