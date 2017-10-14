sudo apt-get install ipython
ipython
from pymodbus.client.sync import modbusSerialClient
koyo =  ModbusSerialClient(method='rtu', port = '/dev/ttyAMA0', baudrate = 9600, parity='0')

koyo.read_coils(address, 1,unit = 1).bits # returns the status of coils in bool
koyo.write_coils(address, 1,unit=1) # to activate coil of PLC
