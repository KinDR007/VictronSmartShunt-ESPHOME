import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, text_sensor
from esphome.const import (
    CONF_BATTERY_VOLTAGE,
    CONF_ID,
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_EMPTY,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_VOLTAGE,
    ICON_CURRENT_AC,
    ICON_EMPTY,
    ICON_FLASH,
    ICON_PERCENT,
    ICON_POWER,
    ICON_TIMELAPSE,
    STATE_CLASS_MEASUREMENT,
    UNIT_AMPERE,
    UNIT_CELSIUS,
    UNIT_EMPTY,
    UNIT_MINUTE,
    UNIT_PERCENT,
    UNIT_VOLT,
    UNIT_WATT,
    UNIT_WATT_HOURS,
)

from . import CONF_VICTRON_SMART_SHUNT_ID, VictronSmartShuntComponent

CONF_INSTANTENEOUS_POWER = "instanteneous_power"
CONF_TIME_TO_GO = "time_to_go"
CONF_STATE_OF_CHARGE = "state_of_charge"
CONF_CONSUMED_AMP_HOURS = "consumed_amp_hours"
CONF_MIN_BATTERY_VOLTAGE = "min_battery_voltage"
CONF_MAX_BATTERY_VOLTAGE = "max_battery_voltage"
CONF_AMOUNT_OF_CHARGED = "amount_of_charged"
CONF_BMV_ALARM_TEXT = "bmv_alarm_text"
CONF_BMV_TEXT = "bmv_text"
CONF_LAST_FULL_CHARGE = "last_full_charge"
CONF_DEEPEST_DISCHARGE = "deepest_discharge"
CONF_LAST_DISCHARGE = "last_discharge"
CONF_DISCHARGED_ENERGY = "discharged_energy"
CONF_NUMBER_OF_FULL_DIS = "number_of_full_dis"
CONF_NUMBER_OF_CHARGE_CYCLES = "number_of_charge_cycles"
CONF_DISCHARGED_ENERGY = "discharged_energy"

CONF_MAX_POWER_YESTERDAY = "max_power_yesterday"
CONF_MAX_POWER_TODAY = "max_power_today"
CONF_YIELD_TOTAL = "yield_total"
CONF_YIELD_YESTERDAY = "yield_yesterday"
CONF_YIELD_TODAY = "yield_today"
CONF_PANEL_VOLTAGE = "panel_voltage"
CONF_PANEL_POWER = "panel_power"
CONF_BATTERY_CURRENT = "battery_current"
CONF_DAY_NUMBER = "day_number"
CONF_CHARGER_STATUS = "charger_status"
CONF_ERROR_CODE = "error_code"
CONF_TRACKER_OPERATION = "tracker_operation"
CONF_LOAD_CURRENT = "load_current"
CONF_BATTERY_TEMPERATURE = "battery_temperature"

