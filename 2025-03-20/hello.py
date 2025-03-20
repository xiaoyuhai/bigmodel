import keyword
from decimal import Decimal

print("hello world")

# 单行注释
"""this is a many text zhushi"""

print("""this is a many text""")

var1 = 1
var2 = 3

result = var1 + var2
print("var1+var2 = ", result)

name = "张三"
age = 18
weight = 1000.3

var1 = var2 = var3 = 10

print("var1 var2 var3", var1, var2, var3)

print(keyword)

# 二进制 0b 或者0B
# 八进制 0o

# 十六进制 0x 0X

# 原码
# 1）正数：二进制数。  负数：绝对值对应的二进制数，最左边变为1 0的原码 仍然是0
# 反码  正数反码：和原码一样 负数反码 原码基础上，符号位不变，其余位取反。0仍然是0

f1 = True
f2 = False
print(f1, f2)

num1 = 0.1
num2 = 0.2
print("num1+num2", num1 + num2)

num3 = Decimal('1.0')
num4 = Decimal('0.9')

print(num3 + num4)

# 字符串
str1 = "this is a 'String'"
str2 = "thhis is  a 'String' to"
print(str1)
print(str2)

str3 = """this is three string
can many row!"""
print(str3)

# 相同的字符串，只创建一份，如果内存里面有这个值就不在创建

# 数据类型转换，饮食转换，小整形会自动大整形

num_str = "123.3"

print("num_str", Decimal(num_str))

num_str1 = "134"
print("num_str1", int(num_str1))

str1 = "你好中国"
print(type(str1))

byte1 = str1.encode(encoding='utf8')
print(byte1, "typ3={}", type(byte1))
string2 = byte1.decode(encoding="utf8")
print(str2, "str2 type", type(string2))

# iput_str = input("请输入：")
# print("input str：", type(iput_str))

# 格式化输出

int1 = 10
float1 = 3.1415

# 格式化输出
# 1） 字符串中使用%占位
str1 = "int1 = %d,float1=%f" % (int1, float1)

print(str1)

# 2）字符串.format
str2 = "int1={},flouat1={},bool1={}".format(int1, float1, f1)
print("格式化后字符串 str2", str2)
a1 = 100
f1 = 100.01

b1 = True
str2 = "int1 = {a1}, float1={f1},boool1={b1}".format(a1=a1, f1=f1, b1=b1)
print("指定变量格式化，str2", str2)
