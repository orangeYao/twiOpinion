def greeting():
    return "Welcome to twiOpinion 1.1.3!"

def startingInfo():
    with open ("../startingInfo.txt", "r") as myfile:
        data=myfile.read()
    return data
