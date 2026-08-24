class StockSpanner:

    def __init__(self):
        # find the daily prie quotes for some stock and return the span of that stock's price for the current day
        # span = max number of daays where the stock was less than or equal to the price of that day

        # [7,2,1,2]
        # coutning ourselves as a day?
        # keep a running list for the span
        # previous value

        # [(100,1),(85,6)]
        self.entries = []


    def next(self, price: int) -> int:
        # todays price is price
        # O(1) time complexity?
        # return 1 if the there is no case 
        # log(n)
        span = 1
        while self.entries:
            entry = self.entries[-1]
            if entry[0] <= price:
                self.entries.pop()
                span += entry[1]
            else:
                break
        self.entries.append((price,span))
        return span
        
        
         

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)