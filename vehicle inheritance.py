class vehicle():
    name=''
    colour=''
    two_wheeler=True
    four_wheeler=True

class car(vehicle):
    two_wheeler=False
car1=car()
car1.name="Ferrari"
car1.colour="Red"

class van(vehicle):
    two_wheeler=False
van1=van()
van1.name="Volkswagen"
van1.colour="white"

class scooty(vehicle):
    four_wheeler=False

scooty1=scooty()
scooty1.name="activa"
scooty1.colour="red"


def output(vehicle):
    print(vehicle.name)
    print(vehicle.colour)

    if(vehicle.four_wheeler==True):
        print(f"{vehicle.name} is a four wheeler")
    else:
        print(f"{vehicle.name} is a two wheeler")
        
    
output(car1)
output(van1)
output(scooty1)

