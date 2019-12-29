
class OutersNotAllowed(ValueError):
    pass
def access(name:str, Id:list):
    if len(Id) != 5:
        raise OutersNotAllowed(f"The id not matched please enter the proper id ")
    return f"The person with name {name} and id {Id}is allowed to access the door "
try:
    print(access("siddhu", [5,7,6,5,3]))
except OutersNotAllowed as e:
    print(e)