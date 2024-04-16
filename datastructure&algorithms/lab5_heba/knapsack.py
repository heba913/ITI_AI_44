class KnapSack:
    def __init__(self,weight,value) -> None:
        self.weight=weight
        self.value=value
        self.ratio=value/weight
    

    
    def __lt__(self,other):
        return self.ratio <other.ratio


class fracKnapsack:
    def greedy(self,w,v,m,n):
        pack=[]
        for i in range(n):
            pack.append(KnapSack(w[i],v[i]))
        pack.sort(reverse=True)
        remain=m
        result=0
        while remain> 0 and i<n:
            if pack[i].weight <= remain:
                result += pack[i].value
                remain -= pack[i].weight
            else:
                result += pack[i].ratio * remain
                remain=0
            i += 1
        return result

  
weights = [2, 3, 5]
values = [10, 5, 15]
max_capacity = 8
n_items = len(weights)
knapsack_solver = fracKnapsack()
max_value = knapsack_solver.greedy(weights, values, max_capacity, n_items)
print(f"Maximum value: {max_value}")
