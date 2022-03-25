## Introduction

This is a project for garbage dump detection with BCA-Net, which can be used to perform global garbage dump 
detection with our upcoming multi-category garbage dump 
dataset.

![demo image](resources/coco_test_12510.jpg)

## Prerequisites

- OS: Ubuntu 16.04
- GPU: Nvidia GTX/RTX series GPU with proper [NVIDIA Driver](https://www.nvidia.com/Download/index.aspx?lang=en-us) installed
- Software: [Docker](https://www.docker.com/) installed

## Installation
  
1. Create a new project folder.
    ```shell
    mkdir /home/$[YOUR_USERNAME]/garbage_dump
    cd /home/$[YOUR_USERNAME]/garbage_dump
    ```
2. Download the code.
    ```shell
    git ...
    ```
3. Download dataset in our paper's link. 

4. Unzip the dataset to `./garbage_dump_detection/data/`.
    ```none 
    garbage_dump_detection
    ├── mmdet
    ├── tools
    ├── configs
    ├── data
    │   ├── garbage_dump_2022
    │   │   ├── VOC2012
    │   │   │   ├──train
    │   │   │   │   ├──Annotations
    │   │   │   │   ├──JPEGImages
    │   │   │   │   ├──train.txt
    │   │   │   ├──test
    │   │   │   │   ├──Annotations
    │   │   │   │   ├──JPEGImages
    │   │   │   │   ├──test.txt
    ```

5. Get the docker image from Docker-hub.
    ```shell
    sudo docker pull y389164605/garbage_dump_detection:latest
    ```
   
6. Create a docker container with the above image.
    ```shell
    sudo nvidia-docker run --privileged=true --name=$[YOUR_CONTAINER_NAME] --shm-size=8g -d -p $[PORT_FOR_CONTAINER_PORT_22]:22 -v /home/$[YOUR_USERNAME]/garbage_dump/garbage_dump_detection:/garbage_dump_detection y389164605/garbage_dump_detection:latest /usr/sbin/sshd -D
    ```
   Note: 
   
    a. If the terminal remains inactive, create a new terminal and continue the operation.
    
    b. `/home/$[YOUR_USERNAME]/garbage_dump/garbage_dump_detection` in your computer and `/garbage_dump_detection` in your docker container are a pair of mapped folders and they will remain consistent.
7. Enter the above docker container.
    ```shell
    sudo docker exec -it $[YOUR_CONTAINER_NAME] /bin/bash
    ```
   
## Demo



## Batch inference



## Trainng thef BCA-Net


