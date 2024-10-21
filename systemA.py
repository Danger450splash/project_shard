
# This is for testing only

from abc import ABC, abstractmethod

class abstractSpawn(ABC):

    @abstractmethod
    def ground(self) -> None:
        pass

    @abstractmethod
    def permit(self) -> None:
        pass

    @abstractmethod
    def loopPattern(self) -> None:
        pass

class shop(abstractSpawn):

    def __init__(self) -> None:
        self.__manager()
        self.permit()
        self.ground()

        self.__value: int = self.__cashier(20)
        print(self.__value)
        self.loopPattern()
        self.replayClass()

    def ground(self) -> None:
        print(f'Ground Method')

    def permit(self) -> None:
        self.__num: int = 1
        print(f'Hello World, this is a brand new testing feature, {self.__num}')

    def loopPattern(self) -> None:
        self.user = int(input(f'Enter the number of stars you want: '))
        self.stars: int = self.user
        for self.rows in range(1, self.stars+1):
            self.num: int = 1
            for self.columns in range(self.stars+1, 0, -1):
                if self.columns > self.rows:
                    print(" ", end=' ')
                else:
                    print("*", end=' ')
                    self.num += 1
            print()

    def __cashier(self, cell1: int) -> int:
        self.__cell1: int = cell1
        return self.__cell1
    
    def __manager(self) -> None:
        print(f'We have successfully accomplish this task.')

    def replayClass(self) -> None:

        user2 = input(f'Do you want to try again? ')
        capitalizer = user2.capitalize()

        if (capitalizer == "Yes") or (capitalizer == "YES"):
            print(f'We are calling back the constructor.')
            print(self.__init__())
        elif (capitalizer == "No") or (capitalizer == "NO"):
            print(f'Thank you and come again!')
        else:
            print(f'You did not choose between Yes or No')
            