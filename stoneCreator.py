"""
Output
uint8_t advdata[] =
{
  0x03,  // Length of Service List
  0x03,  // Param: Service List
  0xAA, 0xFE,  // Eddystone ID
  0x13,  // Length of Service Data
  0x16,  // Service Data
  0xAA, 0xFE, // Eddystone ID
  0x10,  // Frame type: URL
  0xF8, // Power
  0x03, // https://
  'g',
  'o',
  'o',
  '.',
  'g',
  'l',
  '/',
  'a',
  '0',
  'm',
  'n',
  's',
  'S',
};
"""

class StoneCreator:
    def __init__(self, url):
        if(len(url) >= 17):
            raise ValueError('URL length should be maximum 17 characters')
        print("Sucess")
