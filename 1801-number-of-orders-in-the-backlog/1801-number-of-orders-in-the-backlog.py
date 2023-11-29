# 1801. Number of Orders in the Backlog
# Author: Kevin Zhao
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:

        buy,sell  = [], []                                                             

        for price,amt,order in orders:                                                  
            if order: heappush(sell, ( price, amt))                                     
            else    : heappush(buy , (-price, amt))                                     
            
            while buy and sell and -buy[0][0] >= sell[0][0]:                            
                                                                                        
                (buyPrice,buyAmt), (sellPrice,sellAmt) = heappop(buy), heappop(sell)    
                                                                                        
                if   buyAmt > sellAmt: heappush(buy , (buyPrice , buyAmt -sellAmt))     
                elif buyAmt < sellAmt: heappush(sell, (sellPrice, sellAmt- buyAmt))     

        return sum(amt for _,amt in buy+sell)% (1000000007)    
