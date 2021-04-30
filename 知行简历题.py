#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>

# mijia (at) zxunity.com
# 一个朋友在炒股，准备一共买入 50000 元，挑了三只股票，比如美团、腾讯、茅台（不作为投资建议，投资有风险）。同时这位朋友还想进行一下分散配置，比如茅台 20% 仓位（仓位就可以理解为对应总资金的配置比例）、美团 40%、腾讯 40%。但是股票交易有一个限制，就是必须按「手」交易，100 股为一手。那么设计一个算法，让这位朋友的 5w 元尽可能投入市场，同时尽可能满足仓位配置比例。 先声明上述代码版权归你所有，并且我们未来做的是基金业务，所以不会直接使用上述算法。请在邮件中附录代码内容。

class Solution:
    def stock_advise(self,money,stock_picked):
        stock_price_dic={'美团':3.5,'腾讯':66,'茅台':99}
        stock_trade_unit_dic={}
        stock_bought_dic={}
        input_money=money
        pocket_money=money
        for k,v in stock_price_dic.items():
            stock_trade_unit_dic[k]=v*100
            stock_bought_dic[k]=0


        stock_picked=sorted(stock_picked.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)

        ep=9999
        while ep>0:
            for stock_name in stock_picked.keys():
                if pocket_money-stock_trade_unit_dic[stock_name]>0:
                    pocket_money-=stock_trade_unit_dic[stock_name]

            ep+=1

if __name__ == "__main__":
    solution = Solution()
    s = "babad"
    print(s)
    print(solution.longestPalindrome(s)=="bab")
    s = "cbbd"
    print(s)
    print(solution.longestPalindrome(s) == "bb")
    s = "a"
    print(s)
    print(solution.longestPalindrome(s) == "a")
    s = "ac"
    print(s)
    print(solution.longestPalindrome(s) == "a")