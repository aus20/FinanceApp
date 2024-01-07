from pydantic import BaseModel

class NewsBase(BaseModel):
    title: str
    content: str
    date: str
    stockID: int

class NewsCreate(NewsBase):
    pass

class News(BaseModel):
    newsID: int
    class Config:
        orm_mode = True
