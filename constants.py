SCHEMES = [
    "http://www.",
    "https://www.",
    "http://",
    "https://"
]

EXPANSIONS = [
    ".com/",
    ".org/",
    ".edu/",
    ".net/",
    ".info/",
    ".biz/",
    ".gov/",
    ".com",
    ".org",
    ".edu",
    ".net",
    ".info",
    ".biz",
    ".gov"
]

EDDYSCAFFOLD = [
    0x03,   #Length of Service List
    0x03,   #Param: Service List
    0xAA,   #Eddystone ID part-1
    0xFE,   #Eddystone ID part-2
    0,      #DUMMY: Length of Service Data
    0x16,   #Service Data
    0xAA,   #Eddystone ID part-1
    0xFE,   #Eddystone ID part-2
    0x10,   #Frame type: URL
    0xF8   #Power
    # https://,
    # URL
]
