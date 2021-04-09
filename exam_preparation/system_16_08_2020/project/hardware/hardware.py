from project.software.software import Software


class Hardware:
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def __repr__(self):
        result = ''
        result += f'Hardware Component - {self.name}\n'
        express_soft = [s for s in self.software_components if s.type == 'Express']
        light_soft = [s for s in self.software_components if s.type == 'Light']
        result += f'Express Software Components: {len(express_soft)}\n'
        result += f'Light Software Components: {len(light_soft)}\n'
        result += f'Memory Usage: {self.memory_used} / {self.memory}\n'
        result += f'Capacity Usage: {self.capacity_used} / {self.capacity}\n'
        result += f'Type: {self.type}\n'
        result += f'Software Components: {", ".join(s.name for s in self.software_components) if self.software_components else None}'
        return result

    def install(self, software: Software):
        # If there is enough capacity and memory, add the software object to the software_components.
        # Otherwise, raise Exception with message "Software cannot be installed"
        if self.memory_available >= software.memory_consumption and self.capacity_available >= software.capacity_consumption:
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software: Software):
        # Remove the software object from the software_components
        if software in self.software_components:
            self.software_components.remove(software)

    @property
    def memory_available(self):
        return self.memory - sum([s.memory_consumption for s in self.software_components])

    @property
    def memory_used(self):
        return sum([s.memory_consumption for s in self.software_components])

    @property
    def capacity_available(self):
        return self.capacity - sum([s.capacity_consumption for s in self.software_components])

    @property
    def capacity_used(self):
        return sum([s.capacity_consumption for s in self.software_components])
