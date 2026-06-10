# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2024-01-01

### Added
- Initial release.
- `POST /extract` native extraction endpoint.
- `POST /v1/scrape` Firecrawl-compatible extraction endpoint (minimal subset).
- `GET /healthz`, `GET /readyz`, `GET /v1/health` health endpoints.
- SSRF protection: blocks private, loopback, link-local, and cloud metadata addresses.
- Layered HTML extraction pipeline: trafilatura → readability → fallback.
- PDF extraction using pypdf.
- Plain-text content type support.
- Optional browser-rendered extraction via Crawl4AI (requires browser profile).
- In-memory sliding-window rate limiter.
- Optional in-memory TTL cache.
- Docker and docker-compose support.
- GitHub Actions for CI and Docker publish to GHCR.
- Structured logging with domain-only URL masking by default.
- Full pytest test suite (56 tests, no external network).
