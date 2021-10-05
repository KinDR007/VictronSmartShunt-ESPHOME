import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart
from esphome.const import CONF_ID

DEPENDENCIES = ["uart"]
AUTO_LOAD = ["sensor", "text_sensor"]

victron_smart_shunt_ns = cg.esphome_ns.namespace("victron_smart_shunt")
VictronSmartShuntComponent = victron_smart_shunt_ns.class_(
    "VictronSmartShuntComponent", uart.UARTDevice, cg.Component
)

CONF_VICTRON_SMART_SHUNT_ID = "victron_smart_shunt_id"

CONFIG_SCHEMA = uart.UART_DEVICE_SCHEMA.extend(
    {
        cv.GenerateID(): cv.declare_id(VictronSmartShuntComponent),
    }
)


def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    yield uart.register_uart_device(var, config)
