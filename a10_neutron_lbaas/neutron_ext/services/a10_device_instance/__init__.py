# For backwards compatibility with the service_plugin name used in the neutron.conf file:
# a10_neutron_lbaas.neutron_ext.services.a10_device_instance.plugin.A10DeviceInstancePlugin

from a10_neutron_lbaas.neutron_ext.services.a10_device import plugin
import sys
sys.modules['a10_neutron_lbaas.neutron_ext.services.a10_device_instance.plugin'] = plugin
