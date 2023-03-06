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
 - MAX6969 - UT-M 7-SEG R Click (Mikroe)
 - SSD1306 - Micro OLED Breakout (Sparkfun) - I2C
 - SSD1306 - OLED W Click (Mikroe) - SPI

### **Human Machine Interface**
 - CAP1166 - Capacitive Touch 2 Click (Mikroe)
 - Qwiic Joystick (Sparkfun)

### **Interface**
 - W5500 - ETH WIZ Click (Mikroe)

### **Miscellaneous**
 - LCA717 - Relay 2 Click (Mikroe)

### **Motor Control**
 - LB11685AV - Brushless 16 Click (Mikroe)

### **Power Management**
 - MAX17048 - MAX17048EVKIT Evaluation Kits (Maxim)

### **Sensors**
 - AK9753 - Human Presence Sensor (Sparkfun) - I2C
 - AS7265x - Triad Spectroscopy Sensor (Sparkfun) - I2C
 - BMA400 - Accel 5 Click (Mikroe)
 - EM3080-W - Barcode 2 Click (Mikroe)
 - MAXM86161 - Heart Rate 2 Click (Mikroe)
 - MLX90640 - IR Array Breakout (Sparkfun)
 - MMA8452Q - Triple Axis Accelerometer Breakout (Sparkfun)
 - MQ7 - CO Click (Mikroe)
 - Qwiic Soil Moisture Sensor (Sparkfun) - I2C
 - SHTC3 - Temp&Hum 9 Click (Mikroe)
 - Type 5 - Pocket Geiger Radiation (Sparkfun)
 - VCNL4040 - Proximity Sensor (Sparkfun)
 - VL53L1X - Distance Sensor Breakout (Sparkfun)

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


## Integrate new mikroSDK 2.0 Click drivers 

The Third-Party Hardware Drivers extension provides one-click solution for tested hardware drivers allowing you to integrate 25+ hardware drivers into your project with ease.

Besides the tested hardware drivers, the extension provides a peripheral driver wrapper to connect easily the mikroSDK 2.0 Click drivers with Silicon Labs GSDK.

If you're not afraid to do some extra development, thanks to the developed wrapper, over 1,100+ hardware drivers can be added to your project from the mikroSDK 2.0 Click library. This will accelerate the design phase and provide you with a greater level of customer self-serve support.

This chapter is aimed to guide you to integrate a hardware driver from the mikroSDK 2.0 Click library using the wrappers from the *mikroSDK 2.0 SDK - Peripheral Drivers* components.

Supported peripherals so far
   - ADC
   - Digital I/O
   - I2C
   - PWM
   - SPI
   - UART

### Example - Integrate the SHTC3 Temperature and Humidity sensor driver

**Create a new project**

