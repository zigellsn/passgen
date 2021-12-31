# passgen
Python Password Generator

## Parameters

| Parameter        | Meaning                                            | Default value |
|------------------|----------------------------------------------------|---------------|
| -v, --version    | Shows a version message                            | n/a           |
| -c, --count      | How many passwords should be generated?            | 1             |
| -l, --length     | Number of characters in password                   | 10            |
| -o, --obligatory | Must contain at least one of each chosen category  | false         |
| --avoid-zero     | Avoid 0 and uppercase O                            | false         |
| --avoid-one      | Avoid 1, lowercase l and uppercase I               | false         |
| --ascii          | Ascii letters (upper and lower case)               | false         |
| --lowercase      | Lowercase letters                                  | true          |
| --uppercase      | Uppercase letters                                  | false         |
| --digits         | Digits                                             | true          |
| --punctuation    | Punctuation                                        | false         |
| --system         | System password conformity (SAP, ...)              | empty         |
| --custom         | File containing custom characters (UTF-8 encoding) | none          |

## System parameter

Makes the password conform to a specific system.

Supported systems: SAP (=> 'Do not start with ! or ?')