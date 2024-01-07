from pydantic import BaseModel

class AccountBase(BaseModel):
    userID: int
    balance: float
    balance_USD: float
    

class AccountCreate(AccountBase):
    pass

class Account(BaseModel):
    accountID: int
    class Config:
        orm_mode = True
