from dataclasses import dataclass, asdict

from sqlalchemy import DateTime


@dataclass
class UserModel:
    userId: str = None 
    email: str = None
    password: str = None
    datatime: DateTime = None

    def toDict(self):
        return asdict(self)

    def __repr__(self) -> str:
        return f'''
            UserModel(
                userId = {self.userId}
                email = {self.email}
                password = {self.password}
                datatime = {self.datatime}
            )
        '''
