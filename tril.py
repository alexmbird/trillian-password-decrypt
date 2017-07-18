#!/usr/bin/env python3


"""Decrypt a stored password from a .ini file created by ancient versions of
the Trillian IM client.  

Algorithm from http://securityxploded.com/trillianpasswordsecrets.php"""

import sys


MAGIC_BYTES = [ 243, 38, 129, 196, 57, 134, 219, 146, 113, 163, 185, 230, 83, 122, 149, 124, 0, 0, 0, 0, 0, 0, 255, 0, 0, 128, 0, 0, 0, 128, 128, 0, 255, 0, 0, 0, 128, 0, 128, 0, 128, 128, 0, 0, 0, 128, 255, 0, 128, 0, 255, 0, 128, 128, 128, 0, 85, 110, 97, 98, 108, 101, 32, 116, 111, 32, 114, 101, 115, 111, 108, 118, 101, 32, 72, 84, 84, 80, 32, 112, 114, 111, 120, 0 ] 

ALLOWED_HEX_CHARS = bytearray('0123456789ABCDEF', 'ascii')


def decrypt(enc_pass):
    """Decrypt a Trillian password...
    
    Args:
        enc_pass:  bytearray object containing the encrypted pass
    
    Returns:
        bytearray object containing the decrypted pass
    
    Raises:
        TypeError  - supplied pass was not a bytes object
        ValueError - supplied pass had an odd number of bytes or isn't hex
    """
    if not isinstance(enc_pass, bytearray):
        raise TypeError("enc_pass needs to be a bytearray object")
    if len(enc_pass) % 2 != 0:
        raise ValueError("enc_pass needs even number of characters")
    for char in enc_pass:
        if char not in ALLOWED_HEX_CHARS:
            raise ValueError("enc_pass must only contain %s" % (ALLOWED_HEX_CHARS.decode('ascii'),))
    
    # Will store finished password
    dec_pass = bytearray()

    for i in range(0, int(len(enc_pass)/2)):
        # Handle first byte of enc data
        a = enc_pass[2*i]
        if ord('0') <= a <= ord('9'):
            c = a - ord('0')
        else:
            c = 0xA + (a - ord('A'))
        
        # Handle second byte of enc data
        a = enc_pass[2*i+1]
        if ord('0') <= a <= ord('9'):
            a = a - ord('0')
        else:
            a = 0xA + (a - ord('A'))
        
        c = (c << 4) + a
        dec_pass.append(c ^ MAGIC_BYTES[i])

    return dec_pass


if __name__ == '__main__':
    if len(sys.argv) == 2:
        decr_pass = decrypt(bytearray(sys.argv[1], 'ascii'))
        print(decr_pass.decode('ascii'))
    else:
        print("Usage: %s <encrypted_trillian_pass>")




