class Sales:

    def __init__(self):
        self.numberOfSales=0
        self.SalesTable=[['DATE', 'PERSONTYPE', 'PRICE']]  # Row [0] is the title row. records appended
                                                        #satesTable.append([datetype, string, float])
                                                        #each row is one cup of lemonade sold

    def storeSale(self, sale):
        i=0
        self.SalesTable.append(sale)

    def tallySales(self):
        currentProfit=0
        for sale in self.SalesTable:
            currentProfit+= sale[2]                 # Third(0,1,2) element  is the sale price of the cup sold


