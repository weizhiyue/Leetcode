class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        # If the length of s and goal doesn't match, return False
        if len(s) != len(goal):
            return False
        
        # If s and goal are the same, need two repeated characters
        if s == goal:
            if len(set(s)) < len(s):
                return True
            else:
                return False
        
        # If s and goal are not the same
        # s[i] == goal[j] and s[j] == goal[i]
        diff = [[curr_s, curr_goal] for curr_s, curr_goal in zip(s, goal) if curr_s != curr_goal]
        return len(diff) == 2 and diff[0] == diff[1][::-1]
