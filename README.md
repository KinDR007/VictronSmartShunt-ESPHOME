# VictronSmartShunt-ESPHOME

ESPHome component to monitor a Victron BMV and SmartShunt via ve.direct / UART TTL.

## Supported devices

All BMV and SmartShunt providing a ve.direct port.

## Tested devices

* Victron SmartShunt 500A/50mV

## Requirements

* [ESPHome 2021.10 or higher](https://github.com/esphome/esphome/releases).
* Generic ESP32 or ESP8266 board

## Schematics

```
                UART-TTL
┌────────────────┐                ┌──────────────────┐
│           GND o│<-------------->│o GND             │
│ BMV or     RX o│                │       ESP32/     │
│ SmartShunt TX o│--------------->│o D7   ESP8266    │<-- GND
│       5V/3.3V o│                │                  │<-- 3.3V
└────────────────┘                └──────────────────┘

# UART-TTL jack (JST-PH 2.0mm pinch)
┌────────────────┐
│                │
│ O   O   O   O  │
│VCC  TX  RX GND │
└─── ─────── ────┘
```

If you are unsure about to pin order please measure the voltage between GND and VCC (5V/3.3V). If you measure a positive voltage you know the position of VCC and GND!

### JST-PH jack

|  Pin  | Purpose | ESP pin |
| :---: | :------ | :------ |
| **1** | **GND** | GND     |
|   2   | RX      |         |
| **3** | **TX**  | D7 (RX) |
|   4   | 5V      |         |

## Installation

You can install this component with [ESPHome external components feature](https://esphome.io/components/external_components.html).

Example:

```yaml
external_components:
  - source: github://KinDR007/VictronSmartShunt-ESPHOME@main

uart:
  id: the_uart
  rx_pin: D7
  baud_rate: 19200
  stop_bits: 1
  data_bits: 8
  parity: NONE
  rx_buffer_size: 256

victron_smart_shunt:
  uart_id: the_uart

sensor:
  - platform: victron_smart_shunt
    battery_voltage:
      id: bv
    battery_current:
      id: bc
```

The `uart_id` is optional.

All sensors are optional (and go under the `sensor` section).

```yaml
  - platform: victron_smart_shunt
    battery_voltage:
      name: "Battery Voltage"
      id: bv

    battery_current:
      name: "Battery Current"
      id: bc

    battery_temperature:
      name: "Battery Temperature"
      id: bt

    fw_version:
      name: "fw"
      id: fw

    pid:
      name: "pid"
      id: pid

    instantaneous_power:
      name: "instantaneous power"
      id: instantaneous_power

    time_to_go:
      name: "time to go"
      id: time_to_go

    consumed_amp_hours:
      name: "consumed amp hours"
      id: consumed_amp_hours
      unit_of_measurement: Ah

    min_battery_voltage:
      name: "Min battery voltage"
      id: min_battery_voltage

    max_battery_voltage:
      name: "Max battery voltage"
      id: max_battery_voltage

    amount_of_charged:
      name: "Amount of charged"
      id:  amount_of_charged
      filters:
        - multiply: 0.001
      unit_of_measurement: kWh

    bmv_alarm:
      name: "BMV alarm"
      id: bmv_alarm

    bmv_pid:
      name: "bmv - pid"
      id: bmv_pid

    last_full_charge:
      name: "Time since last full charge"
      id: last_full_charge

    deepest_discharge:
      name: "Depth of the deepest discharge"
      id: deepest_discharge
      unit_of_measurement: Ah

    last_discharge:
      name: "Depth of the last discharge"
      id: last_discharge
      unit_of_measurement: Ah

    discharged_energy:
      name: "Amount of discharged energy"
      id: discharged_energy
      filters:
        - multiply: 0.001
      unit_of_measurement: kWh

    state_of_charge:
      id: state_of_charge
      name: "SoC"
```

The available numeric sensors are:

- `amount_of_charged`
- `battery_temperature`
- `consumed_amp_hours`
- `deepest_discharge`
- `discharged_energy`
- `discharged_energy`
- `instanteneous_power`
- `last_discharge`
- `last_full_charge`
- `max_battery_voltage`
- `min_battery_voltage`
- `number_of_charge_cycles`
- `number_of_full_dis`
- `state_of_charge`
- `time_to_go`

The available text sensors are:

- `alarm_reason_text`
- `bmv_alarm_text`
- `bmv_text`
- `charger_text`
- `error_text`
- `fw_version`
- `pid`
- `tracker_text`

See [`full example`](./esp8266-example-advanced.yaml).

`Big thanks for help to ssieb`

```
#victron #esphome #smartshunt #bmv #ve.direct
```