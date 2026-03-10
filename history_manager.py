import json

FILE="health_history.json"


def save_history(data):

    try:

        with open(FILE,"r") as f:
            history=json.load(f)

    except:
        history=[]

    history.append(data)

    with open(FILE,"w") as f:

        json.dump(history,f)


def load_history():

    try:

        with open(FILE,"r") as f:

            return json.load(f)

    except:

        return []
