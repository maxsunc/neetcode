class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prefix sum
        if len(prices) == 1:
            return 0;
        # two pointers

        # buying pointer

        # selling pointer

        # buying pointer gets replaced if value < currentValue


        # selling pointer = max value index
        # After the buying pointer
        # before any value less than max value
        # will look for highest increase ex: 1,3,4,5,6,
        buyingPointer = 0
        sellingPointer = 1
        result = 0


        for i in range(1, len(prices)):
            if prices[sellingPointer] < prices[i]:
                # replace with higher price
                sellingPointer = i
            elif prices[sellingPointer] > prices[i]:
                # sell now cuz we hit peak!
                # only sell if not negative
                if prices[sellingPointer] - prices[buyingPointer] > 0:
                    print(f"buying at {buyingPointer} and selling at {sellingPointer}")
                    result += prices[sellingPointer] - prices[buyingPointer]
                buyingPointer = i
                sellingPointer = i+1
            # 7, 1,2,3,4,5
            if prices[buyingPointer] > prices[i]:
                # buy from here instead
                buyingPointer = i
                # selling pointer must happen after buying
                sellingPointer = i + 1


        # sell the end
        if (len(prices) - 1 >= sellingPointer):
            if prices[sellingPointer] - prices[buyingPointer] > 0:
                    print(f"buying at {buyingPointer} and selling at {sellingPointer}")
                    result += prices[sellingPointer] - prices[buyingPointer]

        return result

                

                # 1,2,4,6,2

            

