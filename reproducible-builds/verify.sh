#!/usr/bin/env bash
# Build the jar twice from a clean state and require identical SHA-256 hashes.
set -euo pipefail
cd "$(dirname "$0")"
MVN="${MVN:-mvn}"
JAR=target/orders-repro-1.0.0.jar

build() {
  "$MVN" -B -q clean package
  sha256sum "$JAR" | cut -d' ' -f1
}

first=$(build)
sleep 2   # a different wall-clock time must not change the result
second=$(build)

echo "build 1: $first"
echo "build 2: $second"
if [ "$first" = "$second" ]; then
  echo "REPRODUCIBLE"
else
  echo "NOT REPRODUCIBLE" >&2
  exit 1
fi
