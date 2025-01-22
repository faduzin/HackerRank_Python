regex_pattern = r",|\."

import re

if __name__ == '__main__':
    print("\n".join(re.split(regex_pattern, input())))
