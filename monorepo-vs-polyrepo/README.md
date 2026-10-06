# monorepo-vs-polyrepo

`affected.py`, a small script that maps changed files to the modules to rebuild in a four-module Orders layout.

## Goal

Make the monorepo versus polyrepo trade-off concrete: given a changed file, list every module that must be rebuilt.

## Run it

```bash
python3 affected.py
```

Expected output, which was run and matches:

```
libs/orders-core/Order.java -> rebuild orders-api, orders-batch, orders-core, orders-pricing
libs/orders-pricing/Price.java -> rebuild orders-api, orders-pricing
apps/orders-batch/Job.java -> rebuild orders-batch
OK
```

Only Python 3 is required.

## What it proves

- A change in `orders-core` rebuilds four modules, a change in `orders-pricing` rebuilds two, and a change in the leaf `orders-batch` rebuilds one.
- The script asserts each of these three cases and exits with an error if the dependency walk gives a different answer.
- In a monorepo that is one atomic commit; in a polyrepo the `orders-core` change would be four pull requests plus version bumps and a release order.

## Trade-offs

- A monorepo needs affected-only builds (like this script) or CI slows down; a polyrepo builds only itself.
- A monorepo needs CODEOWNERS and tooling for ownership; per-repo permissions are natural in a polyrepo.
- The module graph in `affected.py` is hard-coded and path-based; real tools such as Bazel, Gradle or Nx derive it from build files.

## When not to use it

- Do not use a monorepo when teams ship independently with separate release cycles and little shared code.
- Do not use a polyrepo when most changes touch several modules together.
