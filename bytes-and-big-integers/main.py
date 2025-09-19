from Crypto.Util.number import *

message = "HELLO"
message_bytes = message.encode()
message_int = bytes_to_long(message_bytes)
print("Message as integer:", message_int)

recovered_bytes = long_to_bytes(11515195063862318899931685488813747395775516287289682636499965282714637259206269)
recovered_message = recovered_bytes.decode()
print("Recovered message:", recovered_message)