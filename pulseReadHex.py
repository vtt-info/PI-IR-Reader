import machine
import utime

IR_PIN = machine.Pin(1, machine.Pin.IN)
TIMEOUT = 1000  # in milliseconds
PULSE_THRESHOLD = 1000

# Function to read the IR receiver
def read_ir_receiver():
    start_time = utime.ticks_ms()
    while IR_PIN.value() == 0:
        if utime.ticks_diff(utime.ticks_ms(), start_time) > TIMEOUT:
            return None

    pulse_start = utime.ticks_us()
    while IR_PIN.value() == 1:
        if utime.ticks_diff(utime.ticks_ms(), start_time) > TIMEOUT:
            return None

    pulse_end = utime.ticks_us()
    pulse_duration = utime.ticks_diff(pulse_end, pulse_start)

    return pulse_duration

# Main loop
while True:
    pulses = []
    while True:
        pulse = read_ir_receiver()
        if pulse is None:
            break
        pulses.append(pulse)

    if len(pulses) > 0:
        binary_signal = ''.join(["0" if pulse < PULSE_THRESHOLD else "1" for pulse in pulses])        
        print("Hex Signal: ", hex(int(binary_signal, 2)))

    utime.sleep_ms(100)