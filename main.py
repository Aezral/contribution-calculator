from user import User
from project import Project

luis = User("Luis")
ivan = User("Ivan")
ricardo = User("Ricardo")
andrea = User("Andrea")

proyecto = Project()
proyecto.addContributor(luis)
proyecto.addContributor(ivan)
proyecto.addContributor(ricardo)
proyecto.addContributor(andrea)

proyecto.contribute(andrea, 400, "Primera compra")
proyecto.contribute(luis, 100, "Segunda compra")
proyecto.contribute(luis, 100, "Tercera compra")

proyecto.printContributionList()
proyecto.printContributorList()
