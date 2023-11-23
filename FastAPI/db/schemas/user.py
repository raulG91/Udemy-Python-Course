def user_schema(user):
    return {"id": str(user["_id"]),
            "username": user["username"],
            "email": user["email"]
            }
