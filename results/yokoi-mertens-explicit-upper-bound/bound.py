"""Print the integer cutoff symbolically for a real quadratic field."""
import argparse


def parameters(d):
    if d < 5:
        raise ValueError("A positive real quadratic fundamental discriminant is at least 5.")
    ceil_log2 = (d - 1).bit_length()
    h = 512 + 128 * ceil_log2
    return h, 32*h + 4, 32*h + 9, 64*h + 9


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("d", type=int, help="positive fundamental discriminant, e.g. 9413")
    args = parser.parse_args()
    try:
        h, log_t, log_q, log_n_over_h = parameters(args.d)
    except ValueError as err:
        parser.error(str(err))
    print(f"d = {args.d}, H = {h}")
    print(f"T = 2^{log_t}, Q = 2^{log_q}, N = {h} * 2^{log_n_over_h}")
    print(f"Sharper cutoff = 2^(2^(3 + {h} * {log_q} * 2^{log_n_over_h}))")
    print(f"Simpler cutoff = 2^(2^({args.d}^30000))")


if __name__ == "__main__":
    main()
