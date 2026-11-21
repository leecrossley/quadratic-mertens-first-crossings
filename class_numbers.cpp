// Count ordinary ideal classes of the indicated squarefree real quadratic fields.
// Every operation on ideals is an integer operation. One row per discriminant.
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <unordered_set>
#include <vector>

using std::uint64_t;

std::vector<int> primes_up_to(int limit) {
    std::vector<bool> composite(limit + 1);
    std::vector<int> primes;
    for (int p = 2; p <= limit; ++p) {
        if (composite[p]) continue;
        primes.push_back(p);
        for (int n = 2*p; n <= limit; n += p) composite[n] = true;
    }
    return primes;
}

std::vector<std::uint16_t> odd_factors(int limit, const std::vector<int>& primes) {
    std::vector<std::uint16_t> least(limit/2 + 1);
    for (int p : primes) {
        if (p == 2) continue;
        if (p > limit/p) break;
        for (int n = p*p; n <= limit; n += 2*p) {
            if (!least[n/2]) least[n/2] = static_cast<std::uint16_t>(p);
        }
    }
    return least;
}

void divisors(int n, const std::vector<std::uint16_t>& least, std::vector<int>& result) {
    result.clear();
    result.push_back(1);
    while (n > 1) {
        int p = least[n/2];
        if (!p) p = n;
        int count = static_cast<int>(result.size());
        int power = 1;
        do {
            n /= p;
            power *= p;
            for (int i = 0; i < count; ++i) result.push_back(result[i]*power);
        } while (n % p == 0);
    }
}

uint64_t key(int a, int b) {
    return (uint64_t(a) << 32) | std::uint32_t(b);
}

int main(int argc, char** argv) {
    int limit = argc > 1 ? std::atoi(argv[1]) : 20001;
    if (limit < 1 || limit > 20001) return 2;
    const auto primes = primes_up_to(limit + 2);
    const auto least = odd_factors((limit*limit+3)/4, primes);
    std::vector<int> divs;
    std::unordered_set<uint64_t> remaining;
    std::cout << "m d h reduced\n";
    for (int m = 1; m <= limit; m += 2) {
        int d = m*m+4, root = (m == 1 ? 2 : m);
        assert(root*root < d && int64_t(root+1)*(root+1) > d);
        bool squarefree = true;
        for (int p : primes) {
            if (p > root) break;
            if (d % (p*p) == 0) { squarefree = false; break; }
        }
        if (!squarefree) continue;
        remaining.clear();
        remaining.reserve(2*root);
        for (int b = 1; b <= root; b += 2) {
            int product = (d-b*b)/4;
            assert(product > 0 && product % 2 == 1);
            divisors(product, least, divs);
            for (int a : divs) {
                if (2*a > root-b && 2*a <= root+b) {
                    bool fresh = remaining.insert(key(a,b)).second;
                    if (!fresh) return 3;
                }
            }
        }
        auto total = remaining.size();
        int classes = 0;
        while (!remaining.empty()) {
            uint64_t first = *remaining.begin(), here = first;
            do {
                if (remaining.erase(here) != 1) return 4;
                int a = int(here >> 32), b = int(std::uint32_t(here));
                int k = (b+root)/(2*a);
                int next_b = 2*a*k-b;
                int difference = d-next_b*next_b;
                if (difference <= 0 || difference % (4*a)) return 5;
                here = key(difference/(4*a), next_b);
            } while (here != first);
            ++classes;
        }
        std::cout << m << ' ' << d << ' ' << classes << ' ' << total << '\n';
    }
}