CONF_CHARGER_TEXT = "charger_text"
CONF_ERROR_TEXT = "error_text"
CONF_ALARM_REASON_TEXT = "alarm_reason_text"
CONF_TRACKER_TEXT = "tracker_text"
CONF_FW_VERSION = "fw_version"
CONF_PID = "pid"

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_VICTRON_SMART_SHUNT_ID): cv.use_id(
            VictronSmartShuntComponent
        ),
        cv.Optional(CONF_MAX_POWER_YESTERDAY): sensor.sensor_schema(
            unit_of_measurement=UNIT_WATT,
            icon=ICON_POWER,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_POWER,
        ),
        cv.Optional(CONF_MAX_POWER_TODAY): sensor.sensor_schema(
            unit_of_measurement=UNIT_WATT,
            icon=ICON_POWER,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_POWER,
        ),
        cv.Optional(CONF_YIELD_TOTAL): sensor.sensor_schema(
            unit_of_measurement=UNIT_WATT_HOURS,
            icon=ICON_POWER,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_POWER,
        ),
        cv.Optional(CONF_YIELD_YESTERDAY): sensor.sensor_schema(
            unit_of_measurement=UNIT_WATT_HOURS,
            icon=ICON_POWER,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_POWER,
        ),
        cv.Optional(CONF_YIELD_TODAY): sensor.sensor_schema(
            unit_of_measurement=UNIT_WATT_HOURS,
            icon=ICON_POWER,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_POWER,
        ),
        cv.Optional(CONF_PANEL_VOLTAGE): sensor.sensor_schema(
            unit_of_measurement=UNIT_VOLT,
            icon=ICON_FLASH,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_VOLTAGE,
        ),
        cv.Optional(CONF_PANEL_POWER): sensor.sensor_schema(
            unit_of_measurement=UNIT_WATT,
            icon=ICON_POWER,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_POWER,
        ),
        cv.Optional(CONF_BATTERY_VOLTAGE): sensor.sensor_schema(
            unit_of_measurement=UNIT_VOLT,
            icon=ICON_FLASH,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_VOLTAGE,
        ),
        cv.Optional(CONF_BATTERY_CURRENT): sensor.sensor_schema(
            unit_of_measurement=UNIT_AMPERE,
            icon=ICON_CURRENT_AC,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_CURRENT,
        ),
        cv.Optional(CONF_DAY_NUMBER): sensor.sensor_schema(
            unit_of_measurement=UNIT_EMPTY,
            icon=ICON_EMPTY,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_EMPTY,
        ),
        cv.Optional(CONF_CHARGER_STATUS): sensor.sensor_schema(
            unit_of_measurement=UNIT_EMPTY,
            icon=ICON_EMPTY,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_EMPTY,
        ),
        cv.Optional(CONF_ERROR_CODE): sensor.sensor_schema(
            unit_of_measurement=UNIT_EMPTY,
            icon=ICON_EMPTY,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_EMPTY,
        ),
        cv.Optional(CONF_TRACKER_OPERATION): sensor.sensor_schema(
            unit_of_measurement=UNIT_EMPTY,
            icon=ICON_EMPTY,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_EMPTY,
        ),
        cv.Optional(CONF_LOAD_CURRENT): sensor.sensor_schema(
            unit_of_measurement=UNIT_AMPERE,
            icon=ICON_CURRENT_AC,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_CURRENT,
        ),
        cv.Optional(CONF_BATTERY_TEMPERATURE): sensor.sensor_schema(
            unit_of_measurement=UNIT_CELSIUS,
            icon=ICON_EMPTY,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_TEMPERATURE,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_CHARGER_TEXT): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {cv.GenerateID(): cv.declare_id(text_sensor.TextSensor)}
        ),
        cv.Optional(CONF_ERROR_TEXT): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {cv.GenerateID(): cv.declare_id(text_sensor.TextSensor)}
        ),
        cv.Optional(CONF_ALARM_REASON_TEXT): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {cv.GenerateID(): cv.declare_id(text_sensor.TextSensor)}
        ),
        cv.Optional(CONF_TRACKER_TEXT): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {cv.GenerateID(): cv.declare_id(text_sensor.TextSensor)}
        ),
        cv.Optional(CONF_FW_VERSION): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {cv.GenerateID(): cv.declare_id(text_sensor.TextSensor)}
        ),
        cv.Optional(CONF_PID): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {cv.GenerateID(): cv.declare_id(text_sensor.TextSensor)}
        ),
        cv.Optional(CONF_INSTANTENEOUS_POWER): sensor.sensor_schema(
            unit_of_measurement=UNIT_WATT,
            icon=ICON_POWER,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_POWER,
        ),
        cv.Optional(CONF_TIME_TO_GO): sensor.sensor_schema(
            unit_of_measurement=UNIT_MINUTE,
            icon=ICON_TIMELAPSE,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_EMPTY,
        ),
        cv.Optional(CONF_STATE_OF_CHARGE): sensor.sensor_schema(
            unit_of_measurement=UNIT_PERCENT,
            icon=ICON_PERCENT,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_EMPTY,
        ),
        cv.Optional(CONF_CONSUMED_AMP_HOURS): sensor.sensor_schema(
            unit_of_measurement=UNIT_AMPERE,
            icon=ICON_CURRENT_AC,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_POWER,
        ),
        cv.Optional(CONF_BMV_ALARM_TEXT): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {cv.GenerateID(): cv.declare_id(text_sensor.TextSensor)}
        ),
        cv.Optional(CONF_BMV_TEXT): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {cv.GenerateID(): cv.declare_id(text_sensor.TextSensor)}
        ),
        cv.Optional(CONF_MIN_BATTERY_VOLTAGE): sensor.sensor_schema(
            unit_of_measurement=UNIT_VOLT,
            icon=ICON_FLASH,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_VOLTAGE,
        ),
        cv.Optional(CONF_MAX_BATTERY_VOLTAGE): sensor.sensor_schema(
            unit_of_measurement=UNIT_VOLT,
            icon=ICON_FLASH,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_VOLTAGE,
        ),
        cv.Optional(CONF_AMOUNT_OF_CHARGED): sensor.sensor_schema(
            unit_of_measurement=UNIT_WATT_HOURS,
            icon=ICON_POWER,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_POWER,
        ),
        cv.Optional(CONF_LAST_FULL_CHARGE): sensor.sensor_schema(
            unit_of_measurement=UNIT_MINUTE,
            icon=ICON_TIMELAPSE,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_EMPTY,
        ),
        cv.Optional(CONF_DEEPEST_DISCHARGE): sensor.sensor_schema(
            unit_of_measurement=UNIT_AMPERE,
            icon=ICON_CURRENT_AC,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_CURRENT,
        ),
        cv.Optional(CONF_LAST_DISCHARGE): sensor.sensor_schema(
            unit_of_measurement=UNIT_AMPERE,
            icon=ICON_CURRENT_AC,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_CURRENT,
        ),
        cv.Optional(CONF_DISCHARGED_ENERGY): sensor.sensor_schema(
            unit_of_measurement=UNIT_WATT_HOURS,
            icon=ICON_POWER,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_POWER,
        ),
        cv.Optional(CONF_NUMBER_OF_FULL_DIS): sensor.sensor_schema(
            unit_of_measurement=UNIT_EMPTY,
            icon=ICON_EMPTY,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_EMPTY,
        ),
        cv.Optional(CONF_NUMBER_OF_CHARGE_CYCLES): sensor.sensor_schema(
            unit_of_measurement=UNIT_EMPTY,
            icon=ICON_EMPTY,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_EMPTY,
        ),
    }
)

