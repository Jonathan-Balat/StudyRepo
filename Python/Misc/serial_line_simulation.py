import random
from enum import Enum


class SerialLine:

    def __init__(self):
        self.serial_lines = {'data': 0, 'clock': 0}

    def get_serial_lines(self):
        return self.serial_lines

    def clock_tick(self):
        self.serial_lines['clock'] ^= 1


class Host:

    class DataWidth(int, Enum):
        BYTE = 8
        HALF_WORD = 16
        WORD = 32

    def __init__(self, host_name: str, n_bits: DataWidth, serial_line: dict):
        # Init serial lines, this is fixed to mimic a physical line
        self.serial_line = serial_line

        self.name = host_name
        self.data_buffer = self.generate_data(n_bits)

    @staticmethod
    def generate_data(num_bits):
        return [random.randint(0, 1) for _ in range(num_bits)]

    def __send_bit(self):
        self.serial_line['data'] = self.data_buffer.pop(0)

    def __generate_clock_tick(self):
        self.serial_line['clock'] ^= 1

    def transmit(self):
        self.__generate_clock_tick()
        self.__send_bit()

    def is_transmit_done(self):
        return len(self.data_buffer) == 0


class Device:

    class ClockPolarity(Enum):
        RISING = 1
        FALLING = 0

    class DataWidth(int, Enum):
        BYTE = 8
        HALF_WORD = 16
        WORD = 32

    def __init__(self, name, polarity: ClockPolarity, data_width: DataWidth,  serial_line: dict):
        # Init serial lines, this is fixed to mimic a physical line
        self._serial_line = serial_line

        # Device-specific configurable parameters
        self.name = name
        self.clock_polarity: Device.ClockPolarity = polarity

        # Device-specific data storages
        self._data = []
        self._data_max = data_width  # bits
        self._previous_data = None
        self._previous_clock = None

        # Initial configurations
        self.configure_clock_polarity(polarity)

    def transmission_end(self):
        return self.__data_is_full()

    def __data_is_full(self):
        return len(self._data) >= self._data_max

    def __listen_clock_tick(self):
        __is_ticked = False
        tick = self._serial_line.get("clock")

        if tick != self._previous_clock or self._previous_clock is None:
            self._previous_clock = tick
            __is_ticked = True

        return __is_ticked

    def configure_clock_polarity(self, polarity: ClockPolarity):
        self.clock_polarity = polarity
        self._previous_clock = 0 if self.clock_polarity == Device.ClockPolarity.RISING else 1

    def listen(self):
        """ Listen without clock, just store data based on dataline changes.
            Its pitfall is when the dataline doesn't appear to be changing.
            Expected, this just shows how it can be done.
        """
        if self.__data_is_full():
            return

        if self._serial_line.get("data") != self._previous_data:
            data_bit = self._serial_line.get("data")
            self._data.append(data_bit)
            self._previous_data = data_bit

    def listen_with_clock(self):
        """ Listen with clock, store data based on clock ticks.
            This is how a real device would work when reading serial data.
            Highlights the importance of using clock line for synchronization and data sampling.
        """
        if not self.__data_is_full():
            return

        if self.__listen_clock_tick():
            self._data.append(self._serial_line.get("data"))

    def get_data(self):
        # Pad data to 8 bits if less than 8 bits received, to simulate not enough clocks were received

        if len(self._data) < self._data_max:
            # Insert ahead of current data (LSB-received bit) -- This feels wrong.
            # self._data = [0]*(8-len(self._data)) + self._data

            # Append after current data (MSB-received bit)
            self._data = self._data + [0]*(self._data_max-len(self._data))

        return self._data

    def get_data_hex(self):
        byte = "0b"+"".join([str(x) for x in self.get_data()])
        return f"{self.name} data: 0x{int(byte, 2):02X}"


if __name__ == '__main__':

    # Simulates the two-wire serial lines
    serialLine = SerialLine()

    # Setup host and devices
    host = Host('Master Device', Device.DataWidth.WORD, serialLine.get_serial_lines())
    devA = Device('Device A', Device.ClockPolarity.RISING, Device.DataWidth.WORD, serialLine.get_serial_lines())
    devB = Device('Device B', Device.ClockPolarity.FALLING, Device.DataWidth.WORD, serialLine.get_serial_lines())

    while not host.is_transmit_done():
        host.transmit()
        devA.listen_with_clock()
        devB.listen_with_clock()

    print(devA.get_data_hex())
    print(devA.get_data())
    print()
    print(devB.get_data_hex())
    print(devB.get_data())
