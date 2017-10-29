#immutiability

def add_to(opbject, collection=None):
    if collection is None:
        collection = []
    collection.append(opbject)
    return collection

list = [1,2,3]
add_to(4,list)
print(list)
add_to(1)
print(list)
add_to("string")
