# CHANGELOG


## v1.1.0 (2026-10-21)

### Features

- Regenerate SDK from the latest OpenAPI spec
  ([#14](https://github.com/toltapp/tolt-python-sdk/pull/14),
  [`f3ac014`](https://github.com/toltapp/tolt-python-sdk/commit/f3ac0140ceed185fd4244fae9dbebde2f4b32855))


## v1.0.0 (2026-10-21)

### Bug Fixes

- Require Python 3.10 ([#10](https://github.com/toltapp/tolt-python-sdk/pull/10),
  [`83e9ef9`](https://github.com/toltapp/tolt-python-sdk/commit/83e9ef9a1053f0050091dee5e3f085f91b8b4cf1))

The SDK fails on Python 3.8 and 3.9 whenever it parses a response: the generated serializer
  evaluates the type hints of pydantic's ConfigDict, which use X | None, and that syntax only
  evaluates at runtime from Python 3.10. The package claimed >=3.8, so pip installed a client that
  broke on its first call.

### Chores

- Let a breaking change release 1.0.0 ([#12](https://github.com/toltapp/tolt-python-sdk/pull/12),
  [`9b61b78`](https://github.com/toltapp/tolt-python-sdk/commit/9b61b782037a98135ba20247bad2d5810a1450ec))

With major_on_zero = false, python-semantic-release turns a breaking change on 0.x into a minor
  bump, so the SDK 1.0 regen would have shipped as 0.8.0.

- Sync the User-Agent version at release ([#9](https://github.com/toltapp/tolt-python-sdk/pull/9),
  [`61f27a7`](https://github.com/toltapp/tolt-python-sdk/commit/61f27a7d4f3c7f9d7b64bee2698fc52c5fdc2683))

* chore: sync the User-Agent version at release

The generated client sends User-Agent: tolt-python/<version> with the version baked in at generation
  time. The release build now rewrites it to the version being published and commits the file with
  the release.

* chore: fail the release if the User-Agent version isn't rewritten

A sed with no match exits 0, so a release could ship a stale or missing User-Agent version without
  anyone noticing. The build now checks that src/tolt/core/client_wrapper.py contains
  tolt-python/<new version> after the rewrite and stops the release with a message if it doesn't.

### Features

- Regenerate SDK from the latest OpenAPI spec
  ([#11](https://github.com/toltapp/tolt-python-sdk/pull/11),
  [`6cd52e7`](https://github.com/toltapp/tolt-python-sdk/commit/6cd52e7bc34cbddf54369663bbf4479fe96227f1))

SDK 1.0. Regenerated with the Fern Python generator 5.41.4 and the overrides in toltapp/tolt-sdks.

- list() returns a pager: iterate it to walk every page. - clicks.create, commissions.create and
  embed_tokens.create take typed arguments. - Creates and transactions.rerun_flows are not retried
  automatically. - Requests send User-Agent: tolt-python/<version>.

BREAKING CHANGE: Type and module names for single-item operations are singular (GetPartnerResponse,
  create_partner_request_status). embed.create_token() is now embed_tokens.create(),
  reports.customer_stats() is now reports.customers(), and the Error model is now ErrorResponse
  (with ErrorCode and FieldError). list() returns a SyncPager or AsyncPager instead of the envelope:
  rows are in .items rather than .data, and has_more and next_cursor move to .response.
  groups.list(default=...) and flows.list(active=...) take booleans. Python 3.10 or newer is
  required.

### Breaking Changes

- Type and module names for single-item operations are singular (GetPartnerResponse,
  create_partner_request_status). embed.create_token() is now embed_tokens.create(),
  reports.customer_stats() is now reports.customers(), and the Error model is now ErrorResponse
  (with ErrorCode and FieldError). list() returns a SyncPager or AsyncPager instead of the envelope:
  rows are in .items rather than .data, and has_more and next_cursor move to .response.
  groups.list(default=...) and flows.list(active=...) take booleans. Python 3.10 or newer is
  required.


## v0.7.1 (2026-10-21)

### Bug Fixes

- Ship py.typed, keep tests out of the wheel, and run CI on pull requests
  ([#8](https://github.com/toltapp/tolt-python-sdk/pull/8),
  [`6d7bb19`](https://github.com/toltapp/tolt-python-sdk/commit/6d7bb190b3761c64be68a2299e350fa765f680b7))

* fix: ship py.typed, keep tests out of the wheel, and run CI on pull requests

The wheel had no py.typed marker, so mypy skipped the package entirely ("missing library stubs or
  py.typed marker"), and it shipped tolt/tests/ and three markdown files that Fern writes next to
  the source. Fern owns src/tolt and removes files it didn't generate, so py.typed is force-included
  from the repo root.

Adds a PR workflow that builds the wheel, checks its contents, runs the tests on Python 3.8 and
  3.12, and type-checks the package and a strict caller.

* ci: test on Python 3.10 and 3.13

The SDK doesn't run on 3.8 or 3.9 (#10 raises requires-python to 3.10), so the matrix covers the
  supported floor and the newest release.


## v0.7.0 (2026-10-21)

### Features

- Regenerate SDK from the latest OpenAPI spec
  ([#7](https://github.com/toltapp/tolt-python-sdk/pull/7),
  [`f34a84c`](https://github.com/toltapp/tolt-python-sdk/commit/f34a84cfa73c2591f0e27908c13b28f6459b84fe))


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