def to_code(config):
    var = yield cg.get_variable(config[CONF_VICTRON_SMART_SHUNT_ID])

    if CONF_MAX_POWER_YESTERDAY in config:
        sens = yield sensor.new_sensor(config[CONF_MAX_POWER_YESTERDAY])
        cg.add(var.set_max_power_yesterday_sensor(sens))

    if CONF_MAX_POWER_TODAY in config:
        sens = yield sensor.new_sensor(config[CONF_MAX_POWER_TODAY])
        cg.add(var.set_max_power_today_sensor(sens))

    if CONF_YIELD_TOTAL in config:
        sens = yield sensor.new_sensor(config[CONF_YIELD_TOTAL])
        cg.add(var.set_yield_total_sensor(sens))

    if CONF_YIELD_YESTERDAY in config:
        sens = yield sensor.new_sensor(config[CONF_YIELD_YESTERDAY])
        cg.add(var.set_yield_yesterday_sensor(sens))

    if CONF_YIELD_TODAY in config:
        sens = yield sensor.new_sensor(config[CONF_YIELD_TODAY])
        cg.add(var.set_yield_today_sensor(sens))

    if CONF_PANEL_VOLTAGE in config:
        sens = yield sensor.new_sensor(config[CONF_PANEL_VOLTAGE])
        cg.add(var.set_panel_voltage_sensor(sens))

    if CONF_PANEL_POWER in config:
        sens = yield sensor.new_sensor(config[CONF_PANEL_POWER])
        cg.add(var.set_panel_power_sensor(sens))

    if CONF_BATTERY_VOLTAGE in config:
        sens = yield sensor.new_sensor(config[CONF_BATTERY_VOLTAGE])
        cg.add(var.set_battery_voltage_sensor(sens))

    if CONF_BATTERY_CURRENT in config:
        sens = yield sensor.new_sensor(config[CONF_BATTERY_CURRENT])
        cg.add(var.set_battery_current_sensor(sens))

    if CONF_LOAD_CURRENT in config:
        sens = yield sensor.new_sensor(config[CONF_LOAD_CURRENT])
        cg.add(var.set_load_current_sensor(sens))

    if CONF_DAY_NUMBER in config:
        sens = yield sensor.new_sensor(config[CONF_DAY_NUMBER])
        cg.add(var.set_day_number_sensor(sens))

    if CONF_CHARGER_STATUS in config:
        sens = yield sensor.new_sensor(config[CONF_CHARGER_STATUS])
        cg.add(var.set_charger_status_sensor(sens))

    if CONF_ERROR_CODE in config:
        sens = yield sensor.new_sensor(config[CONF_ERROR_CODE])
        cg.add(var.set_error_code_sensor(sens))

    if CONF_TRACKER_OPERATION in config:
        sens = yield sensor.new_sensor(config[CONF_TRACKER_OPERATION])
        cg.add(var.set_tracker_operation_sensor(sens))

    if CONF_CHARGER_TEXT in config:
        conf = config[CONF_CHARGER_TEXT]
        sens = cg.new_Pvariable(conf[CONF_ID])
        yield text_sensor.register_text_sensor(sens, conf)
        cg.add(var.set_charger_text_sensor(sens))

    if CONF_ERROR_TEXT in config:
        conf = config[CONF_ERROR_TEXT]
        sens = cg.new_Pvariable(conf[CONF_ID])
        yield text_sensor.register_text_sensor(sens, conf)
        cg.add(var.set_error_text_sensor(sens))

    if CONF_ALARM_REASON_TEXT in config:
        conf = config[CONF_ALARM_REASON_TEXT]
        sens = cg.new_Pvariable(conf[CONF_ID])
        yield text_sensor.register_text_sensor(sens, conf)
        cg.add(var.set_bmv_alarm_reason_sensor(sens))

    if CONF_TRACKER_TEXT in config:
        conf = config[CONF_TRACKER_TEXT]
        sens = cg.new_Pvariable(conf[CONF_ID])
        yield text_sensor.register_text_sensor(sens, conf)
        cg.add(var.set_tracker_text_sensor(sens))

    if CONF_FW_VERSION in config:
        conf = config[CONF_FW_VERSION]
        sens = cg.new_Pvariable(conf[CONF_ID])
        yield text_sensor.register_text_sensor(sens, conf)
        cg.add(var.set_fw_version_sensor(sens))

    if CONF_PID in config:
        conf = config[CONF_PID]
        sens = cg.new_Pvariable(conf[CONF_ID])
        yield text_sensor.register_text_sensor(sens, conf)
        cg.add(var.set_pid_sensor(sens))

    if CONF_INSTANTENEOUS_POWER in config:
        sens = yield sensor.new_sensor(config[CONF_INSTANTENEOUS_POWER])
        cg.add(var.set_instantaneous_power_sensor(sens))

    if CONF_TIME_TO_GO in config:
        sens = yield sensor.new_sensor(config[CONF_TIME_TO_GO])
        cg.add(var.set_time_to_go_sensor(sens))

    if CONF_STATE_OF_CHARGE in config:
        sens = yield sensor.new_sensor(config[CONF_STATE_OF_CHARGE])
        cg.add(var.set_state_of_charge_sensor(sens))

    if CONF_CONSUMED_AMP_HOURS in config:
        sens = yield sensor.new_sensor(config[CONF_CONSUMED_AMP_HOURS])
        cg.add(var.set_consumed_amp_hours_sensor(sens))

    if CONF_BATTERY_TEMPERATURE in config:
        sens = yield sensor.new_sensor(config[CONF_BATTERY_TEMPERATURE])
        cg.add(var.set_battery_temperature_sensor(sens))
    # **************************** SS***************
    if CONF_BMV_ALARM_TEXT in config:
        conf = config[CONF_BMV_ALARM_TEXT]
        sens = cg.new_Pvariable(conf[CONF_ID])
        yield text_sensor.register_text_sensor(sens, conf)
        cg.add(var.set_bmv_alarm_sensor(sens))

    if CONF_BMV_TEXT in config:
        conf = config[CONF_BMV_TEXT]
        sens = cg.new_Pvariable(conf[CONF_ID])
        yield text_sensor.register_text_sensor(sens, conf)
        cg.add(var.set_bmv_sensor(sens))

    if CONF_AMOUNT_OF_CHARGED in config:
        sens = yield sensor.new_sensor(config[CONF_AMOUNT_OF_CHARGED])
        cg.add(var.set_amount_of_charged_sensor(sens))

    if CONF_MIN_BATTERY_VOLTAGE in config:
        sens = yield sensor.new_sensor(config[CONF_MIN_BATTERY_VOLTAGE])
        cg.add(var.set_min_battery_voltage_sensor(sens))

    if CONF_MAX_BATTERY_VOLTAGE in config:
        sens = yield sensor.new_sensor(config[CONF_MAX_BATTERY_VOLTAGE])
        cg.add(var.set_max_battery_voltage_sensor(sens))

    if CONF_LAST_FULL_CHARGE in config:
        sens = yield sensor.new_sensor(config[CONF_LAST_FULL_CHARGE])
        cg.add(var.set_last_full_charge_sensor(sens))

    if CONF_DEEPEST_DISCHARGE in config:
        sens = yield sensor.new_sensor(config[CONF_DEEPEST_DISCHARGE])
        cg.add(var.set_depth_deepest_dis_sensor(sens))

    if CONF_LAST_DISCHARGE in config:
        sens = yield sensor.new_sensor(config[CONF_LAST_DISCHARGE])
        cg.add(var.set_depth_of_the_last_discharge_sensor(sens))

    if CONF_DISCHARGED_ENERGY in config:
        sens = yield sensor.new_sensor(config[CONF_DISCHARGED_ENERGY])
        cg.add(var.set_amount_of_discharged_energy_sensor(sens))

    if CONF_NUMBER_OF_FULL_DIS in config:
        sens = yield sensor.new_sensor(config[CONF_NUMBER_OF_FULL_DIS])
        cg.add(var.set_number_of_full_discharges_sensor(sens))

    if CONF_NUMBER_OF_CHARGE_CYCLES in config:
        sens = yield sensor.new_sensor(config[CONF_NUMBER_OF_CHARGE_CYCLES])
        cg.add(var.set_number_of_charge_cycles_sensor(sens))
