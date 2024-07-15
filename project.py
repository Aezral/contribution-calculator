from contribution import Contribution
from user import User
from uuid import uuid4


class Project:
    __contributors: dict[str, User]
    __contributions: list[Contribution]

    def __init__(self):
        self.__contributions = []
        self.__contributors = {}

    def addContributor(self, user: User):
        self.__contributors[user.getId()] = user

    def removeContributor(self, user: User):
        if user.getId() not in self.__contributors:
            raise Exception("El usuario no es un contribuyente de este proyecto")

        del self.__contributors[user.getId()]

        for contribution in self.__contributions:
            if contribution.user.getId() == user.getId():
                self.__contributions.remove(contribution)

    def contribute(self, user: User, amount: float, description: str) -> str:

        if user.getId() not in self.__contributors:
            raise Exception("El usuario no es un contribuyente de este proyecto")

        contribution = Contribution(user, amount, description)

        self.__contributions.append(contribution)
        return contribution.id

    def removeContribution(self, contributionId: str):

        for contribution in self.__contributions:
            if contribution.id == contributionId:
                self.__contributions.remove(contribution)
                return

        raise Exception("La contribución no existe")

    def getUserContributions(self, user: User):

        if user.getId() not in self.__contributors:
            raise Exception("El usuario no es un contribuyente de este proyecto")

        contributions: list[Contribution] = []
        for contribution in self.__contributions:
            if contribution.user.getId() == user.getId():
                contributions.append(contribution)
        return contributions

    def getUserTotalContribution(self, user: User):
        if user.getId() not in self.__contributors:
            raise Exception("El usuario no es un contribuyente de este proyecto")

        total = 0
        for contribution in self.getUserContributions(user):
            total += contribution.amount
        return total

    def __getTotal(self) -> float:
        total = 0
        for contribution in self.__contributions:
            total += contribution.amount
        return total

    def getContributorList(self):
        projectTotalContribution = self.__getTotal()

        # list of tuples with user, total contribution, and what they should pay
        contributors: list[tuple[User, float, float]] = []

        amountPerUser = projectTotalContribution / len(self.__contributors)

        for user in self.__contributors.values():
            totalUserContribution = self.getUserTotalContribution(user)
            shouldPay = amountPerUser - totalUserContribution

            contributors.append((user, totalUserContribution, shouldPay))

        return contributors

    def printContributorList(self):
        contributors = self.getContributorList()

        print("------- Contribuyentes ----------------------")
        for contributor in contributors:
            message = f"{contributor[0].getName()} dió ${contributor[1]} y "
            if contributor[2] > 0:
                message += f"debe dar ${contributor[2]}"
            else:
                message += f"debe recibir ${abs(contributor[2])}"
            print(message)

        print(f"\nTotal del proyecto: ${self.__getTotal()}")
        print("----------------------------------------------")

    def printContributionList(self):
        print("------- Contribuciones ----------------------")
        for contribution in self.__contributions:
            print(
                f"{contribution.description} - ${contribution.amount} ({contribution.user.getName()})"
            )
        print("---------------------------------------------")
