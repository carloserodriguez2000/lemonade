import datetime
import WeatherReport
import Owner


class GameDay:

    def __init__(self):
        self.todayWeatherReport = WeatherReport.WeatherReport()
        self.dayStart = datetime.time(8, 0, 0)   # 8 am
        self.dayEnd   = datetime.time(17, 0, 0)  # 5 pm

    def getMoreInventory(self, theOwner):
        # Print make wise choices based on the weather at the time of day.
        # Prompt "Lets buy some supplies"
        # if skip and not enough supplies to buy Put WARNING message. Note: donations to start business.

        print('You have the following')
        theOwner.printInventory()
        more = input('Would you like to get more? y/n: ')
        if more == 'y':
            moreCups  = input('How many more cups would you like?: ')
            moreIce   = input('How much ice would you like?: ')           # Add logic to handle 100, 200,500 cub options
            moreSugar = input('How much more sugar would you like?: ')
        print('Inventory has been updated.')
        print('You have the following')
        theOwner.printInventory()

    def playDay(self):
        print('Welcome Lemonade Stand Entrepreneur')
        # Print some instructions
        owner = Owner.Owner()                       # Create and owner
        owner.loadOwner()                           # initialize owner information
        self.todayWeatherReport.getReport()
        print('Todays weather report is %s, %s, %s Degrees' % (self.todayWeatherReport.weather,
                                                               self.todayWeatherReport.precipitation,
                                                               self.todayWeatherReport.temperature))
        self.getMoreInventory(owner)                     # Ask Owner to update inventory




         #################

        # BUY  items. possibly handle all inside the INVENTORY CLASS.
            # inventory.Buy(Owner)  buy lemons, ice, cups, sugar, water. Accounts for cash VS total cost to buy
                    # buying will create instances of the supplies and quantities.

        #################   GAME LOOP ################

        # if Customer


