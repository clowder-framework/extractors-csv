Clowder CSV Extractor
=====================

[Clowder](https://clowder.ncsa.illinois.edu/) extractor to extract column names from CSV files and add them to the 
metadata of the file. Currently only looks at the first row and does not support files with multiple header rows.

Docker
------

To build the Docker image: 

```docker build -t clowder/extractors-csvheaders .```

Requires clowder/extractors-simple-extractor:onbuild. This can be build by checking out
 
```git clone https://opensource.ncsa.illinois.edu/bitbucket/projects/CATS/repos/pyclowder2``` 

and running 

```./docker.sh```.

To run the extractor with an existing Clowder instance:

```docker run -t -i --rm --name=extractors-csvheaders -e 'RABBITMQ_URI=amqp://guest:guest@yourDNSnameorIP' -e 'REGISTRATION_ENDPOINTS=http://yourDNSnameorIP:9000/api/extractors?key=r1ek3rs' clowder/extractors-csv```

To run the extractor with a Clowder instance running with docker-compose.yml included with the Clowder source repository:

```docker run -t -i --rm --network clowder_clowder clowder/extractors-csvheaders```



