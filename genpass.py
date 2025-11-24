import sys
import itertools

NUM_PAD = ["123", "999", "777", "666", "333", "111", "420", "69", "42069", "6969", "321"]
TEXT_PAD = ["asdf", "qwerty", "xoxo", "xo", "xox"]
END_SYMBOLS = ["!", "#"]

# Leetspeak mapping (multiple possible replacements)
LEET_MAP = {
    "a": ["4", "@"],
    "e": ["3"],
    "i": ["1", "!"],
    "o": ["0"],
    "s": ["5"],
    "t": ["7"],
}

# Vowel mutation list
VOWEL_MUTATE = {
    "a": ["4", "@"],
    "e": ["3"],
    "i": ["1"],
    "o": ["0"],
    "u": ["v"],   # popular obfuscation
}


def ensure_case(password):
    variants = set()
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)

    if has_upper and has_lower:
        variants.add(password)
        return variants

    if not has_upper:
        variants.add(password[0].upper() + password[1:])

    if not has_lower:
        variants.add(password[0].lower() + password[1:])

    variants.add(password)
    return variants


def pad_password(p):
    pads = TEXT_PAD if p.isdigit() else NUM_PAD
    variants = set()

    if len(p) >= 8:
        variants.add(p)

    for pad in pads:
        newp = p + pad
        if len(newp) >= 8:
            variants.add(newp)

    return variants


def end_with_symbol(p):
    return {p + sym for sym in END_SYMBOLS}


def substitute_at(p):
    results = set()
    for i, c in enumerate(p):
        if c.lower() == "a":
            results.add(p[:i] + "@" + p[i+1:])
    return results


def apply_leetspeak(p):
    variants = set()
    for i, c in enumerate(p):
        cl = c.lower()
        if cl in LEET_MAP:
            for rep in LEET_MAP[cl]:
                variants.add(p[:i] + rep + p[i+1:])
    return variants


def mutate_vowels(p):
    variants = set()
    for i, c in enumerate(p):
        cl = c.lower()
        if cl in VOWEL_MUTATE:
            for rep in VOWEL_MUTATE[cl]:
                variants.add(p[:i] + rep + p[i+1:])
    return variants


def generate_all_variants(word):
    base = word.strip()
    if not base:
        return []

    results = set()

    # 1. Enforce case on base
    case_vars = ensure_case(base)

    for cv in case_vars:
        # 2. Leetspeak
        leet_vars = apply_leetspeak(cv)
        leet_vars.add(cv)

        # 3. Vowel mutations
        vowel_vars = set()
        for lv in leet_vars:
            vowel_vars |= mutate_vowels(lv)
            vowel_vars.add(lv)

        # 4. Pad to >= 8
        padded_vars = set()
        for vv in vowel_vars:
            padded_vars |= pad_password(vv)

        # 5. End with symbols
        for pv in padded_vars:
            results |= end_with_symbol(pv)

            # 6. @ substitutions
            at_vars = substitute_at(pv)
            for av in at_vars:
                results |= end_with_symbol(av)

        # 7. Final ensure-case on ALL outputs
        final_results = set(results)

        for w in list(results):

            # Skip strings with no alphabet letters
            if not any(ch.isalpha() for ch in w):
                continue

            # Ensure uppercase exists
            if not any(c.isupper() for c in w):
                for i, ch in enumerate(w):
                    if ch.isalpha():
                        final_results.add(w[:i] + ch.upper() + w[i+1:])

            # Ensure lowercase exists
            if not any(c.islower() for c in w):
                for i, ch in enumerate(w):
                    if ch.isalpha():
                        final_results.add(w[:i] + ch.lower() + w[i+1:])

    return final_results

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 genpass.py input.txt")
        sys.exit(1)

    infile = sys.argv[1]
    outfile = "output.txt"

    out = set()

    with open(infile, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            variants = generate_all_variants(line)
            out.update(variants)

    out = sorted(out)

    with open(outfile, "w") as f:
        for pw in out:
            f.write(pw + "\n")

    print(f"[+] Generated {len(out)} password variants → {outfile}")


if __name__ == "__main__":
    main()
