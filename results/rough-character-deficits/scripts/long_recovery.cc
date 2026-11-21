// Full second pass over the signed count with 43 retained, in 64-integer blocks.
#include <algorithm>
#include <bit>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>

using Word = std::uint64_t;
using Flags = std::vector<unsigned char>;
constexpr int conductor = 2380853;
constexpr std::size_t chunk = 2048;
constexpr Word limit = 137705727787;

struct Cycle {
    std::size_t period;
    std::vector<Word> words;

    explicit Cycle(Flags flags) : period(flags.size()), words(period + chunk) {
        flags.resize(period + 64);
        for (std::size_t i = 0; i < 64; ++i) {
            flags[period + i] = flags[i % period];
        }
        for (std::size_t k = 0; k < period; ++k) {
            auto start = (64 * k) % period;
            for (int j = 0; j < 64; ++j) {
                words[k] |= Word(flags[start + j]) << j;
            }
        }
        for (std::size_t k = 0; k < chunk; ++k) {
            words[period + k] = words[k % period];
        }
    }
};

std::vector<Cycle> make_filters(const Flags& square) {
    std::vector<int> primes, deleted;
    for (int n = 2; n <= 215; ++n) {
        if (std::none_of(primes.begin(), primes.end(), [n](int p) { return n % p == 0; })) {
            primes.push_back(n);
            if (!square[n] && n != 43) deleted.push_back(n);
        }
    }
    assert(deleted.size() == 30 && !square[43]);
    std::vector<int> periods;
    for (auto it = deleted.rbegin(); it != deleted.rend(); ++it) {
        auto row = std::find_if(periods.begin(), periods.end(),
                                [p = *it](int n) { return n <= 65000 / p; });
        if (row == periods.end()) periods.push_back(*it);
        else *row *= *it;
    }
    std::vector<Cycle> filters;
    for (int size : periods) {
        Flags keep(size);
        for (int j = 0; j < size; ++j) keep[j] = std::gcd(j, size) == 1;
        filters.emplace_back(keep);
    }
    return filters;
}

int main() {
    Flags square(conductor);
    for (std::int64_t n = 1; n <= conductor / 2; ++n) square[n * n % conductor] = 1;
    Cycle residues(square);
    auto filters = make_filters(square);
    std::vector<Word> keep(chunk), events;
    std::int64_t total = 0;
    for (Word start = 0; start <= limit / 64; start += chunk) {
        auto width = std::min<Word>(chunk, limit / 64 - start + 1);
        std::fill_n(keep.begin(), width, ~Word(0));
        for (const auto& cycle : filters) {
            auto mask = cycle.words.data() + start % cycle.period;
            for (Word k = 0; k < width; ++k) keep[k] &= mask[k];
        }
        Word low = 64 * start;
        Word high = std::min(limit, low + 64 * width - 1);
        for (Word n = ((low + conductor - 1) / conductor) * conductor; n <= high; n += conductor) {
            keep[(n - low) / 64] &= ~(Word(1) << (n % 64));
        }
        if (high % 64 != 63) keep[width - 1] &= (Word(1) << (high % 64 + 1)) - 1;
        auto positive = residues.words.data() + start % residues.period;
        for (Word k = 0; k < width; ++k) {
            Word alive = keep[k], plus = alive & positive[k];
            int up = std::popcount(plus);
            int down = std::popcount(alive) - up;
            int target = events.size() == 1 ? 1 : 19;
            if (events.empty() ? total - down >= 0 : total + up < target) {
                total += up - down;
                continue;
            }
            while (alive) {
                int bit = std::countr_zero(alive);
                total += (plus & (Word(1) << bit)) ? 1 : -1;
                if ((events.empty() && total < 0) || (events.size() == 1 && total > 0) ||
                    (events.size() == 2 && total >= 19)) {
                    events.push_back(low + 64 * k + bit);
                }
                alive &= alive - 1;
            }
        }
    }
    if (events != std::vector<Word>{48221, 137705720539, limit}) return 1;
    std::cout << "Independent 64-integer sweep reproduces all three positions.\n";
}
