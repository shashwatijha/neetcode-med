class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1;
        maxp = 0;

        while r<len(prices):
            
            if(prices[l]<prices[r]):
               
                profit = abs(prices[l]-prices[r])
                print(profit)
                maxp = max(maxp, profit)
            else:
                l = r;
            
            r= r+1;
        return maxp;
