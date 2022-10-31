import submodulos as sb
from datetime import datetime
import sys
dt = datetime.now()
ts = int(datetime.timestamp(dt))
# getting the timestamp

if __name__ == '__main__':

    print(sb.GetHashLevel2(sys.argv[1]))
