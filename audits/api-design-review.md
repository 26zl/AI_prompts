# API Design Review

Review the design of this project's interfaces: REST or HTTP APIs, GraphQL, gRPC, WebSocket and event interfaces, webhooks, and the public surface of SDKs and libraries. Judge consistency, clarity, safety and evolvability from the consumer's point of view, and recommend the changes that are worth their cost.

## Settings

- Mode: report
- Scope: all interfaces the project exposes
- Report language: English

`report` mode changes nothing. `fix` mode also applies the non-breaking changes described under "Changes".

## Working environment

- **With access to the project** (a coding agent such as Claude Code, Codex, Cursor, Gemini CLI or GitHub Copilot): read route definitions, handlers, schemas (OpenAPI, GraphQL SDL, protobuf), serializers, client SDKs and the API documentation; run the API locally if that is easy and safe.
- **Without access** (a plain chat): ask me for the API specification or route list, example requests and responses, the error format, the authentication model, and who the consumers are. Mark what you cannot see as "Not verified".

## How to work

1. **Identify the consumers**: a first-party frontend, mobile apps, third-party developers, internal services, AI agents. Their needs decide what matters: stability and documentation for third parties, flexibility for a first-party frontend.
2. **Read the whole surface** before judging any part; consistency is only visible across endpoints.
3. **Walk through the main use cases** as a consumer would: authenticate, list, search, create, update, delete, handle an error, paginate through a large set, receive a webhook, upgrade to a new version.
4. **Go through the checklist**; give every item Pass, Fail, Partial, Not applicable or Not verified, with evidence.

## Checklist

### Consistency and naming

1. **One style** throughout: casing of fields and paths, plural resource names, verb usage, parameter names, date and ID formats, envelope or no envelope.
2. **Clear resource model**: nouns for resources, relationships expressed predictably, no endpoints that do several unrelated things, no leaking of internal table or class names.
3. **Predictable shapes**: the same entity is represented the same way everywhere; optional fields are either present with null or absent, consistently.

### HTTP semantics (REST and HTTP APIs)

4. **Methods and status codes** used correctly: GET is safe and cacheable, PUT and DELETE are idempotent, POST creates or performs actions, PATCH updates partially; 200, 201, 202, 204, 400, 401, 403, 404, 409, 422 and 429 used for their meanings.
5. **Idempotency** for retried writes: an `Idempotency-Key` or equivalent for POST operations that must not run twice (payments, orders, messages).
6. **Errors** in one documented format (for example RFC 9457 problem details or a consistent equivalent) with a stable machine-readable code, a human-readable message, field-level details for validation errors, and a request ID; no stack traces or internals.
7. **Pagination** on every list endpoint, cursor-based for large or changing sets, with a maximum page size and a stable sort; filtering and sorting parameters documented and validated.
8. **Caching and concurrency**: `ETag` or `Last-Modified` where it helps; conditional requests to prevent lost updates on concurrent edits; `Cache-Control` set deliberately.
9. **Long-running operations** return 202 with a job resource to poll or a callback, rather than holding the connection.
10. **Bulk operations** where consumers need them, with per-item results.
11. **Content and formats**: JSON by default, explicit `Content-Type`, ISO 8601 timestamps in UTC with offset, explicit units and currencies, numbers that fit the client's precision (large integers and money as strings or minor units where needed).

### Security and limits

12. **Authentication** consistent across all endpoints; scopes or permissions per endpoint documented; no undocumented or unauthenticated internal endpoints.
13. **Rate limits** documented, with `429` and headers that tell the client when to retry.
14. **Input limits**: maximum body size, array lengths, string lengths and nesting depth; validation errors explain the limit.
15. **Field exposure**: responses contain only what the consumer needs; sensitive fields never returned; partial responses or field selection where payloads are large.

### Versioning and evolution

16. **Versioning strategy** chosen and documented (URL, header or date-based), applied consistently, with a deprecation policy, timelines and communication.
17. **Backward compatibility** rules: adding fields is safe, removing or renaming is a new version; enum values can grow; clients are told to ignore unknown fields.
18. **Breaking-change detection**: contract tests, schema diffing in CI (for example on the OpenAPI, GraphQL or protobuf files), and consumer-driven tests for internal services.

### Documentation and developer experience

19. **A specification** (OpenAPI, GraphQL schema, protobuf) exists, is generated from or validated against the code, and is the source for documentation and SDKs.
20. **Documentation** covers authentication, every endpoint with request and response examples, error codes, pagination, rate limits, versioning, webhooks and a changelog; a quick start gets a new consumer to a first successful call in minutes.
21. **Examples and SDKs** stay in sync with the API; generated clients where that helps; a sandbox or test mode for consumers who handle money.
22. **Consistency with the product**: the API exposes what the UI can do, so consumers are not forced to scrape or reverse-engineer.

### GraphQL

23. **Schema design**: clear types and nullability, connections for pagination, input types for mutations, descriptive mutation names and payloads with errors; deprecation with `@deprecated` and a reason.
24. **Operational safety**: query depth and complexity limits, persisted or allow-listed queries for public clients, introspection disabled or restricted in production, batching abuse limited, data loaders to prevent N+1 queries, per-field authorization.

### gRPC and protobuf

25. **Proto style**: packages and naming per the style guide, field numbers never reused or renumbered, reserved fields on removal, enums with a zero unknown value, deadlines propagated, standard status codes, streaming used where it fits.

### Webhooks and events

26. **Webhooks**: signed over the raw body, with timestamps for replay protection, retries with backoff, idempotency through event IDs, versioned event schemas, documentation of each event with examples, and a way for consumers to replay or inspect deliveries.
27. **Events and messages**: schemas versioned and compatible, ordering and delivery guarantees documented (at least once, at most once), consumers expected to be idempotent, dead-letter handling.

### SDK and library surface

28. **Public API minimal and deliberate**: internals not exported; names consistent and discoverable; typed; errors as typed exceptions or results; configuration through explicit options; sensible defaults; no global state; asynchronous and synchronous forms consistent; breaking changes only in major versions with migration notes.

## Changes (`fix` mode only)

Apply only non-breaking changes: documentation and specification fixes so they match the code, examples, deprecation annotations, additional response fields that the code already has, validation messages, and tests. Anything that changes a contract (renaming, removing, changing types or status codes, changing authentication) is proposed, with a migration path, and waits for my approval. Do not commit or push.

## Rules

- Never print secret values found in example requests, configuration or documentation; refer to their type and location only.
- Base findings on the specification, the code and real requests and responses; mark behavior you could not observe as Not verified.

## Report

1. **Summary**: who the consumers are, how the API feels to use today, and the three to five changes with the best value.
2. **Findings**, most important first. For each one:
   - Problem, with an example request or response
   - Impact on consumers
   - Location: endpoint, type or file
   - Recommendation, and whether it is breaking
   - Migration path for breaking changes
   - Status: Verified, Likely or Needs manual check
   - Fixed: yes or no
3. **Checklist results**: every item with Pass, Fail, Partial, Not applicable or Not verified.
4. **Consistency table**: the conventions found (naming, errors, pagination, timestamps, IDs, versioning) and where they deviate.
5. **Changes made** (`fix` mode).
6. **Proposed design guidelines** for this API, one page, so future endpoints stay consistent.

Priority levels:

- **High**: consumers get wrong data, lose updates, cannot recover from errors, or will be broken by the next change.
- **Medium**: an inconsistency or missing capability that costs consumers real effort.
- **Low**: polish.
