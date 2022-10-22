class Solution(object):
    
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        # Binary search: search for the start time that after the current end time
        # Bottom-up DP
        # Maximum profit that can be achieved by scheduling non-confliting jobs between i and the end of array
        # memo[i] = profit[i] + memo[next index] schedule job at index i 
        # memo[i] = memo[i + 1] skipping job at index i
        # Why bottom up? Iterative manner and faster than top-down
        # Create job dictionary
        jobs = []
        for i in range(len(profit)):
            jobs.append([startTime[i], endTime[i], profit[i]])
        # Sort jobs according to the starttime
        jobs.sort(key = lambda x : x[0])
        
        sorted_start = []
        for i in range(len(jobs)):
            sorted_start.append(jobs[i][0])
        
        memo = [0 for i in range(len(profit))]
        for i in range(len(profit) - 1, -1, -1):
            # current profit of the current job
            curr_profit = 0
            
            # Search of the valid next starttime (end, end of array)
            next_pos = bisect.bisect_left(sorted_start, jobs[i][1], i + 1, len(jobs))
            # If there is no next job valid, use its own profit. Otherwise, add the memo of next job
            if next_pos == len(jobs):
                curr_profit = jobs[i][2]
            else:
                curr_profit = jobs[i][2] + memo[next_pos]
                
            # Update memo list
            if i == len(profit) - 1:
                memo[i] = curr_profit
            else:
                memo[i] = max(curr_profit, memo[i + 1])
            
        return memo[0]
