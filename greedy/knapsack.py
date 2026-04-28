def fractionalknapsack(weights,values,capacity):
    items = []
    for i in range(len(values)):
        items.append({
            'v': values[i],
            'w': weights[i],
            'ratio': values[i]/weights[i]
        })
    
    items.sort(key= lambda x:x['ratio'],reverse = True)
    total_value = 0
    for item in items:
        if capacity == 0:
            break
        if item['w']<= capacity:
            capacity-=item['w']
            total_value+=item['v']
        else:
            total_value+=item['ratio']*capacity    
            capacity = 0 
    return total_value

weights = [10,20,30]
values = [60,100,120]
capacity = 50
print(fractionalknapsack(weights,values,capacity))  ### answer is 240.0
### command to run: python greedy/knapsack.py
##maintaing the streak