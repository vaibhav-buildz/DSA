from typing import List

class Solution:
    def countGroups(self, position: List[int], speed: List[int], distance: int) -> int:
        n = len(position)

        # Step 1: collapse instant (t=0) merges based on adjacent original gaps
        reduced_speed = []
        last_pos = None
        for i in range(n):
            if last_pos is not None and position[i] - last_pos <= distance:
                reduced_speed[-1] = speed[i]   # merge: takes rightmost speed
                last_pos = position[i]
            else:
                reduced_speed.append(speed[i])
                last_pos = position[i]

        # Step 2: right-to-left, merge if a group behind is faster (eventually catches up)
        count = 0
        last_speed = None
        for spd in reversed(reduced_speed):
            if last_speed is None or spd <= last_speed:
                count += 1
                last_speed = spd
            # else: spd > last_speed -> catches up and merges, discard

        return count