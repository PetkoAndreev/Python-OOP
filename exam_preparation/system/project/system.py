from typing import List

from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        # Create a PowerHardware instance and add it to the hardware list
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        # Create a HeavyHardware instance and add it to the hardware list
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        # •	If the hardware with the given name does NOT exist, return a message "Hardware does not exist"
        # •	Otherwise, create an ExpressSoftware instance, install it on the hardware (if possible) and add it to the software list (if installed successfully)
        # •	If the installation is not possible return the message of the raised Exception
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return "Hardware does not exist"
        except Exception as ex:
            return str(ex)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        # •	If the hardware with the given name does NOT exist, return a message "Hardware does not exist"
        # •	Otherwise, create a LightSoftware instance, install it on the hardware (if possible) and add it to the software list (if installed successfully)
        # •	If the installation is not possible return the message of the raised Exception
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return "Hardware does not exist"
        except Exception as ex:
            return str(ex)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        # •	If both components exist on the system, uninstall the software from the given hardware
        # •	Otherwise, return a message "Some of the components do not exist"
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [s for s in System._software if s.name == software_name][0]
            hardware.uninstall(software)
            System._software.remove(software)
        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        result = 'System Analysis\n'
        result += f'Hardware Components: {len(System._hardware)}\n'
        result += f'Software Components: {len(System._software)}\n'
        memory_used = sum([h.memory_used for h in System._hardware])
        total_memory = sum([h.memory for h in System._hardware])
        capacity_used = sum([h.capacity_used for h in System._hardware])
        total_capacity = sum([h.capacity for h in System._hardware])
        result += f'Total Operational Memory: {memory_used} / {total_memory}\n'
        result += f'Total Capacity Taken: {capacity_used} / {total_capacity}'
        return result

    @staticmethod
    def system_split():
        result = ''
        for h in System._hardware:
            result += h.__repr__()
        return result
