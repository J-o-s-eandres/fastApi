def userEntity(item) -> dict:
    return{
        "id": str(item["_id"]),
        "name": item["name"],
        "email": item["email"],
        "password": item["password"]
    }


def usersEntity(entity) -> list:
    # por cada elemento que estamos recorriendo le damos el elemento a userentity para wue genere el esquema
    return [userEntity(item) for item in entity]
