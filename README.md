# Free Speech (John Marcotte) Flag generator

This Python script generates a [free speech flag](https://en.wikipedia.org/wiki/Free_Speech_Flag) from a Kryptor public key file.

A free speech flag is a protest symbol against censorship. The original flag was created from converting a cryptographic key used in protected physical media into hexidecimal and splitting them into hex triplet web colors. The key was the subject of a [dispute where any web page mentioning or hyperlinking to it was subject to cease and desist letters by the NCAA and AACS](https://en.wikipedia.org/wiki/AACS_encryption_key_controversy).

This flag creates a 11-color flag (1100x550) and adds the remaining four characters on the bottom right of the flag, in spirit of the original.

Feel free to place your key and corresponding key flag on your web site.

## Examples
| Flag  | Public key |
| ------------- | ------------- |
| ![](https://github.com/final-git/marcottegen/blob/main/flagexample.png?raw=true)  | `Ed//0Dc41jis8/HAWQJ2j7+zP3ZKPRK4xNUpKdfGCEHD42E=` (`11DFFF D03738 D638AC F3F1C0 590276 8FBFB3 3F764A 3D12B8 C4D529 29D7C6 0841C3 E3 61`)  |

*Real examples are double the resolution*

## Requirements
- Python
- Pillow (PIL, Python Imaging Library)

The default setting uses the 'Arial' font, Windows and some major Linux distributions bundle this font. You may change the font by replacing `Arial.ttf`. 

Install Pillow with:
```
pip install pillow
```

## Usage
```
python marcottegen.py <Kryptor public key file>
```

## Output
- The generated flag image is saved as `flag.png` in the current directory.

## TODO

- Use black text over light colors
- User-facing customisation arguments
- Support other public key formats (age? pgp?)

## License
Like the original work, this code is in the public domain. Pull requests not in the public domain will be rejected.
