from audit import audit


def automatic_decision(scenario):
    # *** YOUR CODE GOES HERE ***
    pedestrianScore = 0
    passengerScore = 0
    
    pedestrians = scenario.getPedestrians()
    passengers = scenario.getPassengers()

    for a in pedestrians:
        if a.getCharType() == "human":
            pedestrianScore =+ 5
        elif a.getCharType() == "cat":
            pedestrianScore += 4
        elif a.getCharType() == "dog":
            pedestrianScore += 3
        if a.getAge() ==  "baby":
            pedestrianScore += 5
        if a.getAge() ==   "child":
            pedestrianScore += 4
        if a.getAge() ==   "adult":
            pedestrianScore += 3
        if a.isPregnant():
            pedestrianScore += 5
            
    for a in passengers:
        if a.getCharType() == "human":
            passengerScore =+ 5
        elif a.getCharType() == "cat":
            passengerScore += 4
        elif a.getCharType() == "dog":
            passengerScore += 3
        if a.getAge() ==  "baby":
            passengerScore += 5
        if a.getAge() ==   "child":
            passengerScore += 4
        if a.getAge() ==   "adult":
            passengerScore += 3
        if a.isPregnant():
            passengerScore += 5
        
    if passengerScore >= pedestrianScore:
        return "passengers"
    return "pedestrians"
    # default to saving the passengers
    

if __name__ == '__main__':
    audit(automatic_decision, 60, seed=8675309)
