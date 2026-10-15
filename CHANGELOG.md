# CHANGELOG


## v0.6.1 (2026-10-15)

### Bug Fixes

- Republish with corrected README usage examples
  ([`9b03d39`](https://github.com/toltapp/tolt-python-sdk/commit/9b03d39ac1479388708e378b1cff9dcb1a81dd66))

### Documentation

- Use the renamed partners.approve method in README usage
  ([`f0a653a`](https://github.com/toltapp/tolt-python-sdk/commit/f0a653aeb2cc41184585fd140261fe7e4594f04b))


## v0.6.0 (2026-10-15)

### Features

- Regenerate SDK from the latest OpenAPI spec
  ([#6](https://github.com/toltapp/tolt-python-sdk/pull/6),
  [`af7cca1`](https://github.com/toltapp/tolt-python-sdk/commit/af7cca1a24822edffc426cf01e2b4f6d5725c72e))


## v0.5.0 (2026-09-28)

### Features

- Regenerate SDK from the latest OpenAPI spec
  ([#5](https://github.com/toltapp/tolt-python-sdk/pull/5),
  [`08c6800`](https://github.com/toltapp/tolt-python-sdk/commit/08c6800fbaa9c264999dbe78e868b9825af55876))


## v0.4.0 (2026-09-21)

### Features

- Regenerate SDK from the latest OpenAPI spec
  ([#4](https://github.com/toltapp/tolt-python-sdk/pull/4),
  [`d1a6a94`](https://github.com/toltapp/tolt-python-sdk/commit/d1a6a946e7f48379c49bed4031ad46f9ef814b1c))


## v0.3.0 (2026-09-21)

### Features

- Regenerate SDK from the latest OpenAPI spec
  ([#3](https://github.com/toltapp/tolt-python-sdk/pull/3),
  [`6ed6e91`](https://github.com/toltapp/tolt-python-sdk/commit/6ed6e917201da6205b2143a8c745c47030285439))


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
