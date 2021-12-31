#!/usr/bin/env python

# Copyright 2016-2022 Simon Zigelli
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

import argparse
import string
from random import choice


def _contains_any(contains_string, contains_set):
    return 1 in [c in contains_string for c in contains_set]


def _passgen(password_length, count, ascii_letters, lowercase, uppercase, digits, punctuation, sap, obligatory,
             avoid_zero, avoid_one, custom_chars_file):
    custom_chars = None
    if custom_chars_file is not None:
        custom_chars = custom_chars_file.read()
        characters = custom_chars
    else:
        characters = ""
    if ascii_letters:
        characters += string.ascii_letters
    else:
        if lowercase:
            characters += string.ascii_lowercase
        if uppercase:
            characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if punctuation:
        characters += string.punctuation

    std_password = False
    if not ascii_letters and not lowercase and not uppercase and not digits and not punctuation and custom_chars == "":
        characters = string.ascii_lowercase + string.digits
        std_password = True

    if avoid_zero:
        characters = characters.replace("0", "")
        characters = characters.replace("O", "")

    if avoid_one:
        characters = characters.replace("1", "")
        characters = characters.replace("l", "")
        characters = characters.replace("I", "")

    if len(characters) == 0:
        print("No characters for password left.")
        exit()

    i = 0
    while i < count:
        passwort = ''.join([choice(characters) for i in range(password_length)])
        if sap and (passwort[0] == "!" or passwort[0] == "?"):
            continue
        if obligatory:
            if std_password:
                if _contains_any(passwort, string.ascii_lowercase) and _contains_any(passwort, string.digits):
                    print(passwort)
                    i += 1
                    continue
            else:
                if custom_chars is not None and not _contains_any(passwort, custom_chars):
                    continue
                if ascii_letters and not _contains_any(passwort, string.ascii_letters):
                    continue
                if lowercase and not _contains_any(passwort, string.ascii_lowercase):
                    continue
                if uppercase and not _contains_any(passwort, string.ascii_uppercase):
                    continue
                if digits and not _contains_any(passwort, string.digits):
                    continue
                if punctuation and not _contains_any(passwort, string.punctuation):
                    continue
                print(passwort)
                i += 1
        else:
            print(passwort)
            i += 1


if __name__ == '__main__':
    # initiate the parser
    parser = argparse.ArgumentParser(prog='Password Generator')
    parser.add_argument("-v", "--version", help="Show version", action="version",
                        version="%(prog)s 2.0.0 - Copyright (c) 2016-2022 Zigelli ENTERPRISES. All rights reserved.")
    parser.add_argument("-c", "--count", type=int, help="Password count", default=1)
    parser.add_argument("-l", "--length", type=int, help="Password length", default=10)
    parser.add_argument("-o", "--obligatory", help="Must contain at least one of each chosen category",
                        action=argparse.BooleanOptionalAction)
    parser.add_argument("--avoid-zero", help="Avoid 0 and uppercase O", action=argparse.BooleanOptionalAction)
    parser.add_argument("--avoid-one", help="Avoid 1, lowercase l and uppercase I",
                        action=argparse.BooleanOptionalAction)
    parser.add_argument("--ascii", help="Ascii letters (uppercase and lowercase)",
                        action=argparse.BooleanOptionalAction)
    parser.add_argument("--lowercase", help="Lowercase", action=argparse.BooleanOptionalAction)
    parser.add_argument("--uppercase", help="Uppercase", action=argparse.BooleanOptionalAction)
    parser.add_argument("--digits", help="Digits", action=argparse.BooleanOptionalAction)
    parser.add_argument("--punctuation", help="Punctuation", action=argparse.BooleanOptionalAction)
    parser.add_argument("--sap", help="SAP conform password (=> 'Do not start with ! or ?')",
                        action=argparse.BooleanOptionalAction)
    parser.add_argument("--custom", help="Custom characters file (UTF-8 encoding)",
                        type=argparse.FileType("r", encoding="UTF-8"), required=False)
    args = parser.parse_args()

    _passgen(args.length, args.count, args.ascii, args.lowercase, args.uppercase, args.digits, args.punctuation,
             args.sap, args.obligatory, args.avoid_zero, args.avoid_one, args.custom)