* **STEP 1** Open the **Simplicity Studio**
* **STEP 2** Add the **Third-Party Hardware Drivers extension**, see details [here](/application-examples/<docspace-docleaf-version>/ae-getting-started/how-do-you-use-it#adding-sdk-extensions-for-hardware-drivers).
* **STEP 3** Connect your board to the PC via a USB cable
* **STEP 4** Open the **Launcher** perspective in Simplicity Studio, select the target board
* **STEP 5** Select the **EXAMPLE PROJECTS & DEMOS** tab in the launcher view
* **STEP 6** Select an empty template project (e.g.: **Empty C Project**), click on the **Create** button
* **STEP 7** Give a name for the new project and click on the **Finish** button

**Add required peripheral drivers from the TPHD extension**

The SHTC3 Sensor has an I2C interface to communicate with the host microcontroller, you should check the required interface(s) needed by the external hardware you want to integrate the driver for. 

![MikroE-SHTC3-pinout](doc/shtc3_pinout.png)

* **STEP 1** Open the project configuration by double clicking on the *.slcp file in the folder of the project**
* **STEP 2** Select the software components tab in the project configuration view
* **STEP 3** Enable the extension and clear the quality filters
* **STEP 4** Install the I2C wrapper from [Third Party Hardware Drivers] -> [Services] -> [mikroSDK 2.0 SDK - Peripheral Drivers] -> I2C

![MikroE-SHTC3-i2c](doc/tphd_sw_mikrosdk_i2c.png)

* **STEP 5** Install Log, and Sleep Timer components
  * [Application] -> [Utility] -> Log
  * [Services] -> [Timers] -> Sleep Timer

Default I2CSPM instance is "mikroe", make sure that your I2CSPM instance is configured properly for the target board. 

See an example configuration for the EFR32xG24 Explorer Kit below.

![MikroE-SHTC3-i2cspm-mikroe](doc/tphd_sw_mikrosdk_i2cspm_mikroe.png)

Once the I2C software component is installed, the header and source files provided by this component will be available in the project's file structure.

![MikroE-SHTC3-i2c-files](doc/tphd_sw_mikrosdk_i2c_files.png)

The driver will use the I2C peripheral interfaces provided by the **drv_i2c_master.h** header file in the background.

**Add driver source files to the project**

Download the driver source files from the [mikroSDK 2.0 Click library](https://github.com/MikroElektronika/mikrosdk_click_v2).

* **STEP 1** Copy and paste the driver's folder containing the source files for the selected driver

![MikroE-SHTC3-driver-files](doc/tphd_sw_mikrosdk_driver_files.png)

* **STEP 2** Exclude the main.c and other *.c files from the temphum9/lib/example folder

![MikroE-SHTC3-exclude-example2](doc/tphd_sw_mikrosdk_exclude2.png)

![MikroE-SHTC3-exclude-example](doc/tphd_sw_mikrosdk_exclude.png)

* **STEP 3** Append the temphum9/lib/include folder to the list of the include directories

![MikroE-SHTC3-include](doc/tphd_sw_mikrosdk_include_path.png)

* **STEP 4** Enable printf for floating point numbers

![MikroE-SHTC3-float](doc/tphd_sw_mikrosdk_float.png)

**Integrate the driver**

* **STEP 1** Open the app.c file

* **STEP 2** Create a custom init function for the driver and add the required driver and driver config instances to the project.

``` c
#include "app_log.h"
#include "sl_status.h"
#include "sl_i2cspm_instances.h"
#include "sl_sleeptimer.h"

#include "temphum9.h"

static temphum9_t temphum9;
static temphum9_cfg_t temphum9_cfg;
static sl_sleeptimer_timer_handle_t handle_periodic;

sl_status_t mikroe_custom_shtc3_init(sl_i2cspm_t *i2cspm_instance);
void measure_periodic(sl_sleeptimer_timer_handle_t *handle, void *data);

sl_status_t mikroe_custom_shtc3_init(sl_i2cspm_t *i2cspm_instance)
{
  if (NULL == i2cspm_instance) {
    return SL_STATUS_INVALID_PARAMETER;
  }
  // Configure default i2csmp instance
  temphum9.i2c.handle = i2cspm_instance;

  // Call basic setup functions
  temphum9_cfg_setup(&temphum9_cfg);

  return temphum9_init(&temphum9, &temphum9_cfg) ? SL_STATUS_FAIL : SL_STATUS_OK;
}

```

The mikroSDK driver provides the temphum9_t and temphum9_cfg_t types to configure the driver.

``` c
typedef struct
{
    // Modules 

    i2c_master_t i2c;

    // ctx variable 

    uint8_t slave_address;

} temphum9_t;

typedef struct
{
    // Communication gpio pins 

    pin_name_t scl;
    pin_name_t sda;

    // static variable 

    uint32_t i2c_speed;
    uint8_t i2c_address;

} temphum9_cfg_t;
```

**Silicon Labs wrapper provides the high level configuration for the I2CSPM instance, therefore it is not required to configure the speed, pin, or any other parameters except the i2c parameter in the temphum9_t type.**

**Only the i2c.handle pointer should be configured to point to the configured I2CSPM instance.**

**Please check the provided drivers as examples for other peripheral (SPI, UART, etc.) integration.**

**Initialization**

``` c
void app_init(void)
{

  if (SL_STATUS_OK != mikroe_custom_shtc3_init(sl_i2cspm_mikroe)) {
    app_log("TempHum9 initialization failed.");
  } else {
    app_log("TempHum9 initialization succeed.");

    sl_sleeptimer_start_periodic_timer_ms(&handle_periodic, 1000,
        measure_periodic, NULL, 0, 0);
  }
}
```

**Reading and printing the measured values**

``` c
void measure_periodic(sl_sleeptimer_timer_handle_t *handle, void *data)
{
  (void) handle;
  (void) data;

  float _measurement_data[2];
  temhum9_get_temperature_and_humidity(&temphum9, TEMPHUM9_NORMAL_MODE,
      _measurement_data);
  app_log(">> Temp: %.2f °C RH: %.2f %%\n", _measurement_data[0],
      _measurement_data[1]);
}
```

**The whole example app.c**

``` c
#include "app_log.h"
#include "sl_status.h"
#include "sl_i2cspm_instances.h"
#include "sl_sleeptimer.h"

#include "temphum9.h"

static temphum9_t temphum9;
static temphum9_cfg_t temphum9_cfg;
static sl_sleeptimer_timer_handle_t handle_periodic;

sl_status_t mikroe_custom_shtc3_init(sl_i2cspm_t *i2cspm_instance);
void measure_periodic(sl_sleeptimer_timer_handle_t *handle, void *data);

sl_status_t mikroe_custom_shtc3_init(sl_i2cspm_t *i2cspm_instance)
{
  if (NULL == i2cspm_instance) {
    return SL_STATUS_INVALID_PARAMETER;
  }
  // Configure default i2csmp instance
  temphum9.i2c.handle = i2cspm_instance;

  // Call basic setup functions
  temphum9_cfg_setup(&temphum9_cfg);

  return temphum9_init(&temphum9, &temphum9_cfg) ? SL_STATUS_FAIL : SL_STATUS_OK;
}

/***************************************************************************//**
 * Initialize application.
 ******************************************************************************/
void app_init(void)
{

  if (SL_STATUS_OK != mikroe_custom_shtc3_init(sl_i2cspm_mikroe)) {
    app_log("TempHum9 initialization failed.");
  } else {
    app_log("TempHum9 initialization succeed.");

    sl_sleeptimer_start_periodic_timer_ms(&handle_periodic, 1000,
        measure_periodic, NULL, 0, 0);
  }
}

void measure_periodic(sl_sleeptimer_timer_handle_t *handle, void *data)
{
  (void) handle;
  (void) data;

  float _measurement_data[2];
  temhum9_get_temperature_and_humidity(&temphum9, TEMPHUM9_NORMAL_MODE,
      _measurement_data);
  app_log(">> Temp: %.2f °C RH: %.2f %%\n", _measurement_data[0],
      _measurement_data[1]);
}

/***************************************************************************//**
 * App ticking function.
 ******************************************************************************/
void app_process_action(void)
{

}
```

* **Build and flash the application**

 The driver and the demo application should operate properly if you connect the Temphum9 board to the explorer kit.

**Output**

![SHTC3-Output](doc/tphd_sw_mikrosdk_output.png)