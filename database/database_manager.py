from flask import json
from database.user_database import Session, UserDatabase
from models.user_model import UserModel
from werkzeug.security import check_password_hash


class DatabaseManager:
    @staticmethod
    def getAllUsers():
        results: list = []
        try:
            for value in Session.query(UserDatabase).all():
                result = value
                for k, v in result.__dict__.items():
                    try:
                        result.__dict__[k] = json.loads(v)
                    except Exception as e:
                        print(f"ERR Key {k} Value {v}")
                        print(f"ERROR {e}")

                # Remove the item with key "b"
                if "_sa_instance_state" in result.__dict__:
                    del result.__dict__["_sa_instance_state"]
                    results.append(result.__dict__)
                else:
                    results.append(result.__dict__)
            return {"message": "All users gotten successfully", "status": True, "result": results}
        except Exception as e:
            return {"message": f"{e}", "status": False, "result": None}

    @staticmethod
    def getUserByEmail(email: str):
        try:
            value = Session.query(UserDatabase).filter_by(email=email).first().__dict__
            if value is None:
                return {"message": "User was not found", "status": False, "result": None}
            result = value
            for k, v in value.items():
                try:
                    result[k] = json.loads(v)
                except Exception as e:
                    print(f"ERR Key {k} Value {v}")
                    print(f"ERROR {e}")
            # Remove the item with key "b"
            if "_sa_instance_state" in result:
                del result["_sa_instance_state"]
            return {"message": "User gotten successfully", "status": True, "result": result}
        except Exception as e:
            return {"message": f"{e}", "status": False, "result": None}

    @staticmethod
    def getUserByUserId(userId: str):
        try:
            value = Session.query(UserDatabase).filter_by(userId=userId).first().__dict__
            if value is None:
                return {"message": "User was not found", "status": False, "result": None}
            result = value
            for k, v in value.items():
                try:
                    result[k] = json.loads(v)
                except Exception as e:
                    print(f"ERR Key {k} Value {v}")
                    print(f"ERROR {e}")
            # Remove the item with key "b"
            if "_sa_instance_state" in result:
                del result["_sa_instance_state"]
            return {"message": "User gotten successfully", "status": True, "result": result}

        except Exception as e:
            return {"message": f"{e}", "status": False, "result": None}

    @staticmethod
    def createUser(userModel: UserModel):
        try:
            user = DatabaseManager.getUserByEmail(email=userModel.email)
            if not user["status"]:
                Session.add(UserDatabase(userModel))
                Session.commit()
                return {"message": "User was added successfully", "status": True,
                        "result": userModel.toDict()}
            return {"message": "User with email already exist", "status": False, "result": None}
        except Exception as e:
            return {"message": f"{e}", "status": False, "result": None}

    @staticmethod
    def updateUserById(userId: str, values: dict):
        try:
            user = DatabaseManager.getUserByUserId(userId=userId)
            if not user['status']:
                return {"message": "User does not exist", "status": False, "result": None}
            Session.query(UserDatabase).filter_by(userId=userId).update(values=values)
            Session.commit()
            return {"message": "User was updated successfully", "status": True,
                    "result": values}
        except Exception as e:
            return {"message": f"{e}", "status": False, "result": None}

    @staticmethod
    def updateUserByEmail(email: str, values: dict):
        try:
            user = DatabaseManager.getUserByEmail(email=email)
            if not user['status']:
                return {"message": "User does not exist", "status": False, "result": None}
            Session.query(UserDatabase).filter_by(email=email).update(values=values)
            Session.commit()
            return {"message": "User was updated successfully", "status": True,
                    "result": values}
        except Exception as e:
            return {"message": f"{e}", "status": False, "result": None}

    @staticmethod
    def deleteUserByUserId(userId: str):
        try:
            Session.query(UserDatabase).filter_by(userId=userId).delete()
            Session.commit()
            return {"message": "User was deleted successfully", "status": True,
                    "result": {}}
        except Exception as e:
            return {"message": f"{e}", "status": False, "result": None}

    @staticmethod
    def deleteUserByEmail(email: str):
        try:
            Session.query(UserDatabase).filter_by(email=email).delete()
            Session.commit()
            return {"message": "User was deleted successfully", "status": True,
                    "result": {}}
        except Exception as e:
            return {"message": f"{e}", "status": False, "result": None}

    @staticmethod
    def signUpUser(userModel: UserModel):
        try:
            user = DatabaseManager.createUser(userModel)
            return user
        except Exception as e:
            return {"message": f"{e}", "status": False, "result": None}

    @staticmethod
    def logInUserById(userId: str, values: dict):
        try:
            user = DatabaseManager.getUserByUserId(userId)
            if not user['status'] or not check_password_hash(user['result']["password"],
                                                             values['password']):
                return {"message": "Check your login details", "status": False, "result": None}
            user = DatabaseManager.updateUserById(userId, {"isLogIn": True})
            return user
        except Exception as e:
            return {"message": f"{e}", "status": False, "result": None}

    @staticmethod
    def logInUserByEmail(email: str, values: dict):
        try:
            user = DatabaseManager.getUserByEmail(email)
            if not user['status'] or not check_password_hash(user['result']["password"],
                                                             values['password']):
                return {"message": "Check your login details", "status": False, "result": None}
            user = DatabaseManager.updateUserByEmail(email, {"isLogIn": True})
            return user
        except Exception as e:
            return {"message": f"{e}", "status": False, "result": None}

    @staticmethod
    def logOutUserByEmail(email: str):
        try:
            DatabaseManager.updateUserByEmail(email, {"isLogIn": False})
            user = DatabaseManager.getUserByEmail(email)
            return user
        except Exception as e:
            return {"message": f"{e}", "status": False, "result": None}

    @staticmethod
    def logOutUserByUserId(userId: str):
        try:
            DatabaseManager.updateUserById(userId, {"isLogIn": False})
            user = DatabaseManager.getUserByUserId(userId)
            return user
        except Exception as e:
            return {"message": f"{e}", "status": False, "result": None}
