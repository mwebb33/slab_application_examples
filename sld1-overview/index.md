# Overview
**Application Examples Program (AEP)** is an umbrella term that includes the different promotion and enablement HW drivers, virtual applications or reference designs. 

Strong emphases is put on a building block concept, where these can be combined and people can experiment even more complex applications reusing these sample codes. The aim is to extend the operation to 3rd party HW platforms / ecosystems as well, not just supporting our development kits.


![AEP](doc/aep_layers.png)

**As the go-to provider for IoT solutions, we provide developers at all levels with an easy to use, accessible application examples they can use to speed their developments and get to market faster.**

## Simple Sample Code

Simple sample code is the most basic product from the AEP program portfolio . Those mainly intend to demonstrate peripherals and low level platform components (NVM3, crypto, BL).

The goal is provide a comprehensive set of examples demonstrating their features from different angles for different purposes.

## Hardware Driver

Hardware drivers are basic drivers for external hardware such as sensors, displays, or transmitters that would commonly be used with Silicon Labs products.

The scope of the hardware driver development is to provide feature-rich basic drivers for the market-leading development shields (Sparkfun Qwiic, MikroE Click platforms) commonly used for rapid prototyping by professionals and hobbyists for university and hobby projects.

Those mainly intend to provide basic building blocks for application development.

## Virtual Application

Virtual application is a higher abstraction layer, it intends to promote the capabilities of hardware drivers integrated into a wireless stack like BLE.

Virtual applications are either wireless stack applications or mostly wireless stack applications using simple sample codes and hardware drivers to promote the platform and the AEP component features. Those applications form ready to build like Simplicity Studio projects.

Complex virtual applications typically provide solutions for popular IoT products, like smart door lock, speech controlling and so on.


![AEP](doc/virtual_app.png)


## Example - Bluetooth Ethernet Gateway Application

### Overview

This project aims to implement a simple Bluetooth-Ethernet Thin Gateway, the sensor measures and collects data from the device's environment and the gateway request the results via BLE.

When the device in connected to a sensor peripheral the gateway reads the BLE characteristics to retrieve the measured temperature and humidity. The measurements results are uploaded to dweet.io via the Ethernet Click board.

![AEP](doc/example/overview_eth_ble_gateway.png)

### Hardware Setup

The ETH WIZ Click can be plugged into the BGM220 Bluetooth Module Explorer Kit via the mikroBus socket.

![AEP](doc/example/hardware_setup.png)

### Cloud Service

The temperature and humidity values measured by the Thunderboard Sense 2 development kit. Values are trasmitted via BLE from the data sender device to the data collector environment. 

The measured environment data are transferred to the cloud service via Ethernet connection.

The trasmitted values can be visualised on the graphical interface of the cloud service.

![AEP](doc/example/dweet.png)