"""Exact local factor and integration checks, including ramification and endpoints."""
from fractions import Fraction as F


def check_prime(p, char, y, degree):
    # All ordinary prime powers through p^degree; a degree-two norm uses half as many.
    norms = [(p,2)] if char == 1 else ([(p,1)] if char == 0 else [(p*p,1)])
    kproduct = omitted = ordinary = character_value = character_tail = F(0)
    def future(start):
        return min(F(1), y/start)
    for q,mult in norms:
        for j in range(1,(degree if q == p else degree//2)+1):
            term = F(mult,j*q**j)
            kproduct += term*future(q)
            omitted += term*(future(q)-future(q**j))
    for j in range(1,degree+1):
        term = F(1,j*p**j)
        ordinary += term*future(p**j)
        character_value += char**j*term
        if j >= 2:
            character_tail += char**j*term*(1-future(p**j))
    race = (1-future(p))*F(char,p)
    assert kproduct-character_value+race == ordinary+omitted-character_tail


def main():
    if not __debug__:
        raise SystemExit("Enable Python assertions.")
    count = 0
    for p in [2,3,5,7,13,29]:
        for char in [-1,0,1]:
            for degree in [2,3,6,9]:
                for y in [F(2),F(p),F(2*p+1,2),F(p*p),F(3*p*p-1,3),F(p**4)]:
                    check_prime(p,char,y,degree)
                    count += 1
    print(f"{count} exact local checks for split, ramified and inert primes.")
    assert F(4,5) > (F(2,3)+F(1,8))**2
    assert F(1,8)-F(46192,10**6) > F(1,16)
    print("The single-frequency and signed-window margins hold in rational arithmetic.")


if __name__ == "__main__":
    main()
