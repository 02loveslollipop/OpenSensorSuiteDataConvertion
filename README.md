# OpenSensorSuite
> A simple sensor monitoring utility for ESP32 microcontrollers, powered by Python and Redis.

## Introduction
OpenSensorSuite is a simple sensor monitoring utility for ESP32 microcontrollers using a RedisDB for the data persistence. It is designed to be a simple, lightweight, and easy to use solution for monitoring sensor data from ESP32 microcontrollers. This repository contains the source code for GUI to view and manage the data. The source code for the ESP32 microcontroller can be found [here](https://github.com/02loveslollipop/OpenSensorSuiteESP32). And the source code for the GUI to view the data can be found can be found [here](https://github.com/02loveslollipop/OpenSensorSuiteGUI)

## Linux & Windows setup

1. Clone the repository
```sh
git clone https://github.com/02loveslollipop/OpenSensorSuiteDataConvertion
```

2. Install the dependencies
```sh
pip install -r requirements.txt
```

3. Copy the `example_config.yaml` file to `config.yaml`
```sh
cp example_config.yaml config.yaml
```

4. Edit the `config.yaml` file to match your configuration
```yaml
redis:
  host: redis.yourhost.example #change to your redis host
  port: 6379 #change to your redis port
  password: MIREALLYSECUREPASSWORD #change to your redis password
  key_origin: "SENSOR_32A_BUFFER" #change to the key of the data you want to parse
  key_destination: "SENSOR_32A" #change to the key where you want to store the parsed data

service:
  update_interval: 1 #change to the interval you want to update the data in seconds
```

5. Run the microservice
```sh
python main.py
```

## Docker setup

1. Clone the repository
```sh
git clone https://github.com/02loveslollipop/OpenSensorSuiteDataConvertion
```

2. Copy the `example_config.yaml` file to `config.yaml`
```sh
cp example_config.yaml config.yaml
```

3. Edit the `config.yaml` file to match your configuration
```yaml
redis:
  host: redis.yourhost.example #change to your redis host
  port: 6379 #change to your redis port
  password: MIREALLYSECUREPASSWORD #change to your redis password
  key_origin: "SENSOR_32A_BUFFER" #change to the key of the data you want to parse
  key_destination: "SENSOR_32A" #change to the key where you want to store the parsed data

service:
  update_interval: 1 #change to the interval you want to update the data in seconds
```

4. Build the docker image
```sh
docker build -t opensensorsuite-dataconvertion .
```

5. Run the docker image
```sh
docker run -d --name opensensorsuite-dataconvertion opensensorsuite-dataconvertion
```
