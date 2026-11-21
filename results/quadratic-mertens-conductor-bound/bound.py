"""Print the a priori integer bound without expanding the tower."""
import argparse
import sys


def ceil_log2(n):
    return (n-1).bit_length()


def parameters(d):
    if d < 5:
        raise ValueError("The theorem uses a real quadratic fundamental discriminant d >= 5.")
    ell = 16 + ceil_log2(d)
    m = 1024 + 16*ceil_log2(ell)
    t = (1 << 257)*m*ell**2
    return ell, m, t, 64*t*ell, 128*t*ell, 1000*ell


def main():
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    arg = argparse.ArgumentParser(description=__doc__)
    arg.add_argument("d", type=int)
    args = arg.parse_args()
    try:
        ell, m, t, n, q, j = parameters(args.d)
    except ValueError as exc:
        arg.error(str(exc))
    print(f"L={ell}, m={m}, T={t}")
    print(f"J={j}, Q={q}, N={n}")
    print("U = 2^(4 * J * Q^N)")
    print(f"log2(log2(U)) <= {ceil_log2(4*j) + n*ceil_log2(q)}")


if __name__ == "__main__":
    main()
