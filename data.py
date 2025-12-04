import json
def load(filepath = "person_data.json"):
    try:
        with open(filepath,"r") as f:
           return json.load(f)
    except json.JSONDecodeError:
        return []
    except FileNotFoundError:
        print("file does not exist")
        return []

def save(data,filepath="person_data.json"):
    with open(filepath,"w") as f:
        json.dump(data,f,indent=4)


