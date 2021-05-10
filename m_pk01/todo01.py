from enum import Enum, unique
import pdb
import logging

logging.basicConfig(level=logging.CRITICAL)
logging.debug("---debug---")
logging.info("---info---")
logging.warning("---warning---")
logging.error("---error---")
logging.critical("---critical---")

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


@unique
class WeekDay(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


# pdb.set_trace()  # 可以用命令p查看变量，或者用命令c继续运行
print(WeekDay(0))
