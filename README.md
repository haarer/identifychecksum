# identifychecksum
Tool to identify the checksum algorithm by a known checksum on an existing file
Uses hashlib and crccheck modules for algorithms (135 Algorithms)

Usage: identifychecksum.py <filename> <known checksum> <optional checksum bit length>
  
Passing a checksum bit length reduces the amount of algorithms tested. 
Sometimes a checksum is derived from an algorithms output by omitting bytes, e.g. the 
first four bytes of a SHA hash.
The tool recognizes this, if the checksum is not shifted, or shifted by a multiple of 4 bits.

  
Algorithms available:
  
    md4
    sm3
    sha1
    sha512_256
    md5
    sha256
    sha3_512
    shake_256
    blake2s
    whirlpool
    sha512_224
    mdc2
    blake2b
    md5-sha1
    ripemd160
    sha384
    sha3_224
    sha3_384
    sha3_256
    shake_128
    sha224
    sha512
    Crc3Gsm
    Crc3Rohc
    Crc4G704
    Crc4Interlaken
    Crc5EpcC1G2
    Crc5G704
    Crc5Usb
    Crc6Cdma2000A
    Crc6Cdma2000B
    Crc6Darc
    Crc6G704
    Crc6Gsm
    Crc7Mmc
    Crc7Rohc
    Crc7Umts
    Crc8Autosar
    Crc8Bluetooth
    Crc8Cdma2000
    Crc8Darc
    Crc8DvbS2
    Crc8GsmA
    Crc8GsmB
    Crc8I4321
    Crc8ICode
    Crc8Lte
    Crc8MaximDow
    Crc8MifareMad
    Crc8Nrsc5
    Crc8Opensafety
    Crc8Rohc
    Crc8SaeJ1850
    Crc8Smbus
    Crc8Tech3250
    Crc8Wcdma
    Crc10Atm
    Crc10Cdma2000
    Crc10Gsm
    Crc11Flexray
    Crc11Umts
    Crc12Cdma2000
    Crc12Dect
    Crc12Gsm
    Crc12Umts
    Crc13Bbc
    Crc14Darc
    Crc14Gsm
    Crc15Can
    Crc15Mpt1327
    Crc16Arc
    Crc16Cdma2000
    Crc16Cms
    Crc16Dds110
    Crc16DectR
    Crc16DectX
    Crc16Dnp
    Crc16En13757
    Crc16Genibus
    Crc16Gsm
    Crc16Ibm3740
    Crc16IbmSdlc
    Crc16IsoIec144433A
    Crc16Kermit
    Crc16Lj1200
    Crc16MaximDow
    Crc16Mcrf4Xx
    Crc16Modbus
    Crc16Nrsc5
    Crc16OpensafetyA
    Crc16OpensafetyB
    Crc16Profibus
    Crc16Riello
    Crc16SpiFujitsu
    Crc16T10Dif
    Crc16Teledisk
    Crc16Tms37157
    Crc16Umts
    Crc16Usb
    Crc16Xmodem
    Crc17CanFd
    Crc21CanFd
    Crc24Ble
    Crc24FlexrayA
    Crc24FlexrayB
    Crc24Interlaken
    Crc24LteA
    Crc24LteB
    Crc24Openpgp
    Crc24Os9
    Crc30Cdma
    Crc31Philips
    Crc32Aixm
    Crc32Autosar
    Crc32Base91D
    Crc32Bzip2
    Crc32CdRomEdc
    Crc32Cksum
    Crc32Iscsi
    Crc32IsoHdlc
    Crc32Jamcrc
    Crc32Mpeg2
    Crc32Xfer
    Crc40Gsm
    Crc64Ecma182
    Crc64GoIso
    Crc64We
    Crc64Xz
    Crc82Darc
    Checksum8
    Checksum16
    Checksum32
    ChecksumXor8
    ChecksumXor16
    ChecksumXor32
