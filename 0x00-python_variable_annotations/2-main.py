#!/usr/bin/env python3

import math

floor = __import__('2-floor').floor

ans=floor(3.14)
print(ans == math.floor(3.14))
print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))
