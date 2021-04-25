WIDTH = 26
HEIGHT = 26
FIRST = 0x20
LAST = 0x7f

_font =\
b'\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a'\
b'\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a'\
b'\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a'\
b'\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a'\
b'\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a'\
b'\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a'\
b'\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a\x11\x4b\x59\x51\x4b\x4e'\
b'\x4c\x4c\x4e\x4b\x51\x4b\x53\x4c\x56\x4e\x58\x51\x59\x53\x59'\
b'\x56\x58\x58\x56\x59\x53\x59\x51\x58\x4e\x56\x4c\x53\x4b\x51'\
b'\x4b\x05\x4c\x58\x4c\x4c\x4c\x58\x58\x58\x58\x4c\x4c\x4c\x04'\
b'\x4b\x59\x52\x4a\x4b\x56\x59\x56\x52\x4a\x05\x4c\x58\x52\x48'\
b'\x4c\x52\x52\x5c\x58\x52\x52\x48\x0b\x4a\x5a\x52\x49\x50\x4f'\
b'\x4a\x4f\x4f\x53\x4d\x59\x52\x55\x57\x59\x55\x53\x5a\x4f\x54'\
b'\x4f\x52\x49\x0d\x4c\x58\x50\x4c\x50\x50\x4c\x50\x4c\x54\x50'\
b'\x54\x50\x58\x54\x58\x54\x54\x58\x54\x58\x50\x54\x50\x54\x4c'\
b'\x50\x4c\x05\x4b\x59\x52\x4b\x52\x59\x20\x52\x4b\x52\x59\x52'\
b'\x05\x4d\x57\x4d\x4d\x57\x57\x20\x52\x57\x4d\x4d\x57\x08\x4d'\
b'\x57\x52\x4c\x52\x58\x20\x52\x4d\x4f\x57\x55\x20\x52\x57\x4f'\
b'\x4d\x55\x22\x4e\x56\x51\x4e\x4f\x4f\x4e\x51\x4e\x53\x4f\x55'\
b'\x51\x56\x53\x56\x55\x55\x56\x53\x56\x51\x55\x4f\x53\x4e\x51'\
b'\x4e\x20\x52\x4f\x51\x4f\x53\x20\x52\x50\x50\x50\x54\x20\x52'\
b'\x51\x4f\x51\x55\x20\x52\x52\x4f\x52\x55\x20\x52\x53\x4f\x53'\
b'\x55\x20\x52\x54\x50\x54\x54\x20\x52\x55\x51\x55\x53\x1a\x4e'\
b'\x56\x4e\x4e\x4e\x56\x56\x56\x56\x4e\x4e\x4e\x20\x52\x4f\x4f'\
b'\x4f\x55\x20\x52\x50\x4f\x50\x55\x20\x52\x51\x4f\x51\x55\x20'\
b'\x52\x52\x4f\x52\x55\x20\x52\x53\x4f\x53\x55\x20\x52\x54\x4f'\
b'\x54\x55\x20\x52\x55\x4f\x55\x55\x10\x4d\x57\x52\x4c\x4d\x55'\
b'\x57\x55\x52\x4c\x20\x52\x52\x4f\x4f\x54\x20\x52\x52\x4f\x55'\
b'\x54\x20\x52\x52\x52\x51\x54\x20\x52\x52\x52\x53\x54\x10\x4c'\
b'\x55\x4c\x52\x55\x57\x55\x4d\x4c\x52\x20\x52\x4f\x52\x54\x55'\
b'\x20\x52\x4f\x52\x54\x4f\x20\x52\x52\x52\x54\x53\x20\x52\x52'\
b'\x52\x54\x51\x10\x4d\x57\x52\x58\x57\x4f\x4d\x4f\x52\x58\x20'\
b'\x52\x52\x55\x55\x50\x20\x52\x52\x55\x4f\x50\x20\x52\x52\x52'\
b'\x53\x50\x20\x52\x52\x52\x51\x50\x10\x4f\x58\x58\x52\x4f\x4d'\
b'\x4f\x57\x58\x52\x20\x52\x55\x52\x50\x4f\x20\x52\x55\x52\x50'\
b'\x55\x20\x52\x52\x52\x50\x51\x20\x52\x52\x52\x50\x53\x08\x44'\
b'\x60\x44\x52\x60\x52\x20\x52\x44\x52\x52\x62\x20\x52\x60\x52'\
b'\x52\x62\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a\x00'\
b'\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a\x00'\
b'\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a\x00'\
b'\x4a\x5a\x00\x4a\x5a\x11\x4b\x59\x51\x4b\x4e\x4c\x4c\x4e\x4b'\
b'\x51\x4b\x53\x4c\x56\x4e\x58\x51\x59\x53\x59\x56\x58\x58\x56'\
b'\x59\x53\x59\x51\x58\x4e\x56\x4c\x53\x4b\x51\x4b\x05\x4c\x58'\
b'\x4c\x4c\x4c\x58\x58\x58\x58\x4c\x4c\x4c\x04\x4b\x59\x52\x4a'\
b'\x4b\x56\x59\x56\x52\x4a\x05\x4c\x58\x52\x48\x4c\x52\x52\x5c'\
b'\x58\x52\x52\x48\x0b\x4a\x5a\x52\x49\x50\x4f\x4a\x4f\x4f\x53'\
b'\x4d\x59\x52\x55\x57\x59\x55\x53\x5a\x4f\x54\x4f\x52\x49\x0d'\
b'\x4c\x58\x50\x4c\x50\x50\x4c\x50\x4c\x54\x50\x54\x50\x58\x54'\
b'\x58\x54\x54\x58\x54\x58\x50\x54\x50\x54\x4c\x50\x4c\x05\x4b'\
b'\x59\x52\x4b\x52\x59\x20\x52\x4b\x52\x59\x52\x05\x4d\x57\x4d'\
b'\x4d\x57\x57\x20\x52\x57\x4d\x4d\x57\x08\x4d\x57\x52\x4c\x52'\
b'\x58\x20\x52\x4d\x4f\x57\x55\x20\x52\x57\x4f\x4d\x55\x22\x4e'\
b'\x56\x51\x4e\x4f\x4f\x4e\x51\x4e\x53\x4f\x55\x51\x56\x53\x56'\
b'\x55\x55\x56\x53\x56\x51\x55\x4f\x53\x4e\x51\x4e\x20\x52\x4f'\
b'\x51\x4f\x53\x20\x52\x50\x50\x50\x54\x20\x52\x51\x4f\x51\x55'\
b'\x20\x52\x52\x4f\x52\x55\x20\x52\x53\x4f\x53\x55\x20\x52\x54'\
b'\x50\x54\x54\x20\x52\x55\x51\x55\x53\x1a\x4e\x56\x4e\x4e\x4e'\
b'\x56\x56\x56\x56\x4e\x4e\x4e\x20\x52\x4f\x4f\x4f\x55\x20\x52'\
b'\x50\x4f\x50\x55\x20\x52\x51\x4f\x51\x55\x20\x52\x52\x4f\x52'\
b'\x55\x20\x52\x53\x4f\x53\x55\x20\x52\x54\x4f\x54\x55\x20\x52'\
b'\x55\x4f\x55\x55\x10\x4d\x57\x52\x4c\x4d\x55\x57\x55\x52\x4c'\
b'\x20\x52\x52\x4f\x4f\x54\x20\x52\x52\x4f\x55\x54\x20\x52\x52'\
b'\x52\x51\x54\x20\x52\x52\x52\x53\x54\x10\x4c\x55\x4c\x52\x55'\
b'\x57\x55\x4d\x4c\x52\x20\x52\x4f\x52\x54\x55\x20\x52\x4f\x52'\
b'\x54\x4f\x20\x52\x52\x52\x54\x53\x20\x52\x52\x52\x54\x51\x10'\
b'\x4d\x57\x52\x58\x57\x4f\x4d\x4f\x52\x58\x20\x52\x52\x55\x55'\
b'\x50\x20\x52\x52\x55\x4f\x50\x20\x52\x52\x52\x53\x50\x20\x52'\
b'\x52\x52\x51\x50\x10\x4f\x58\x58\x52\x4f\x4d\x4f\x57\x58\x52'\
b'\x20\x52\x55\x52\x50\x4f\x20\x52\x55\x52\x50\x55\x20\x52\x52'\
b'\x52\x50\x51\x20\x52\x52\x52\x50\x53\x08\x44\x60\x44\x52\x60'\
b'\x52\x20\x52\x44\x52\x52\x62\x20\x52\x60\x52\x52\x62\x00\x4a'\
b'\x5a\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a\x00\x4a'\
b'\x5a\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a\x00\x4a'\
b'\x5a\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a\x00\x4a\x5a\x00\x4a'\
b'\x5a'

