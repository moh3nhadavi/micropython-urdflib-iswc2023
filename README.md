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
   $ git clone https://github.com/micropython/micropython.git
    ```
    ```bash
   $ git clone https://github.com/moh3nhadavi/micropython-urdflib
   ```

## Step 2: Configure MicroPython

1. Navigate to the MicroPython repository:

    ```bash
    cd micropython
    ```

1. Open the `.gitmodules` file located in the MicroPython repository.
    
    ```bash
    nano .gitmodules
    ```

1. Add the following lines to the end of the `.gitmodules` file:

    ```bash
    [submodule "lib/urdflib-ext"]
        path = lib/urdflib-ext
        url = git@github.com:moh3nhadavi/urdflib-ext.git
    ```
1. Save and exit the text editor.

1. Initialize the submodules:

    ```bash
    git submodule init
    ```
    
1. Update the submodules:
    ```bash
    git submodule update
    ```
1. build [MicroPython cross-compiler](https://github.com/micropython/micropython/blob/master/mpy-cross)
    ```bash
    $ cd mpy-cross
    $ make
    ```


## Step 3: Build and Run MicroPython with "urdflib"

### UNIX port

To build on UNIX port:

    $ cd ../ports/unix
    $ make submodules
    $ make USER_C_MODULES=../../../micropython-urdflib

After build, you can run it by:
    
    $ ./build-standard/micropython

To run the `evaluation.py` file:

    $ ./build-standard/micropython /path/to/evaluation.py
    

### ESP32 port

To build on ESP32 port, you need to setup [ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/release-v4.4/esp32/get-started/index.html) and the build environment. I used `release-v4.4`. Whenever you set it up, comeback to your MicroPython directory with the same terminal and follow below steps.


1. Make submodules
    ```bash
    $ cd ports/esp32
    $ make submodules
    ```
1. add [urdflib-ext](https://github.com/moh3nhadavi/urdflib-ext) to ESP32:
    - open `CMakeLists.txt` file:
        ```bash
        nano main/CMakeLists.txt
        ```
    - find this section:
    ```txt
    set(MICROPY_SOURCE_LIB
        ${MICROPY_DIR}/lib/littlefs/lfs1.c
        ${MICROPY_DIR}/lib/littlefs/lfs1_util.c
        ${MICROPY_DIR}/lib/littlefs/lfs2.c
        ${MICROPY_DIR}/lib/littlefs/lfs2_util.c
        ${MICROPY_DIR}/lib/mbedtls_errors/mp_mbedtls_errors.c
        ${MICROPY_DIR}/lib/oofatfs/ff.c
        ${MICROPY_DIR}/lib/oofatfs/ffunicode.c
    )
    ```

    - replace it with this:
    ```text
    set(MICROPY_SOURCE_LIB
        ${MICROPY_DIR}/lib/littlefs/lfs1.c
        ${MICROPY_DIR}/lib/littlefs/lfs1_util.c
        ${MICROPY_DIR}/lib/littlefs/lfs2.c
        ${MICROPY_DIR}/lib/littlefs/lfs2_util.c
        ${MICROPY_DIR}/lib/mbedtls_errors/mp_mbedtls_errors.c
        ${MICROPY_DIR}/lib/oofatfs/ff.c
        ${MICROPY_DIR}/lib/oofatfs/ffunicode.c
        ${MICROPY_DIR}/lib/urdflib-ext/zix/allocator.c
        ${MICROPY_DIR}/lib/urdflib-ext/zix/btree.c
        ${MICROPY_DIR}/lib/urdflib-ext/zix/bump_allocator.c
        ${MICROPY_DIR}/lib/urdflib-ext/zix/digest.c
        ${MICROPY_DIR}/lib/urdflib-ext/zix/errno_status.c
        ${MICROPY_DIR}/lib/urdflib-ext/zix/hash.c
        ${MICROPY_DIR}/lib/urdflib-ext/zix/path.c
        ${MICROPY_DIR}/lib/urdflib-ext/zix/ring.c
        ${MICROPY_DIR}/lib/urdflib-ext/zix/status.c
        ${MICROPY_DIR}/lib/urdflib-ext/zix/string_view.c
        ${MICROPY_DIR}/lib/urdflib-ext/zix/system.c
        ${MICROPY_DIR}/lib/urdflib-ext/zix/tree.c
        ${MICROPY_DIR}/lib/urdflib-ext/serd/base64.c
        ${MICROPY_DIR}/lib/urdflib-ext/serd/byte_source.c
        ${MICROPY_DIR}/lib/urdflib-ext/serd/env.c
        ${MICROPY_DIR}/lib/urdflib-ext/serd/n3.c
        ${MICROPY_DIR}/lib/urdflib-ext/serd/node.c
        ${MICROPY_DIR}/lib/urdflib-ext/serd/reader.c
        ${MICROPY_DIR}/lib/urdflib-ext/serd/string.c
        ${MICROPY_DIR}/lib/urdflib-ext/serd/system.c
        ${MICROPY_DIR}/lib/urdflib-ext/serd/uri.c
        ${MICROPY_DIR}/lib/urdflib-ext/serd/writer.c
        ${MICROPY_DIR}/lib/urdflib-ext/sord/sord.c
        ${MICROPY_DIR}/lib/urdflib-ext/sord/syntax.c
    )
    ```
    - Save the file and exit.
1. Build MicroPython by:
    ``` bash
    make USER_C_MODULES=../../../../micropython-urdflib/urdflib/micropython.cmake
    ```

After build, you can find the `firmware.bin` file at `build-GENERIC` directory. follow [this Link](https://github.com/micropython/micropython/blob/v1.20.0/docs/esp32/tutorial/intro.rst) to build this firmware on your ESP32 microcontroller and try the `evaluation.py` file.

> **_NOTE:_**  replace `esp32-20180511-v1.9.4.bin` with your `firmware.bin` file.
