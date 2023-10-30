# MicroPython-urdflib-ISWC2023

This repository is dedicated to the ISWC2023 Poster and Demos Track, where we have submitted a paper. In this repository, you will find instructions on how to replicate and access the evaluation results mentioned in our paper.

## Prerequisites

Before you begin, ensure you have the following prerequisites:

- Git installed on your system.
- MicroPython and "urdflib" repositories cloned to your local machine. (I used MicroPython v1.20.0)
- An EPS32 for running it on ESP32 port

## Step 1: Clone MicroPython and "urdflib" Repositories

1. Open your terminal.

2. Clone the MicroPython and urdflib repository to a directory of your choice:

   ```bash
   $ git clone -b v1.21.0 --depth 1 --recurse-submodules --shallow-submodules https://github.com/micropython/micropython.git
   ```

## Step 2: Configure MicroPython

1. Navigate to the MicroPython repository and add the `urdflib-ext` submodule:

    ```bash
    cd micropython
    git submodule add --depth 1 https://github.com/moh3nhadavi/urdflib-ext.git lib/urdflib-ext
    git submodule add --depth 1 https://github.com/moh3nhadavi/micropython-urdflib urdflib
    ```
    
1. build [MicroPython cross-compiler](https://github.com/micropython/micropython/blob/master/mpy-cross)
    ```bash
    $ cd mpy-cross
    $ make
    ```


## Step 3: Build and Run MicroPython with "urdflib"

### UNIX port

To build on UNIX port, do not make all warnings into errors:

   ```bash
    $ cd ../ports/unix
    $ make submodules
    $ sed -i '/CWARN = -Wall -Werror/cCWARN = -Wall #CWARN = -Wall -Werror' Makefile
    $ make USER_C_MODULES=../../urdflib
   ```


After build, you can run it by:
    
   ```bash
    $ ./build-standard/micropython
   ```

To run the `evaluation.py` file:

    $ ./build-standard/micropython /path/to/evaluation.py
    

### ESP32 port

To build on ESP32 port, you need to setup [ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/v5.1.1/esp32/get-started/index.html) and the build environment. Version `release-v5.1.1` is used in this tutorial. 

This tutorial assumes `idf.py` is added to the `PATH` environment variable. This is done in Step 4 of the [ESP-IDF get started tutorial](https://docs.espressif.com/projects/esp-idf/en/v5.1.1/esp32/get-started/linux-macos-setup.html#get-started-set-up-env).

    ```bash
    $ . ~/esp/esp-idf/export.sh
    ```

When ESP-IDF is set up, come back to your MicroPython directory with the same terminal and follow below steps.

1. Make submodules
    ```bash
    $ cd ports/esp32
    $ make submodules
    ```
1. add [urdflib-ext](https://github.com/moh3nhadavi/urdflib-ext) to ESP32:

    ```bash
    LINE=$(grep -n "list(APPEND MICROPY_SOURCE_LIB" esp32_common.cmake  | cut -d : -f 1)
    sed -i "${LINE}r ../../urdflib/esp32_common.cmake.insert" esp32_common.cmake
    ```

1. Build MicroPython by:
    ``` bash
    make USER_C_MODULES=../../../urdflib/urdflib/micropython.cmake
    ```

After build, you can find the `firmware.bin` file at `build-ESP32_GENERIC` directory. follow [this Link](https://github.com/micropython/micropython/blob/v1.21.0/docs/esp32/tutorial/intro.rst) to flash this firmware on your ESP32 microcontroller and try the `evaluation.py` file.

> **_NOTE:_**  replace USB or serial port `/dev/USB0` to the one used by your device, and firmware `esp32-20180511-v1.9.4.bin` with your `build-ESP32_GENERIC/firmware.bin` file.

for example:

    ```bash
    esptool.py --chip esp32 --port /dev/ttyS1 write_flash -z 0x1000 build-ESP32_GENERIC/firmware.bin
    ```
