Python 3 Trillian Password Decrypting Tool
==========================================

...because you want to party like it's 2001.


## Setup

*   Have Python 3 in your path.


## Usage

Just feed in the encrypted password string from Trillian's .ini file.  Hex-as-ascii with uppercase letters.

*   Good: `./tril.py '1A2B3C'`
*   Bad:  `./tril.py '1a2b3c'`


## Notes

Later formats allegedly base64 encode the password.  If what comes out of here looks like garbage, try running it through `base64 -d`:

```bash
$ ./tril.py '1A2B3C4D' | base64 -d
omg-my-password
```

