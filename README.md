# davy-jones
Python object for controlling Insight DeepSee Lasers. The `DeepSee` class is a
wrapper around the serial interface to the laser providing convenient methods
in place of unwieldy serial commands.


## Installation
Clone this repository and then move into the top level directory. Then

`pip install .`


## Table of serial commands

| Serial command | `davy_jones.DeepSee` method|
|----------------|----------------------------|
| ON | `power_on` |
| OFF | `NotImplemented`|
| IRSHUTter | `open_stokes_shutter`/`close_stokes_shutter`|
| IRSHUTter? | `NotImplemented`|
| LCD:BRIGtness | `NotImplemented`|
| MODE RUN | `NotImplemented`|
| MODE ALIGN | `NotImplemented`|
| MODE? | `NotImplemented`|
| READ:AHIStory? | `NotImplemented`|
| READ:HUM? | `NotImplemented`|
| READ:PCTWarmedup? | `NotImplemented`|
| READ:PLASer:DIODe(n):CURRent? | `NotImplemented`|
| READ:PLASer:DIODe(n):TEMPerature? | `NotImplemented`|
| READ:PLASer:DIODe(n):HOURS | `NotImplemented`|
| READ:POWer? |`NotImplemented`|
| READ:WAVelength? |`NotImplemented`|
| SAVe |`NotImplemented`|
| SHUTDOWN | `NotImplemented`|
| SHUTter (n) | `open_pump_shutter`/`close_pump_shutter` |
| SHUTter? | `NotImplemented`|
| TIMer:WATChdog (n) | `NotImplemented`|
| WAVelength (nnn) | `set_wavelength` |
| WAVelength? | `NotImplemented`|
| WAVelength:min? | `min_wavelength` (attribute) |
| WAVelength:max? | `max_wavelength` (attribute) |
| \*IDN? | `NotImplemented`|
| \*STB? | `get_status` |
