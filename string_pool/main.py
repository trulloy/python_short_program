import ctypes
s = "Hello"
str = "Hello" "Hell" "world"
address = id(str)
a = ctypes.cast(address, ctypes.py_object).value
print(a)

a = "HelloWorldFllopYupoigkopHelloWorldFllopYupoigkopHelloWorldFllopYupoigkopFllopYupoigkopHelloWorldFllopYupoigkop"
b = "HelloWorldFllopYupoigkopHelloWorld""FllopYupoigkopHelloWorldFllopYupoigkop"+"FllopYupoigkopHelloWorldFllopYupoigkop"
c = "HelloWorldFllopYupoigkopHelloWorld"
print(a is b)
print(b is c)