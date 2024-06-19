# coding challenge for IAS aka WMATA Trains Docker Container

This container fetches and displays Yellow Line trains headed to Huntington Station using the WMATA API.

## Prerequisites

- Docker installed on your machine.
- A WMATA API key. <the key can be obtained form https://developer.wmata.com/demokey>

## Build the Docker Image

1. uznip the file.
2. Navigate to the project directory.
3. export the obtained key as environmental variable
for linux cli:
```sh
export WMATA_API_KEY=<your_wmata_api_key>
````
4. Run harness bashscript to build and run the cod:

```sh
chmod +x run_container.sh
./run_container.sh
````
