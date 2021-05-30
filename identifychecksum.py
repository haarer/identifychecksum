#
#identifychecksum.py
#
# Usage: 
#   identifychecksum.py <filename> <known checksum> <checksum bit length>
#
# Description:
#   The Script computes sums of by known checksum algorithms and tries
#   to guess what algorithm was used.
#
# Dependencies:
#   python3
#   crccheck python module "pip3 install crccheck"
#
#
# copyright 2021 Alexander Haarer
# License: Apache 2.0 License
#


from mmap import ACCESS_READ, mmap
import crccheck,sys,re

print(len(sys.argv))
if len(sys.argv) < 3 or len(sys.argv) > 4:
  print ("need file, checksum and optional checksum bit length as arguments")
  sys.exit(-1)

checksumtoidentify= int(sys.argv[2],16)

if len(sys.argv) ==4:
    checksumlength= int(sys.argv[3])
else:
    checksumlength=None

sumresults={}


with open(sys.argv[1], 'rb') as fh:
  data=fh.read()
  print("file read")

#tests with binascii
  if checksumlength == 32 or checksumlength == None:
    print("testing crc32 from binasci (same as zlib)")
    import binascii
    res = binascii.crc32(data) & 0xFFFFFFFF
    clsname = "crc32"
    if res in sumresults:
        sumresults[res].extend(clsname)
    else:
        sumresults[res]=[clsname]
    print("crc: {0}  = {1:x} ({2} bit width)".format(clsname,res,32) )


# tests with crc module - has an identify but it does basically the same stuff we do


  print("testing crccheck.crc {0} bit functions".format(checksumlength))
  for cls in crccheck.crc.ALLCRCCLASSES:
    clsname = cls.__name__
    if checksumlength == None or cls._width == checksumlength:
      try:
        res = cls.calc(data)
        if res in sumresults:
          sumresults[res].extend(clsname)
        else:
          sumresults[res]=[clsname]
        print("crc: {0}  = {1:x} ({2} bit width)".format(clsname,res,cls._width) )
      except:
        pass




# tests with checksum module
  print("testing crccheck.checksum {0} bit functions".format(checksumlength))
  for cls in crccheck.checksum.ALLCHECKSUMCLASSES:
    clsname = cls.__name__
    if checksumlength == None or cls._width == checksumlength:
      try:
        res = cls.calc(data)
        if res in sumresults:
          sumresults[res].extend(clsname)
        else:
          sumresults[res]=[clsname]
        print("crc: {0}  = {1:x} ({2} bit width)".format(clsname,res,cls._width) )
      except:
        pass



#print(sumresults)

#print(sumresults[checksumtoidentify])
try:
  print("{0:x} is a {1}".format(checksumtoidentify,sumresults[checksumtoidentify]))
except: 
  print("checksum {0:x} not identified".format(checksumtoidentify))

