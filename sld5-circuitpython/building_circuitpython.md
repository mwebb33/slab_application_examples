
# Building CircuitPython
The CircuitPython port for xG24 is readily accessible through [Adafruit's CircuitPython repository](https://github.com/adafruit/circuitpython/tree/main/ports/silabs).

## How this port is organized:

- **boards/** contains the configuration files for each development board and breakout available on the port, as well as system files and both shared and SoC-specific linker files. Board configuration includes a pin mapping of the board, oscillator information, board-specific build flags, and setup for some other peripheral where applicable.
- **common-hal/** contains the port-specific module implementations, used by shared-module and shared-bindings.
- **cp_efr32_extension/** sdk extension contains a list of paths to search for components
- **gecko_sdk/** Silicon Labs Gecko SDK as submodule
- **peripherals/** contains peripheral setup files and peripheral mapping information, sorted by family and sub-variant. Most files in this directory can be generated with the python scripts in **tools/**.
- **supervisor/** contains port-specific implementations of internal flash and serial, as well as the **port.c** file, which initializes the port at startup.
- **tools/** contains Silicon Labs configurator (SLC) tool, python scripts for generating peripheral and pin mapping files in **peripherals/** and **board/**.

At the root level, refer to **mpconfigboard.h** and **mpconfigport.mk** for port specific settings and a list of enabled modules.

## Prerequisites
Please ensure you set up your build environment appropriately, as per the guide. You will need:

- Linux: https://learn.adafruit.com/building-circuitpython/linux
- Windows Subsystem for Linux (WSL): https://learn.adafruit.com/building-circuitpython/windows-subsystem-for-linux
- Windows: Not supported yet
- MacOS: Not supported yet

Install necessary packages
```bash
$ sudo apt install default-jre gcc-arm-none-eabi python3 python3-pip git git-lfs gettext uncrustify
$ sudo python -m pip install --upgrade pip
```

## Build instructions

Ensure your clone of Circuitpython is ready to build by following the [guide on the Adafruit Website](https://learn.adafruit.com/building-circuitpython/build-circuitpython). This includes installing the toolchain, synchronizing submodules, and running `mpy-cross`.

Clone the source code of CircuitPython from Github:
```bash
$  git clone https://github.com/adafruit/circuitpython.git
$  cd circuitpython
$  make fetch-submodules
```
Checkout the branch or tag you want to build. For example:
```bash
$  git checkout main
```
Following the guideline below to install required packages for SLC tool:
    https://www.silabs.com/documents/public/user-guides/ug520-software-project-generation-configuration-with-slc-cli.pdf

Once the one-time build tasks are complete, you can build at any time by navigating to the port directory:
```bash
$ make BOARD=explorerkit_xg24_brd2703a
```
You may also build with certain flags available in the makefile, depending on your board and development goals:
```bash
$ make BOARD=explorerkit_xg24_brd2703a DEBUG=1
```
Clean project by using:
```bash
$ make BOARD=explorerkit_xg24_brd2703a clean
```
You can use the following command build for each xG24 board:

| Board                       | Build CMD                                  |
| --------------------------- | ------------------------------------------ |
| xG24 Dev Kit                | devkit_xg24_brd2601b                       |
| xG24 Explorer Kit           | explorerkit_xg24_brd2703a                  |
| Sparkfun Thing Plus MGM240P | sparkfun_thingplus_matter_mgm240p_brd2704a |

Once the build process is complete, navigate to the build folder for the corresponding board, such as build-sparkfun_thingplus_matter_mgm240p_brd2704a, and verify that the **firmware.bin** file is present. This file contains the compiled binary firmware and is the file that should be uploaded to the microcontroller to run the application. By confirming the presence of the firmware.bin file, you can ensure that the build completed successfully and that the firmware is ready to be loaded onto the board.

## Troubleshooting

If you encounter issues with the libbluetooth.a file, it may be due to an incomplete or corrupted clone of the Gecko SDK submodule. To prevent this issue, make sure to install **git-lfs** before cloning the submodule. 
```log
./circuitpython/ports/silabs/gecko_sdk/protocol/bluetooth/lib/EFR32MG24/GCC/libbluetooth.a: file format not recognized
./circuitpython/ports/silabs/gecko_sdk/protocol/bluetooth/lib/EFR32MG24/GCC/libbluetooth.a:1: syntax error
collect2: error: ld returned 1 exit status
make[1]: *** [Makefile:150: build-devkit_xg24_brd2601b/firmware.out] Error 1
make: *** [Makefile:141: build-devkit_xg24_brd2601b/firmware.bin] Error 2
```