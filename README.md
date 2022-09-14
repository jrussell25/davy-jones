# davy-jones
Python object for controlling Insight DeepSee Lasers. The `DeepSee` class is a
wrapper around the serial interface to the laser providing convenient methods
in place of unwieldy serial commands.


## Installation

`pip install davy-jones`


## Table of serial commands


ON
OFF
IRSHUTter
IRSHUTter?
LCD:BRIGtness
MODE RUN
MODE ALIGN
MODE?
READ:AHIStory?
READ:HUM?
READ:PCTWarmedup?
READ:PLASer:DIODe(n):CURRent?
READ:PLASer:DIODe(n):TEMPerature?
READ:PLASer:DIODe(n):HOURS
READ:POWer?
READ:WAVelength?
SAVe
SHUTDOWN
SHUTter (n)
SHUTter?
TIMer:WATChdog (n)
WAVelength (nnn)
WAVelength?
WAVelength:min?
WAVelength:max?
\*IDN?
\*STB?
