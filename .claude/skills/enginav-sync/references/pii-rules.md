# PII tagging for field nodes

Tag by property name (case-insensitive, camel/snake/kebab all match) or TS/zod type. First match wins.

| category | name contains / type | pii_confidence |
|---|---|---|
| email | `email`, `mail`, zod `.email()`, type `EmailStr` | 0.95 |
| phone | `phone`, `mobile`, `msisdn`, `tel` | 0.9 |
| name | `firstName`, `lastName`, `fullName`, `displayName`, `userName`, `givenName`, `surname` | 0.85 |
| address | `address`, `street`, `postcode`, `zip`, `city` (with other address fields) | 0.8 |
| id | `ssn`, `nationalId`, `passport`, `taxId`, `ipAddress`, `ip` | 0.85 |
| financial | `iban`, `card`, `pan`, `accountNumber`, `sortCode` | 0.9 |
| (person refs) | `createdBy`, `updatedBy`, `userId`, `ownerId`: pii true, category `id`, only if the value is a user identity (email/user id); check the type or an example | 0.6 |
| none | everything else | 1.0 |

Set `pii: true` for every category except `none`. Unsure → pick the category with confidence ≤ 0.6 and mention it in your reply.
