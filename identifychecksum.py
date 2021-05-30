#
#identifychecksum.py
#
# Usage: 
#   identifychecksum.py <filename> <known checksum> <checksum bit length>
#
# Description:
#   The Script computes sums of by known checksum algorithms and tries
#   to guess what algorithm was used. It is possible to pass the length
#   of the check sum as 3rd parameter
#   It is also possible to detect, if the given checksum is a part of a larger checksum
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

if len(sys.argv) < 3 or len(sys.argv) > 4:
  print ("Error, missing file, checksum and optional checksum bit length as arguments")
  print ("Usage: identifychecksum.py <filename> <known checksum> <checksum bit length>")

  import hashlib
  print ("available algorithms from hashlib: ")
  for clsname in hashlib.algorithms_available:
    print("   ", clsname)
  import crccheck
  print ("available algorithms from crccheck.crc: ")
  for cls in crccheck.crc.ALLCRCCLASSES:
    print("   ",  cls.__name__)
  print ("available algorithms from crccheck.checksum: ")
  for cls in crccheck.checksum.ALLCHECKSUMCLASSES:
    print("   ",  cls.__name__)
  sys.exit(-1)

checksumtoidentify = sys.argv[2]

if len(sys.argv) ==4:
    checksumlength= int(sys.argv[3])
else:
    checksumlength=None

sumresults={}


with open(sys.argv[1], 'rb') as fh:
  data=fh.read()
  print("file read")


# tests with hashlib module
  print("testing hashlib {0} bit functions".format(checksumlength))
  import hashlib
  for clsname in hashlib.algorithms_available:

    #print( clsname)
    cls = hashlib.new(clsname)
    if checksumlength == None or checksumlength == cls.digest_size*8 or cls.digest_size == 0:
      #try:

        cls.update(data)
        if clsname=="shake_128":
            if checksumlength== None:
                res=cls.hexdigest(128)
            else:
                res=cls.hexdigest(int(checksumlength/8))
        elif clsname=="shake_256":
            if checksumlength== None:
                res=cls.hexdigest(256)
            else:
                res=cls.hexdigest(int(checksumlength/8))
        else:
            res=cls.hexdigest()

        if res in sumresults:
          sumresults[res].append(clsname)
        else:
          sumresults[res]=[clsname]
        print("crc: {0}  = {1} ({2} bit width)".format(clsname,res,cls.digest_size*8) )
      #except:
        pass


#tests with binascii
  if checksumlength == 32 or checksumlength == None:
    print("testing crc32 from binasci (same as zlib)")
    import binascii
    res = binascii.crc32(data) & 0xFFFFFFFF
    res = "{0:x}".format(res)
    clsname = "crc32"
    if res in sumresults:
        sumresults[res].extend(clsname)
    else:
        sumresults[res]=[clsname]
    print("crc: {0}  = {1} ({2} bit width)".format(clsname,res,32) )


# tests with crc module - has an identify but it does basically the same stuff we do


  print("testing crccheck.crc {0} bit functions".format(checksumlength))
  for cls in crccheck.crc.ALLCRCCLASSES:
    clsname = cls.__name__
    if checksumlength == None or cls._width == checksumlength:
      try:
        res = cls.calc(data)
        res = "{0:x}".format(res)
        if res in sumresults:
          sumresults[res].append(clsname)
        else:
          sumresults[res]=[clsname]
        print("crc: {0}  = {1} ({2} bit width)".format(clsname,res,cls._width) )
      except:
        pass




# tests with checksum module
  print("testing crccheck.checksum {0} bit functions".format(checksumlength))
  for cls in crccheck.checksum.ALLCHECKSUMCLASSES:
    clsname = cls.__name__
    if checksumlength == None or cls._width == checksumlength:
      try:
        res = cls.calc(data)
        res = "{0:x}".format(res)
        if res in sumresults:
          sumresults[res].append(clsname)
        else:
          sumresults[res]=[clsname]
        print("crc: {0}  = {1} ({2} bit width)".format(clsname,res,cls._width) )
      except:
        pass


#print(sumresults)

#print(sumresults[checksumtoidentify])
try:
  print("{0} exactly matches a {1}".format(checksumtoidentify,sumresults[checksumtoidentify]))
except: 
  print("checksum {0} not exactly identified".format(checksumtoidentify))
  for res in sumresults:
    if re.search(checksumtoidentify,res):
      print("checksum {0} partially matches {1} which is a {2}".format(checksumtoidentify,res,sumresults[res]))

