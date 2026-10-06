#!/usr/bin/env bash
# Build, wipe build outputs, rebuild with --build-cache: compileJava must be FROM-CACHE.
set -euo pipefail
cd "$(dirname "$0")"
GRADLE="${GRADLE:-./gradlew}"

rm -rf .build-cache build
"$GRADLE" --no-daemon --build-cache compileJava >/dev/null   # populates the cache
rm -rf build                                                  # outputs gone, cache stays
out=$("$GRADLE" --no-daemon --build-cache compileJava)

if grep -q ":compileJava FROM-CACHE" <<<"$out"; then
  echo "CACHE HIT: :compileJava FROM-CACHE"
else
  echo "CACHE MISS" >&2
  exit 1
fi
