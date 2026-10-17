class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks).values()
        maxf = max(freq)
        cnt = sum(1 for f in freq if f == maxf)
        return max(len(tasks), (maxf - 1) * (n) + cnt)