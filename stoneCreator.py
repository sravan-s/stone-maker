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

CONSTS = __import__('constants');

class StoneCreator:
    def __init__(self, url, power = 0):
        if(len(url) >= 17):
            raise ValueError('URL length should be maximum 17 characters')
        if(power < -100 or power > 20):
            raise ValueError('Power should be greater than -100dBm and lessthan 20dBm')
        self.power = power
        self.url = url
        self.map()
        print("Sucess")

    def map(self):
        self.encoded = CONSTS.EDDYSCAFFOLD
        for index, scheme in enumerate(CONSTS.SCHEMES):
            isSchemeAvailable = False
            if(self.url.startswith(scheme)):
                isSchemeAvailable = True
                self.encoded.append(index)
                break
        if(not isSchemeAvailable):
            raise ValueError('Invalid URL protocol please use any og these \n', CONSTS.SCHEMES)
        print(self.encoded)

    def getURL(self):
        return self.url

    def getEncodedURL(self):
        return self.encoded
