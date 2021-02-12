# ** **DESCRIPTION:** **
*The generate_animals.py script takes in various parameters for the head, body,arms, tail, and legs of an animal. 20 animals are created in a Python dictionaryand written into an animals.json file.*

The read_animals.py script reads out all the animals from the generated animals.json file. It also has a breed function that takes two random animals from the Python dictionary and ‘breeds’ them by mixing their elements to create a new a
nimal, which is printed to screen alongwith its ‘parents’

## **DOWNLOADING:**
```
git clone https://github.com/rheebeee/rbhat-coe332.git
```

## **RUNNING:**

### **Docker:**
In order to build an image, run the command:

```
docker build -t username/json-animal:0.1 .
```

In order to run the scripts inside a container, run the commands:

```
docker run --rm -it username/json-animal:0.1 /bin/bash
generate_animals.py test.json
read_animals.py test.json
```

In order to run the scripts non-interactively, run the commands:

```
docker run --rm -v $PWD:/data username/json-animal:0.1 generate_animals.py /data/animals.json
docker run --rm -v $PWD:/data username/json-animal:0.1 read_animals.py /data/animals.json
```
### **Unit Tests:**
In order to run the unit tests, run the command:
```
python3 test_read_animals.py
```

