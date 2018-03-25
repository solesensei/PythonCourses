class Shop():
    def __init__(self, name):
        self.name = name
        self.goods = {}
        self.mgoods = {}

    # returns minimal cost of goods
    def getMinCost(self):
        goods = list(self.goods.items())
        min_cost = goods[0][1]
        for good in goods:
            if good[1] < min_cost:
                min_cost = good[1]
        return min_cost

    # returns goods with the cost
    def setGoodsByCost(self, cost):
        goods = list(self.goods.items())
        cgoods = []
        for good in goods:
            if good[1] == cost:
                cgoods.append(good)
        if cgoods:
            for good in cgoods:
                self.mgoods[good[0]] = good[1]

    def find_in_other(self, shops, goods, start):
        mgoods = []
        for good in goods:
            g = Good(good)
            g.shops.append(self.name)
            for i in range(start, len(shops)):
                for mgood in shops[i].mgoods:
                    a = good.split()
                    b = mgood.split()
                    if sorted(a) == sorted(b):
                        if a != b:
                            g.name.append(mgood)
                        g.shops.append(shops[i].name)
                        g.count += 1
                shops[i].mgoods.pop(good, 0)
            if g.count > 1:
                g.name.sort()
                mgoods.append(g)
        return mgoods


class Good():
    def __init__(self, name):
        self.name = []
        self.name.append(name)
        self.shops = []
        self.count = 1


def find_minimal_cost(shops):
    min_cost = shops[0].getMinCost()
    for shop in shops:
        cost = shop.getMinCost()
        if cost < min_cost:
            min_cost = cost
    return min_cost


def classSort(cl):
    return cl[0].name


def start_finding(shops):
    outFile = open("output.txt", 'w', encoding='utf8')
    cost = find_minimal_cost(shops)
    for shop in shops:
        shop.setGoodsByCost(cost)
    goods_shops = []
    find_from = 0
    for shop in shops:
        find_from += 1
        if not len(shop.mgoods):
            continue
        good_shops = shop.find_in_other(shops, shop.mgoods, find_from)
        if len(good_shops):
            goods_shops.append(good_shops)
    print(cost, file=outFile)
    goods_shops.sort(key=classSort)
    for class_lists in goods_shops:
        for good in class_lists:
            print(good.name[0], end='', file=outFile)
            print(':', end=' ', file=outFile)
            print(', '.join(map(str, sorted(good.shops))), file=outFile)
    outFile.close()


def main():
    inFile = open("input.txt", 'r', encoding='utf8')
    lines = inFile.readlines()
    shops = []
    for line in lines:
        tmp = line.split(': ')
        shop = Shop(tmp[0])
        goods = tmp[1].split(', ')
        for good in goods:
            tmp = good.split(' - ')
            shop.goods[tmp[0]] = tmp[1].replace('\n', '')
        shops.append(shop)
    start_finding(shops)
    inFile.close()

if __name__ == "__main__":
    main()
