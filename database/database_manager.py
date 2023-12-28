from flask import json
from database.user_database import Session, UserDatabase
from models.user_model import UserModel


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
            return {"message": "All users gotten sucssessfully", "status": True, "result": results}
        except Exception as e:
            return {"message": f"{e}", "status": False, "result": None}

    @staticmethod
    def getUserByEmail(email: str):
        try:
            result = Session.query(UserDatabase).filter_by(email=email).first()
            if result is None:
                return {"message": "User was not found", "status": False, "result": result}
            return {"message": "User gotten sucssessfully", "status": True, "result": result}
        except Exception as e:
            return {"message": f"{e}", "status": False, "result": None}

    @staticmethod
    def getUserByUserId(userId: str):
        try:
            result = Session.query(UserDatabase).filter_by(
                userId=userId).first()
            if result is None:
                return {"message": "User was not found", "status": False, "result": result}
            return {"message": "User gotten sucssessfully", "status": True, "result": result}
        except Exception as e:
            return {"message": f"{e}", "status": False, "result": None}
        
    @staticmethod
    def createUser(userModel:UserModel):
        try:
            user = DatabaseManager.getUserByEmail(email=userModel.email)
            if not user["status"]:
                Session.add(UserDatabase(userModel))
                Session.commit()
                return {"message": "User was added sucssessfully", "status": True, "result": userModel.toDict()}
            return {"message": "User with email already exist", "status": False, "result": None}
        except Exception as e:
            return {"message": f"{e}", "status": False, "result": None}
