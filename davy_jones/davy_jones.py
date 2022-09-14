import time
from typing import Any

import serial
from pyvisa import ResourceManager
from pyvisa.resources.serial import SerialInstrument
from serial import SerialException
from serial.tools import list_ports

from .status_codes import state_number


def port_map() -> None:
    for p in list_ports.comports():
        try:
            s_test = serial.Serial(p.name)
            s_test.close()
            print(p)
        except SerialException:
            pass


class DeepSee:
    def __init__(self, port_name: str = "ASRL4::INSTR", **kwargs: Any):
        # super().__init__(self, **kwargs)
        self.rm = ResourceManager()
        self.device = self._setup_device(port_name)

        self.min_wavelength = int(self.device.query("wav:min?"))
        self.max_wavelenth = int(self.device.query("wav:max?"))

    def _setup_device(self, port_name: str) -> SerialInstrument:
        device = ResourceManager().open_resource(port_name)
        device.baud_rate = 115200
        device.read_termination = "\n"
        device.write_termination = "\n"
        return device

    def power_on(self, blocking: bool = True, verbose: bool = False) -> None:

        status = self.get_status()

        if status != 25:
            raise ValueError(
                f"DeepSee is not ready to turn on. Found status number {status}"
            )
        self.device.write("on")

        if blocking:
            count = 0
            while True:
                time.sleep(1)
                count += 1
                status = self.get_status()
                if verbose:
                    print(f"{count} s - {status=:03d}")

                if status == 50:
                    break

    def get_status(self) -> int:
        status = self.device.query("*stb?")
        return state_number(status)

    def set_wavelength(self, wav: int) -> None:
        wav = int(wav)
        low = self.min_wavelength
        high = self.max_wavelenth

        if (self.min_wavelength > wav) or (self.max_wavelenth < wav):
            raise ValueError(f"Require {low} <= wav <= {high}. Found {wav=}.")

        self.device.write(f"wav {wav}")

    def open_pump_shutter(self):
        self.device.write("shut 1")

    def open_stokes_shutter(self):
        self.device.write("irshut 1")

    def close_pump_shutter(self):
        self.device.write("shut 0")

    def close_stokes_shutter(self):
        self.device.write("irshut 0")

    def get_shutter_state(self):
        pump = int(self.device.query("shut?"))
        stokes = int(self.device.query("irshut?"))
        states = ["OPEN", "CLOSED"]
        print(f"Pump shutter is {states[pump]} -- Stokes shutter is {states[stokes]}")
