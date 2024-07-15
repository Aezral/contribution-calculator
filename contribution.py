from user import User
from uuid import uuid4
class Contribution:
    id:str
    user: User
    amount: float
    description: str

    def __init__(self,user:User,amount:float, description:str):
        self.id = str(uuid4())
        self.amount = amount
        self.user = user
        self.description = description