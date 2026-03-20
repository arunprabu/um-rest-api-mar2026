class UserService:
    
    def get_users(self):
        print("I will fetch all users from the database")

        return [
            {"id": 1, "name": "Arun"},
            {"id": 2, "name": "Bob"},
        ]

    def create_user(self, user: dict):
        print(f"I will save the user data: {user} to the database")
        return {
            "status": "saved successfully",
        }

    def get_user_by_id(self, user_id: int):
        print(f"I will fetch the user data for the user id: {user_id} from the database")
        return {
            "id": user_id,
            "name": "Alice"
        }

    def update_user_by_id(self, user_id: int, user: dict):
        print(f"I will update the user data for the user id: {user_id} with the data: {user} in the database")
        return {
            "status": "updated successfully",
        }

    def delete_user_by_id(self, user_id: int):
        print(f"I will delete the user data for the user id: {user_id} from the database")
        return {
            "status": "deleted successfully",
        }

    def get_user_service():
        return UserService()

