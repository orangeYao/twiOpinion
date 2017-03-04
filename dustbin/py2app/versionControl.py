def greeting():
    return "Welcome to twiOpinion 0.1.3!"

def startingInfo():
    with open ("../startingInfo.txt", "r") as myfile:
        data=myfile.read()
    return data
