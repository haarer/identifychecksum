#
#identifychecksum.py
#
# Usage: 
#   identifychecksum.py <filename> <known checksum>
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
import crccheck,sys

if len(sys.argv) != 3:
  print ("need file and checksum as arguments")
  sys.exit(-1)

sumresults={}
with open(sys.argv[1], 'rb') as fh, mmap(fh.fileno(), 0, access=ACCESS_READ) as mm:
  for clsname in dir(crccheck.crc):
    try:
      cc = getattr(crccheck.crc,clsname) 
      res = cc.calc((b[0] for b in mm))
      if res in sumresults:
        sumresults[res].add(clsname)
      else:
        sumresults[res]=[clsname]
      print("crc: {0}  = {1:x}".format(clsname,res) )
    except:
      pass

  for clsname in dir(crccheck.checksum):
    try:
      cc = getattr(crccheck.checksum,clsname) 
      res = cc.calc((b[0] for b in mm))
      if res in sumresults:
        sumresults[res].add(clsname)
      else:
        sumresults[res]=[clsname]
      print("crc: {0}  = {1:x}".format(clsname,res) )
    except:
      pass

#print(sumresults)
checksumtoidentify= int(sys.argv[2],16)
#print(sumresults[checksumtoidentify])
try:
  print("{0:x} is a {1}".format(checksumtoidentify,sumresults[checksumtoidentify]))
except: 
  print("checksum {0:x} not identified".format(checksumtoidentify))

