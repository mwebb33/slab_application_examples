# Third-Party Hardware Drivers

Third-Party Hardware Drivers are GSDK Extension to provide support for third-party external hardware.

- **Scaling GSDK functionality with SDK Extension**
   - One-click solution for tested third-party sensor boards
   - Developed wrapper can be used to add untested boards easily
- **Accelerate Design Phase**
  - Quick and easy integration of 1,100+ devices manufactured by different board providers
  - 10x faster than developing individual HW drivers from scratch
- **Customer Self-Serve Support**
  - Easy to start, fast to learn, time-saving
  - Based on third-party boards, diverse applications can be created


![ThirdPartyHwDrvExt](doc/layers.png)

This extension consumes the [mikroSDK Click Plugin](https://github.com/MikroElektronika/mikrosdk_click_v2) for the [mikroSDK](https://github.com/MikroElektronika/mikrosdk_v2) developed by [Mikroe](https://www.mikroe.com/).


**See the [instructions](/application-examples/<docspace-docleaf-version>/ae-getting-started/how-do-you-use-it#adding-sdk-extensions-for-hardware-drivers) of the Getting Started section for more information.**

## Software Components

The following drivers are tested and integrated into the extension. 

Besides the integrated drivers, it is possible to add additional drivers from the [mikroSDK Click Plugin Repository](https://github.com/MikroElektronika/mikrosdk_click_v2) by using the [Services] -> mikroSDK 2.0 SDK - Peripheral Drivers software components.

Software components in the mikroSDK 2.0 SDK - Peripheral Drivers are implemented as the required peripheral driver interfaces for the MikroSDK Click plugin.

In general, the software components are named in accordance with the following naming convention.

**<IC_NAME> - <BOARD_NAME> (<BOARD_VENDOR>) - \<INTERFACE>**

Where,
  - **IC_NAME** - The name of the integrated circuit on the external board. (e.g.,: SSD1306)
  - **BOARD_NAME** - The name of the external board. (OLED W Click) 
  - **BOARD_VENDOR** - External board vendor. (e.g.,: Mikroe, Sparkfun, Adafruit, etc.)
  - **INTERFACE** - Optional parameter to indicate the communication interface in case the SDK extension implements multiple drivers for the same device with different interfaces. (e.g.,: SPI, I2C)

Although, the drivers were mainly developed and tested with the **<BOARD_NAME>** external board, in most cases they should work with other boards using the same IC too.

 **Example**

 SSD1306 - Micro OLED Breakout (Sparkfun) - I2C driver was developed and tested with Sparkfun Micro OLED Breakout board; however, it can work (it may require changing the I2C address/display resolution in the configuration by the display board) with most of the OLED displays are available on the market controlled by the SSD1306 display controller.


### **Audio & Voice**
 - CMT_8540S_SMT - Buzz 2 Click (Mikroe)

### **Display & LED**
 - SSD1306 - Micro OLED Breakout (Sparkfun) - I2C
 - SSD1306 - OLED W Click (Mikroe) - SPI

### **Human Machine Interface**
 - CAP1166 - Capacitive Touch 2 Click (Mikroe)

### **Motor Control**
 - LB11685AV - Brushless 16 Click (Mikroe)

### **Sensors**
 - BMA400 - Accel 5 Click (Mikroe)
 - MAXM86161 - Heart Rate 2 Click (Mikroe)
 - SHTC3 - Temp&Hum 9 Click (Mikroe)
 - Type 5 - Pocket Geiger Radiation (Sparkfun)

### **Services**
 - GLIB - OLED Graphics Library
 - mikroSDK 2.0 SDK - Peripheral Drivers
   - ADC
   - Digital I/O
   - I2C
   - PWM
   - SPI
   - UART

### **Wireless Connectivity**
 - ID-12LA - RFID Reader (Sparkfun) - I2C