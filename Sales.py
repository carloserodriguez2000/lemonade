class Sales:

    def __init__(self):
        self.numberOfSales=0
        self.SalesTable=[['DATE', 'PERSONTYPE', 'PRICE']]  # Row [0] is the title row. records appended
                                                        #satesTable.append([datetype, string, float])
                                                        #each row is one cup of lemonade sold

    def storeSale(self, sale):
        self.SalesTable.append(sale)
        self.numberOfSales += 1

    def tallySales(self):
        currentProfit=0
        for sale in self.SalesTable:
            currentProfit += sale[2]                 # Element 2  is the sale price of the cup sold


