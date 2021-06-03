# VictronSmartShunt-ESPHOME
 SmartShunt ve.direct to ESPHOME node


A configured uart component is required.

Example:
```yaml
victron:
  uart_id: the_uart

sensor:
  - platform: victron
    battery_voltage:
      id: bv
    battery_current:
      id: bc
```

The `uart_id` is optional.

All sensors are optional.

```
  - platform: victron
    battery_voltage:
      name: "Battery Voltage"  
      id: bv

    battery_current:
      name: "Battery Current" 
      id: bc

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
        # Multiplication factor from W to kW is 0.001
        - multiply: 0.001
      unit_of_measurement: kWh

    state_of_charge:
      id: state_of_charge
      name: "SoC"  
```

Install:
copy folder `victron` in `custom_components` folder to `~/config/esphome/custom_components/victron`

Full example in `smartshunt.yaml`

`Big thanks for help to ssieb`

```
#victron #esphome #smartshunt #bmv #ve.direct 
