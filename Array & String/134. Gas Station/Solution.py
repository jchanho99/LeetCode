class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1

        tank: int = 0
        GAS: int = len(gas)
        for i, g in enumerate(gas):
            if g < cost[i]:
                continue
            else:
                correct: bool = True
                tank: int = g
                pt: int = (i+1)%GAS
                
                while correct:
                    if tank < cost[pt]: 
                        correct = False
                        break
                    else:
                        tank += gas[pt]-cost[pt]
                        if pt == i: return i 
                        pt = (pt+1)%GAS

                
            

        
# gas[i]-cost[i]+gas[i+1] if gas[i] > cost[i]
