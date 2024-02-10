def individual_serial(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "name": str(todo["_name"],
        "description": todo["_description"],
        "complete": todo["_complete"]
    }
