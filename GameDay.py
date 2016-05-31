import datetime
import WeatherReport
import Owner
import Customer


class GameDay:
    def __init__(self):
        self.todayWeatherReport = WeatherReport.WeatherReport()
        self.dayStart = datetime.datetime.now()
        self.dayEnd = self.dayStart.replace(hour=17)  # datetime.time(17, 0, 0)  # 5 pm
        self.warpFactor = 60  # increment in 60 seconds blocks

    def getMoreInventory(self, theOwner):
        # Print make wise choices based on the weather at the time of day.
        # Prompt "Lets buy some supplies"
        # if skip and not enough supplies to buy Put WARNING message. Note: donations to start business.

        print('You have the following')
        theOwner.printInventory()
        more = input('Would you like to get more? y/n: ')
        if more == 'y':
            moreCups = int(input('How many more cups would you like?: '))
            moreIce = int(input('How much ice would you like?: '))  # Add logic to handle 100, 200,500 cub options
            moreSugar = int(input('How much more sugar would you like?: '))
            moreLemons = int(input('How many more lemons would you like?: '))
            theOwner.inventory.addCups(moreCups, theOwner.inventory.cupPrice)
            theOwner.inventory.addIcubes(moreIce, theOwner.inventory.icePrice)
            theOwner.inventory.addSugar(moreSugar, theOwner.inventory.sugarPrice)
            theOwner.inventory.addLemons(moreLemons, theOwner.inventory.lemonPrice)

        print('Inventory has been updated.')
        print('You have the following')
        theOwner.printInventory()

    def playDay(self):
        print('Welcome Lemonade Stand Entrepreneur')
        # Print some instructions
        owner = Owner.Owner()  # Create and owner
        owner.loadOwner()  # initialize owner information
        self.todayWeatherReport.getReport()
        print('Today\'s weather report is %s, %s, %s Degrees' % (self.todayWeatherReport.weather,
                                                                 self.todayWeatherReport.precipitation,
                                                                 self.todayWeatherReport.temperature))
        self.getMoreInventory(owner)  # Ask Owner to update inventory
        owner.inventory.fillPitcher()
        seconds = ((self.dayEnd.hour - self.dayStart.hour) * 60 + self.dayStart.minute + self.dayEnd.minute) * 60
        while self.dayStart < self.dayEnd and seconds > 0:
            potentialCustomer = Customer.Customer()  # one customer every loop. Improve with random daily rate code
            if owner.inventory.enoughInventory() == True and owner.inventory.pitcher.level>0:
                if potentialCustomer.isInterested(self.todayWeatherReport):
                    print('Customer is buying')
                    cupObject = owner.inventory.takeCup(1)
                    owner.fillCup(cupObject, owner.inventory.pitcher)
                    owner.giveFullCup(cupObject)  # deletes cup object from memory space

                else:
                    print('Customer is not interested')
                nowSeconds = datetime.datetime.now().second
                print('Time Left = ', seconds/60/60, ' Pitcher level = ',owner.inventory.pitcher.level)
                while nowSeconds == datetime.datetime.now().second:
                    tickTock = 1

                seconds -= self.warpFactor  # eat seconds faster by warp factor
            else:
                print('Sorry: you ran out of supplies')
                # Add capability to track actual sales, lost sales due to interest, lost sales due to supplies
                owner.printInventory()
                break

            print('         SORRY. its pass %s. Time to go home. ' % (self.dayEnd))