_index =\
b'\x00\x00\x03\x00\x06\x00\x09\x00\x0c\x00\x0f\x00\x12\x00\x15'\
b'\x00\x18\x00\x1b\x00\x1e\x00\x21\x00\x24\x00\x27\x00\x2a\x00'\
b'\x2d\x00\x30\x00\x33\x00\x36\x00\x39\x00\x3c\x00\x3f\x00\x42'\
b'\x00\x45\x00\x48\x00\x4b\x00\x4e\x00\x51\x00\x54\x00\x57\x00'\
b'\x5a\x00\x5d\x00\x60\x00\x63\x00\x88\x00\x95\x00\xa0\x00\xad'\
b'\x00\xc6\x00\xe3\x00\xf0\x00\xfd\x00\x10\x01\x57\x01\x8e\x01'\
b'\xb1\x01\xd4\x01\xf7\x01\x1a\x02\x2d\x02\x30\x02\x33\x02\x36'\
b'\x02\x39\x02\x3c\x02\x3f\x02\x42\x02\x45\x02\x48\x02\x4b\x02'\
b'\x4e\x02\x51\x02\x54\x02\x57\x02\x5a\x02\x5d\x02\x82\x02\x8f'\
b'\x02\x9a\x02\xa7\x02\xc0\x02\xdd\x02\xea\x02\xf7\x02\x0a\x03'\
b'\x51\x03\x88\x03\xab\x03\xce\x03\xf1\x03\x14\x04\x27\x04\x2a'\
b'\x04\x2d\x04\x30\x04\x33\x04\x36\x04\x39\x04\x3c\x04\x3f\x04'\
b'\x42\x04\x45\x04\x48\x04\x4b\x04\x4e\x04\x51\x04\x54\x04'

INDEX = memoryview(_index)
FONT = memoryview(_font)
