# Contributing to dileepadev

Thank you for your interest in contributing to [dileepadev](https://github.com/dileepadev/dileepadev)! We welcome contributions, including corrections, documentation improvements, and other general improvements.

This repository is the **platform root**: it holds the brand guidelines, the design system, the architecture documentation, and the cross-repository roadmap that the rest of the `dileepa.dev` platform implements against. It ships no application — there is no build, no test suite, and no dependencies. What changes here is prose, tokens, and assets, and those changes are read by people implementing in six other repositories.

## Getting Started

1. **Fork the repository**  
   Fork this repository to your GitHub account. This creates a copy of the repository in your account, allowing you to make changes without affecting the original repository.  
   To fork the repository, click the **Fork** button in the top right corner of this page or click [here to fork the repository](https://github.com/dileepadev/dileepadev/fork).

2. **Clone your fork**  
   Clone your forked repository to your local machine using the following command:

   ```bash
   git clone https://github.com/<your-username>/dileepadev.git
   ```

3. **Create a new branch**  
   Create a new branch for your changes. Follow the [branch naming guidelines](BRANCH_NAMING_GUIDELINES.md).

   ```bash
   git checkout -b your-branch-name
   ```

4. **Make changes and commit**  
   Make your changes and commit them with a descriptive commit message. Follow the [commit message guidelines](COMMIT_MESSAGE_GUIDELINES.md).

   ```bash
   git commit -m "docs: Correct the redirect status code"
   ```

5. **Push your changes**  
   Push your changes to your forked repository.

   ```bash
   git push origin your-branch-name
   ```

6. **Submit a pull request**  
   To submit a pull request:
   - Go to your forked repository.
   - Click the **Compare & pull request** button next to your `your-branch-name`.
   - Add a title and description for your pull request. Follow the [pull request guidelines](PULL_REQUEST_GUIDELINES.md).
   - Click **Create pull request** and remember to add the relevant labels using the [pull request template](.github/PULL_REQUEST_TEMPLATE.md).

## Guidelines

- Read [AGENTS.md](AGENTS.md) first. It is the single source of truth for how this repository is written and what must never be broken — the brand rules in particular.
- Write prose, not marketing. Sentence case everywhere, and a banned-word list that has no exceptions — both in [`DESIGN.md`](DESIGN.md) §17, and repeated in [AGENTS.md](AGENTS.md).
- Be exact about file paths, token names, and hex values. Vague guidance produces drift across seven repositories.
- **There is nothing to run here, so verification is manual.** Before opening a pull request, check that every file path, token name, and hex value you referenced actually exists, and that every cross-repository link resolves.
- Never declare a colour, type step, or spacing value in a document. They come from [`docs/brand/brand-tokens.css`](docs/brand/brand-tokens.css), which is the canonical token sheet for the whole platform.
- When a decision is still open, say so and record the alternatives. Do not present an unmade decision as settled.
- Keep your pull request focused and avoid unrelated changes.
- Refer to the following templates and guidelines before submitting your changes:
  - [dileepadev/](./) - Root directory of the repository
    - [.github/](./.github) - GitHub-specific files (templates, agent instructions, etc.)
      - [ISSUE_TEMPLATE/](./.github/ISSUE_TEMPLATE) - Contains all issue templates
        - [bug_report.md](./.github/ISSUE_TEMPLATE/bug_report.md) - Template for reporting bugs
        - [documentation_update.md](./.github/ISSUE_TEMPLATE/documentation_update.md) - Template for documentation updates
        - [feature_request.md](./.github/ISSUE_TEMPLATE/feature_request.md) - Template for suggesting new features
        - [feedback.md](./.github/ISSUE_TEMPLATE/feedback.md) - Template for general feedback
        - [other.md](./.github/ISSUE_TEMPLATE/other.md) - Template for other types of issues
      - [PULL_REQUEST_TEMPLATE.md](./.github/PULL_REQUEST_TEMPLATE.md) - Template for pull request submissions
    - [docs/](./docs) - The platform documentation this repository exists to publish
      - [README.md](./docs/README.md) - Platform documentation index
      - [brand/](./docs/brand) - Brand guide, canonical token sheet, design system, logo and assets
      - [architecture/](./docs/architecture) - Platform overview, API contract, content pipeline, redirects
      - [migration/](./docs/migration) - v2.0.0 migration plan and versioning policy
    - [AGENTS.md](./AGENTS.md) - Canonical instructions for AI coding agents, and the rules for this repo
    - [BRANCH_NAMING_GUIDELINES.md](./BRANCH_NAMING_GUIDELINES.md) - Branch naming rules
    - [CHANGELOG.md](./CHANGELOG.md) - Record of project changes
    - [CLAUDE.md](./CLAUDE.md) - Claude Code specific notes; points back to `AGENTS.md`
    - [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) - Contributor behavior guidelines
    - [COMMIT_MESSAGE_GUIDELINES.md](./COMMIT_MESSAGE_GUIDELINES.md) - Rules for writing commit messages
    - [CONTRIBUTING.md](./CONTRIBUTING.md) - How to contribute to the project
    - [DESIGN.md](./DESIGN.md) - Machine-readable design token and UI contract
    - [LICENSE](./LICENSE) - Project license
    - [PULL_REQUEST_GUIDELINES.md](./PULL_REQUEST_GUIDELINES.md) - Pull request submission guidelines
    - [README.md](./README.md) - The GitHub profile README
    - [SECURITY.md](./SECURITY.md) - Security policy and reporting
    - [TODO.md](./TODO.md) - Cross-repository roadmap
    - [VERSIONING.md](./VERSIONING.md) - Versioning strategy for the project

## Code of Conduct

This project adheres to the **Contributor Covenant Code of Conduct**. By participating, you agree to abide by its terms.  
Read the full Contributor Covenant Code of Conduct in the [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) file.

## Contact

If you have any questions or suggestions regarding these community standards, feel free to open an issue or submit a pull request in this repository.

You can also reach me via email at: **<contact@dileepa.dev>**
