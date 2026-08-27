# CHANGELOG


## v0.2.0 (2026-08-27)

### Continuous Integration

- Run python-semantic-release as a pinned CLI to avoid the GitPython incompatibility in the Docker
  action
  ([`c906dd0`](https://github.com/toltapp/tolt-python-sdk/commit/c906dd0c5e5b4c0bb6120278e2c8aca4c7cf71fc))

- Switch to python-semantic-release with OIDC and drop the bootstrap workflow
  ([`6e81608`](https://github.com/toltapp/tolt-python-sdk/commit/6e816089c2433bbab2db05f5bbf71fedf1516282))

### Features

- Regenerate SDK from the latest OpenAPI spec
  ([#2](https://github.com/toltapp/tolt-python-sdk/pull/2),
  [`364053f`](https://github.com/toltapp/tolt-python-sdk/commit/364053ff4925be037774bc4706cbff08a519de39))


## v0.1.0 (2026-08-27)

### Chores

- Gitignore Fern .fern/ metadata to keep regen PRs clean
  ([`d6230b1`](https://github.com/toltapp/tolt-python-sdk/commit/d6230b10e9f1f135b10cb39e1f30c27c1b564b8a))

- Regenerate SDK from the latest OpenAPI spec
  ([#1](https://github.com/toltapp/tolt-python-sdk/pull/1),
  [`11853bd`](https://github.com/toltapp/tolt-python-sdk/commit/11853bd4b5c1f9efe194d33c1c0c5f1ed80ee218))

- Restructure into src/tolt package layout (reproducible Fern output)
  ([`ad467d1`](https://github.com/toltapp/tolt-python-sdk/commit/ad467d19844bab180481460476a6a0e1aa36779f))

### Continuous Integration

- Add Apache-2.0 license and PyPI publishing
  ([`188dced`](https://github.com/toltapp/tolt-python-sdk/commit/188dced8aed1c851088f35c148d9346367bde892))

Bootstrap workflow does the first publish of 0.1.0 via PyPI trusted publishing (OIDC), which can
  mint a brand-new project. pyproject carries semantic-release config for versions after that.

- Grant contents:read to bootstrap publish so checkout can read the repo
  ([`8811843`](https://github.com/toltapp/tolt-python-sdk/commit/8811843ccc7fade366d530058503905104f6d684))
