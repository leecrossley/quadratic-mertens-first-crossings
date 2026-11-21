"""Check the normalization of the two-grid transform by summing actual ordinates."""
from flint import arb, ctx


def sinc_square(z):
    return z.sinc()**2


def fejer(x, h, p, angle):
    total = arb(1)
    assert h <= 5*p
    for j in range(1,6):
        total += 2*max(0,1-j*p/h)*(j*angle).cos()*(j*p*x).cos()
    return 2*p*total/h


def check():
    p = arb(13)
    for angle in (arb(0),arb(2)/7):
        for h in (5*p,arb(33)*p/7):
            for t in (arb(0),angle/p,arb(1)/9):
                kmax = 1200
                total = arb(0)
                for k in range(-kmax,kmax+1):
                    for sign in (-1,1):
                        height = (2*arb.pi()*k+sign*angle)/p
                        total += sinc_square(h*(t-height)/2)
                # For |k|>kmax, |2 pi k +- angle - pt| >= pi |k|.
                tail = 16*p**2/(h*h*arb.pi()**2*kmax)
                polynomial = fejer(t,h,p,angle)
                assert (total+arb(0,tail)).overlaps(polynomial)
            # All coefficients are nonnegative. Test a signed vector on the full kernel.
            points = [arb(0),arb(1)/19,arb(2)/19,arb(4)/19]
            vector = (-3,8,-7,2)
            quadratic = arb(0)
            for ti,a in zip(points,vector):
                for tj,b in zip(points,vector):
                    t = ti-tj
                    w = 1/((arb(1)/4+t*t)*(arb(9)/4+t*t)).sqrt()
                    quadratic += a*b*(w*fejer(t,h,p,angle)+arb(2)/3*sinc_square(h*t/2))
            assert quadratic > 0
    print("Direct ordinate sums overlap the triangular polynomial at 12 frequency/scale choices.")
    print("A signed four-point quadratic form is strictly positive in all four test cases.")


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Enable Python assertions.")
    ctx.prec = 192
    check()
