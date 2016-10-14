#!/usr/bin/env python

# Copyright 2016 Simon Zigelli
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import string
from random import choice
import sys

print('Password generator')
print('Copyright (c) 2016 Zigelli ENTERPRISES. All rights reserved.')
print('\n')
if len(sys.argv) > 1:
    size = sys.argv[1]
else:
    size = 8
    count = 1
if len(sys.argv) > 2:
    count = sys.argv[2]
else:
    count = 1
try:
    num = int(size)
    k = int(count) 
    for i in range(k):
        passwort = ''.join([choice(string.ascii_lowercase + string.digits) for i in range(num)])
        print (passwort)
except:
    print("Fehlerhafte Eingabe.")
    print("Verwendung: 'python passgen.py <Laenge> <Anzahl>'") 
