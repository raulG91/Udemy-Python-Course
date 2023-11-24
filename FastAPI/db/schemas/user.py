def user_schema(user):
    return {"id": str(user["_id"]),
            "username": user["username"],
            "email": user["email"]
            }
def users_schema(users):
    return[ user_schema(user) for user in users]