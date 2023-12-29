from dataclasses import dataclass, asdict

from sqlalchemy import DateTime


@dataclass
class UserModel:
    email: str = None
    userId: str = None
    isAuth: bool = False
    isLogIn: bool = False
    password: str = None
    datatime: DateTime = None
    lastName: str = None
    firstName: str = None

    def toDict(self):
        return asdict(self)

    def __repr__(self) -> str:
        return f'''
            UserModel(
                userId = {self.userId}
                email = {self.email}
                password = {self.password}
                datatime = {self.datatime}
                firstName = {self.firstName}
                lastName = {self.lastName}
                isLogIn = {self.isLogIn}
                isAuth = {self.isAuth}
            )
        '''
