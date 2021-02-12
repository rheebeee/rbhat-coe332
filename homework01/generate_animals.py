import json
import random
import petname

heads= ['snake', 'bull', 'lion', 'raven', 'bunny']
animals= {}
animals['animal']= []

arm= random.randrange(2,10,2)
leg= random.randrange(3,12,3)

for x in range(0,20):
    animals['animal'].append({'head': heads[random.randrange(0,4)],
                              'body': petname.name()+ '-'+ petname.name(),
                              'arms': arm,
                              'legs': leg,
                              'tails':arm+leg})

    arm= random.randrange(2,10,2);
    leg= random.randrange(3,12,3);

with open('animals.json','w') as out:
    json.dump(animals, out, indent=2)




