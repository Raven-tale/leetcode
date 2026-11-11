class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        total = 0
        # No type 3 items needed
        if cost1 + cost2 <= costBoth:
            total = cost1 * need1 + cost2 * need2
        # Some type 3 needed
        else:
            count_both = min(need1, need2)
            total = count_both * costBoth

            need1 -= count_both
            need2 -= count_both
            # If need extra type 1, add cheaper of type 1 n 3
            if need1 > 0:
                total += need1 * min(cost1, costBoth)
            # If need extra type 2
            if need2 > 0:
                total += need2 * min(cost2, costBoth)
        return total

        """
        Missed the split case, did brute force instead
        Solution existed, didn't have intuition for second case
        Needed to play around with example cases more
        Trust feeling of uncertainty in problem
        """

class SolutionSlow:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # Works, but too slow
        count_1 = need1
        count_2 = need2
        count_both = 0

        # count_both is 0
        total = count_1 * cost1 + count_2 * cost2
        print(count_1, count_2, count_both, total)

        # count_both is <= max need
        for count_both in range(1, max(need1, need2) + 1):
            if count_1 > 0:
                count_1 -= 1
            if count_2 > 0:
                count_2 -= 1
            curr_cost =  count_1 * cost1 + count_2 * cost2 + count_both * costBoth
            if total > curr_cost:
                total = curr_cost
            print(count_1, count_2, count_both, total)

        return total
