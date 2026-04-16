# Contributing

## Local Build

Install dependencies and build the documentation:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
make -C docs html
```

Treat Sphinx warnings as issues to fix before submitting changes.

## Bilingual Structure

Every new page should be added to both language trees:

```text
docs/source/zh_CN/<section>/<page>.md
docs/source/en/<section>/<page>.md
```

Keep directory names and page slugs aligned. Chinese can be the primary writing language, but English pages should remain readable and should not be empty.

## Standard Page Template

Use this structure for major topic pages:

```markdown
# Chapter Title

## Learning Goals
## Prerequisites
## Core Concepts
## Mathematical Formulation
## Algorithms / System Design
## Practical Notes
## Common Pitfalls
## Recommended Reading
## Exercises / Research Questions
## Glossary
```

Short overview pages may omit sections that do not apply.

## External Links and Citations

- Link to stable project pages, papers, or documentation whenever possible.
- Explain why a resource is useful instead of listing links without context.
- Do not copy substantial text from external resources.
- Keep [OpenAI Spinning Up](https://spinningup.openai.com/en/latest/) linked from RL Basics as a classical RL reference.

## Updating Reading Lists

When adding a paper or resource, prefer entries that are useful for a junior PhD student: clear problem statement, reusable method, strong baseline, benchmark value, or important negative lesson.
