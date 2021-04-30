#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>

# mijia (at) zxunity.com


def sort_value(old_dict, reverse=False):
    items = sorted(old_dict.items(), key=lambda obj: obj[1], reverse=reverse)
    new_dict = {}
    for item in items:
        new_dict[item[0]] = old_dict[item[0]]
    return new_dict


class Solution:
    def stock_advise(self, money, stock_picked):
        if money is None or float(money) <= 0 or stock_picked is None or len(stock_picked) == 0:
            return None
        stock_price_dic = {'美团': 3.5, '腾讯': 66, '茅台': 99}
        stock_trade_unit_dic = {}

        input_money = money
        pocket_money = money

        stock_bought_proportion = {}
        stock_bought_dic = {}
        min_bought = None
        for k, v in stock_picked.items():
            stock_trade_unit_dic[k] = stock_price_dic[k] * 100
            if min_bought is None or stock_trade_unit_dic[k] < min_bought:
                min_bought = stock_trade_unit_dic[k]
            stock_bought_dic[k] = 0
            stock_bought_proportion[k] = 0

        # 哎一手都买不起
        if money < min_bought:
            return None
        # 永远遵从用户初始的意愿来安排购买顺序
        stock_picked = sort_value(stock_picked, reverse=True)

        ep = 9999
        # 此flag用于花光用户袋袋里头的最后一块钱
        has_bought_flag = False
        len_stock_picked = len(stock_picked)
        i = 0
        force_bought = False
        while ep > 0:
            for stock_name in stock_picked.keys():
                # 他还有钱且当前此股票比例小于他期望的比例则购买一手
                if pocket_money - stock_trade_unit_dic[stock_name] > 0 \
                        and (stock_bought_proportion[stock_name] < stock_picked[stock_name] or force_bought):
                    # 口袋里的钱又少了
                    pocket_money -= stock_trade_unit_dic[stock_name]
                    stock_bought_dic[stock_name] += 1
                    has_bought_flag = True
                    if force_bought:
                        force_bought = False
                    # 重新计算意愿
                    stock_money = input_money - pocket_money
                    for k, v in stock_bought_proportion.items():
                        stock_bought_proportion[k] = stock_bought_dic[k] * 100 * stock_price_dic[k] / stock_money
                if pocket_money < min_bought:
                    return stock_bought_dic, stock_bought_proportion, pocket_money
                i += 1

            # 当确定没有意愿购买时强制购买
            if i % len_stock_picked == 0:
                if has_bought_flag == False:
                    force_bought = True
                else:
                    has_bought_flag = False
            ep += 1


if __name__ == "__main__":
    solution = Solution()
    s = {'美团': 0.2, '腾讯': 0.4, '茅台': 0.4}
    print(s)
    print(solution.stock_advise(50000, s))
    print('-----------------50000------------------')
    s = {'美团': 0.2, '腾讯': 0.4, '茅台': 0.4}
    print(s)
    print(solution.stock_advise(15000, s))
    print('----------------15000-------------------')
    s = {'美团': 0.1, '腾讯': 0.4, '茅台': 0.4}
    print(s)
    print(solution.stock_advise(5000, s))
    print('----------------5000-------------------')
