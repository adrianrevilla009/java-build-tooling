#!/usr/bin/env python3
"""Monorepo benefit in miniature: given changed files, find every module that must be rebuilt.

In a monorepo one commit can change a library and all its consumers atomically, and this
graph walk tells CI exactly what to rebuild. In a polyrepo the same change is N PRs in N repos.
"""
import sys

# module -> (path prefix, modules it depends on)
MODULES = {
    "orders-core": ("libs/orders-core/", []),
    "orders-pricing": ("libs/orders-pricing/", ["orders-core"]),
    "orders-api": ("apps/orders-api/", ["orders-core", "orders-pricing"]),
    "orders-batch": ("apps/orders-batch/", ["orders-core"]),
}


def affected(changed_files):
    hit = {m for m, (prefix, _) in MODULES.items() if any(f.startswith(prefix) for f in changed_files)}
    grew = True
    while grew:  # add dependents until nothing new appears
        grew = False
        for m, (_, deps) in MODULES.items():
            if m not in hit and hit.intersection(deps):
                hit.add(m)
                grew = True
    return sorted(hit)


def main():
    cases = {
        "libs/orders-core/Order.java": ["orders-api", "orders-batch", "orders-core", "orders-pricing"],
        "libs/orders-pricing/Price.java": ["orders-api", "orders-pricing"],
        "apps/orders-batch/Job.java": ["orders-batch"],
    }
    for changed, expected in cases.items():
        got = affected([changed])
        assert got == expected, f"{changed}: expected {expected}, got {got}"
        print(f"{changed} -> rebuild {', '.join(got)}")
    print("OK")


if __name__ == "__main__":
    sys.exit(main())
