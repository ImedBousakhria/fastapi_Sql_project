def individual_serial(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "name": todo["_name"],
        "description": todo["_description"],
        "complete": todo["_complete"]
    }
    
def list_serializer(todos) -> list:
    return [indi]
