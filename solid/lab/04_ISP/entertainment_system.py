class HdmiConnect:
    def connect_via_hdmi(self, device):
        pass


class RcaConnect:
    def connect_via_rca(self, device):
        pass


class EthernetConnect:
    def connect_via_ethernet(self, device):
        pass


class PowerOutletConnect:
    def connect_via_power_outlet(self, device):
        pass


class EntertainmentDevice:
    pass


class Television(EntertainmentDevice, RcaConnect, HdmiConnect, PowerOutletConnect):
    def connect_to_dvd(self, dvd_player):
        self.connect_via_rca(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_via_hdmi(game_console)

    def plug_in_power(self):
        self.connect_via_power_outlet(self)

    def connect_via_hdmi(self, device):
        return None


tv = Television()


class DvdPlayer(EntertainmentDevice, HdmiConnect, PowerOutletConnect):
    def connect_to_tv(self, television):
        self.connect_via_hdmi(television)

    def plug_in_power(self):
        self.connect_via_power_outlet(self)


class GameConsole(EntertainmentDevice, HdmiConnect, EthernetConnect, PowerOutletConnect):
    def connect_to_tv(self, television):
        self.connect_via_hdmi(television)

    def connect_to_router(self, router):
        self.connect_via_ethernet(router)

    def plug_in_power(self):
        self.connect_via_power_outlet(self)


class Router(EntertainmentDevice, EthernetConnect, PowerOutletConnect):
    def connect_to_tv(self, television):
        self.connect_via_ethernet(television)

    def connect_to_game_console(self, game_console):
        self.connect_via_ethernet(game_console)

    def plug_in_power(self):
        self.connect_via_power_outlet(self)


'''
We've been hired to create a game where the player sets up entertainment systems. 
Each piece of the system (television, game console, etc.) uses a specific cable to connect to another device. 
The TV uses an HDMI cable to connect to a game console. 
Both the game console and TV connect to a router via an ethernet cable so they can access the internet. 
And lastly, all the devices are connected to the wall via a power cable so they can turn on. 
Your job is to extend this behavior in the device classes.
'''
