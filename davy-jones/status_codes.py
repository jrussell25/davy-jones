# Helpers for decoding DeepSee status codes

def to_bits(status):
    """
    Convert the result from *STB? which is an int like string to bits
    """
    return f"{int(status):032b}"

def state_number(bits):
    return int(bits[16:23],2)

def state_defs(x):
    if x<0 or x>127:
        raise ValueError("Invalide State Code")
    elif x<25:
        return "Initializing"
    elif x==25:
        return "Ready"
    elif 25<x<50:
        return "Optimizing"
    elif x==50:
        return "Running"
    elif 50<x<60:
        return "Moving to align mode"
    elif x==60:
        return "Align mode"
    elif 60<x<70:
        return "Exiting align mode"
    else:
        return "Reserved state"


INTERPRETATION = ['Emission', 'Pulsing', 'Main Shutter', 'IR Shutter',
                  'Reserved', 'Servo On', 'Reserved', 'Reserved',
                  'Reserved', 'User Interlock', 'Keyswitch', 'Power Supply',
                  'Internal', 'Reserved', 'Warning', 'Fault']

DESCRIPTIONS = [['Diodes are not energized', 'Diodes are energized'],
                ['Laser is not running', 'Laser is in RUN/ALIGN mode'],
                ['Main shutter is closed', 'Main shutter is open'],
                ['IR shutter is closed', 'IR shutter is open'],
                ['',''],
                ['Servo is off', 'Servo is on'],
                ['',''], ['',''], ['',''],
                ['Interlock closed', 'Interlock open - laser is forced off'],
                ['Interlock closed', 'Interlock open - laser is forced off'],
                ['Interlock closed', 'Interlock open - laser is forced off'],
                ['Interlock closed', 'Interlock open - laser is forced off'],
                ['',''], 
                ['No warnings', 'Warning detected -- use read_history to investigate'],
                ['No faults', 'Fault detected. Laser will not run. Use read_history to investigate']]


def print_state(status):
    status_bits = to_bits(status)
    description_bits = status_bits[:16]
    state = state_number(status_bits)
    print("BIT Interpretation Description") 
    for i, interp in enumerate(INTERPRETATION):
        bit = int(description_bits[i])
        print(f"{i:3d} {interp:14s} {DESCRIPTIONS[i][bit]}")

    print()
    print(f'Status Code {state:3d} -- {state_defs(state)}')
