# ** **DESCRIPTION:** **
*The app.py  script takes in various commands and uses app routes in order to return different data from the animals.json file.
>The method /animals/legs/<leg> returns the animals with the specified number of legs in the file
>The command /animals returns all the animals in the file
>The command /animals/head<name> returns the animals with the specificed head*

The web directory given has an app.py file with the code for the commands and the requirements.txt specifices which version of FLASK must be installed. The dockerfile provided has more instructions on how to build the file.

## **DOWNLOADING:**
```
git clone https://github.com/rheebeee/rbhat-coe332.git
```

## **RUNNING:**

### **Docker:**
In order to build an image, run the command:

```
docker build -t flask-animalContainer:latest .
```

In order to run the scripts inside a container, run the commands:

```
docker run --name "give your container a name" -d -p 5003:5000 flask-animalContainer
```

In order to check the scripts (and make sure that it is running on your port), run the command:

```
docker ps -a
```

In order to curl your port run the command:

```
curl localhost:5003
```

