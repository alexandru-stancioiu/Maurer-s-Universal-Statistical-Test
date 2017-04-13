# Maurer's Universal Statistical Test
By Alexandru Stancioiu and Erlich Sebastian

## Description

In cryptography, a pseudorandom generator (PRG) for a class of statistical tests is a deterministic procedure
that maps a random seed to a longer pseudorandom string such that no statistical test in the class can distinguish
between the output of the generator and the uniform distribution. The random seed is typically a short binary string
drawn from the uniform distribution.

We say a PRG is cryptographically secure if there is no "efficient" statistical test that can distinguish its output
from a true random generator.

## Running

The algorithm requires a file containing a hex string at least 50KB.

By running:

```
python maurer.py <file>
```

you will find out if the sequence seems random or not !

## Testing

RC4 algorithm was the most widely used stream cipher, being implemented in SSL and WEP. It used to be considered for
a very long period of time a secure PRG. Our implementation makes no exception and thinks it is secure (outputs "sequence
is random").

Very obvious non-random sequences like "000...." or "abcdefabcdefabcdef" turn out to be non-random.

## The challenge

Tests like Maurer's are being widely abused to judge positively the security of ciphers and
random number generators, probably leading to many security flaws which may go undetected until they are
widely deployed.

You have to find an "unsecure" PRG that can prove the Maurer's Universal Test is flawed and it should not be
used to judge the security of a PRG.
To do this, you must correctly implement the PRG, output a hex string of at least 50KB (you can use a short key) and,
then, feed it to maurer.py.

The output should be that "Sequence is random".

## References

[1] Ueli M. Maurer, Maurer's Universal Statistical Test for Random Bit Generators, 1992
ftp://ftp.inf.ethz.ch/pub/crypto/publications/Maurer92a.pdf

[2] Andrew Rukhin, Juan Soto, James Nechvatal, Miles Smid, Elaine Barker, Stefan Leigh, Mark Levenson,
Mark Vangel, David Banks, Alan Heckert, James Dray, San Vo, A Statistical Test Suite for Random and
Pseudorandom Number Generators for Cryptographic Applications, NIST, 2010
http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-22r1a.pdf
