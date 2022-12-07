from ..utils.database.collection import Collection

expenses = Collection("expenses")
user = ""

def get_all():
    data = expenses.get()
    print(data)     