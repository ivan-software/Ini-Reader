# 1.1

import configparser
import sys

# Vars

cfg = configparser.ConfigParser()

Link = "https://github.com/ivan-software/Ini-Reader/"

# Error Exceptions

class IniReaderError(Exception):
    None

class UnknownValueError(IniReaderError):
    def __init__(self, text):
        self.txt = text

# Main Functional

class INIReader:
    def IniRead(FILE):
        '''
        Open File.
        '''
        global cfg
        file = FILE
        cfg.read(file)
    def Read(BLOCK, VARIABLE, PRINT=1):
        '''
        Read File.
        '''
        global cfg
        block = BLOCK
        var = VARIABLE
        read = cfg[block][var]
        if PRINT == 1:
            print(read)
        elif PRINT == 0:
            read = cfg[block][var]
        else:
            raise UnknownValueError(f"Unknown Value {PRINT}; \n MAX(0-1);")
    def WriteIniFile(FILE, VARIABLE):
        '''
        Write Ini File.
        '''
        file = FILE
        var = VARIABLE
        ini = open(file, 'a')
        ini.write(var)
        ini.close()
    def CreateAndWriteIniFile(FILENAME, STRINGTOWRITE):
        '''
        Create And Write Ini File.
        '''
        fn = FILENAME
        stw = STRINGTOWRITE
        file = open(fn, "w")
        file.write(stw)
        file.close()
    def Help():
        '''
        Get Help.
        '''
        global Link
        print(
        "IniRead - Read INI \n "
      	"Read - Read And Print INI \n "
      	"If PRINT = 0 - Data Will Not Print \n "
      	"If PRINT = 1 - Data Prints \n "
        "More on " + Link
        )

# Details

#-----/*\----------/*\----------/*\-----

__package__ = "INI-Reader"
__version__ = "1.1"
__author__ = "Ivan Perzhinskiy"
__mask__ = "ini_reader"

#-----/*\----------/*\----------/*\-----
