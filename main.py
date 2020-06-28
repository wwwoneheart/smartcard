"""
您提供的链接有效并且APDU命令也有效，可能是您在实现中遗漏了一些信息，请注意，在继续执行任何命令之前，您首先需要使用以下命令选择卡：
FF A4 00 00 01 06
如果选择成功，则应返回90 00 。
然后您可以使用该命令从卡中读取数据
FF B0 00 XX YY
XX代表应大于32且小于256的位置
YY表示要读取的数据的长度，并且应该返回数据，如果读取过程成功，则返回90 00 。

要将数据写入卡，您需要提交密码，通过使用此命令，默认密码为FF FF FF
 FF 20 00 00 03因此用于提交密码的命令将为FF 20 00 00 03 FF FF FF
然后您可以使用以下命令写入数据：
FF D0 00 XX YY data
其中XX是您要在其中写入数据的卡中地址的位置，而YY是数据的长度，而data是要写入的数据

您可以按照需要使用文档中的其他命令

注意 ：所有代码命令均应为Hex格式，数据，存储位置..etc
"""

from blockchain.System import readers

# define the APDUs used in this script
Select = [ 0xFF, 0xA4, 0x00, 0x00, 0x01, 0x06 ]
Read = [ 0xFF, 0xB0, 0x00, 0x00, 0x09 ]
SubmitPassword = [ 0xFF, 0x20, 0x00, 0x00, 0x03, 0xFF, 0xFF, 0xFF ]
Write = [ 0XFF, 0XD0, 0x00, 0x00, 0x09, 0xA7, 0x02, 0xA7, 0x02, 0xA7, 0x02, 0xA7, 0x02, 0xA7 ]

# get all the available readers
r = readers()
print("Available readers:", r)

reader = r[0]
print("Using:", reader)

connection = reader.createConnection()
connection.connect()

data, sw1, sw2 = connection.transmit(Select)
print("Select Applet: %02X %02X" % (sw1, sw2))

data, sw1, sw2 = connection.transmit(Read)
print(f"Read Data: {data}")

# data, sw1, sw2 = connection.transmit(SubmitPassword)
# print("Submit Password: %02X %02X" % (sw1, sw2))

# data, sw1, sw2 = connection.transmit(Write)
# print("Write Data: %02X %02X" % (sw1, sw2))