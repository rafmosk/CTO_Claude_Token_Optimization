# Privacy rules

This repository is public and permanent: anything committed stays in the Git history even after it is deleted from the files.

## Never include

- Names, email addresses, phone numbers, postal addresses
- Employer, client or company names tied to a real person or a real deal
- Salaries, prices you negotiated, contract terms
- API keys, tokens, passwords, session links, account or organization IDs
- Links to private documents, chats or artifacts
- Health, family or other personal details, even inside an example prompt
- Screenshots that show any of the above

## How to anonymize

- Replace real values with clear placeholders: `<NAME>`, `<COMPANY>`, `<EMAIL>`, `<PROJECT>`.
- Keep the **structure** of a prompt or a skill, remove the **content** that is about you.
- When in doubt, leave it out.

## Automatic check

Every pull request runs [`scripts/check_personal_data.py`](scripts/check_personal_data.py), which looks for common patterns (email addresses, phone numbers, IBANs, API keys). It is a safety net, not a guarantee: the responsibility stays with the contributor.

## If something slipped through

Do not open a public issue that repeats the data. Contact a maintainer through GitHub, and the history will be cleaned.
