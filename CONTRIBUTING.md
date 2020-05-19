# Contributing to GovText

We would love for you to contribute to GovText and help make it even better than it is today! As a contributor, here are the guidelines we would like you to follow:

* [Code of Conduct](#code-of-conduct)
* [Questions](#questions)
* [Issues and Bugs](#issues-and-bugs)
* [Feature Requests](#feature-requests)
* [Submission Guidelines](#submission-guidelines)
    * [Submitting an Issue](#submitting-an-issue)
    * [Submitting a Pull Request (PR)](#submitting-a-pr)
* [Commit Message Guidelines](#commit-message-guidelines)
    * [Commit Message Format](#commit-message-format)
    * [Revert](#revert)
    * [Type](#type)
    * [Scope](#scope)
    * [Subject](#subject)
    * [Body](#body)
    * [Footer](#footer)

## Code of Conduct <a name="code-of-conduct"></a>

Help us keep GovText open and inclusive. Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## Questions <a name="questions"></a>

Do not open issues for general support questions as we want to keep GitHub issues for bug reports and feature requests. Instead, drop us an email with your question at [text@dsaid.gov.sg](mailto:text@dsaid.gov.sg) and we will try to get back to you ASAP!

## Issues and Bugs <a name="issues-and-bugs"></a>
If you find a bug in the source code, you can help us by
[submitting an issue](#submitting-an-issue) to our GitHub Repository.

For security related issues or bugs, please email us at [text@dsaid.gov.sg](mailto:text@dsaid.gov.sg) instead.

## Feature Requests <a name="feature-requests"></a>
You can *request* a new feature by [submitting an issue](#submitting-an-issue) to our GitHub
Repository.

## Submission Guidelines <a name="submission-guidelines"></a>

### Submitting an Issue <a name="submitting-an-issue"></a>

Before you submit an issue, please search the issue tracker, maybe an issue for your problem already exists and the discussion might inform you of workarounds readily available.

We want to fix all the issues as soon as possible, but before fixing a bug we need to reproduce and confirm it. In order to reproduce bugs, we will systematically ask you to provide a minimal reproduction. Having a minimal reproducible scenario gives us a wealth of important information without going back & forth to you with additional questions.

A minimal reproduction allows us to quickly confirm a bug (or point out a coding problem) as well as confirm that we are fixing the right problem.

We will be insisting on a minimal reproduction scenario in order to save maintainers time and ultimately be able to fix more bugs. Interestingly, from our experience, users often find coding problems themselves while preparing a minimal reproduction. We understand that sometimes it might be hard to extract essential bits of code from a larger codebase but we really need to isolate the problem before we can fix it.

Unfortunately, we are not able to investigate / fix bugs without a minimal reproduction, so if we don't hear back from you, we are going to close an issue that doesn't have enough info to be reproduced.

You can file new issues by selecting from [new issue templates](https://github.com/dsaidgovsg/govtext-template/issues/new/choose) and filling out the issue template.

### Submitting a Pull Request (PR) <a name="submitting-a-pr"></a>

Before you submit your Pull Request (PR) consider the following guidelines:

1. Search [GitHub](https://github.com/dsaidgovsg/govtext-template/pulls) for an open or closed PR that relates to your submission. You don't want to duplicate effort.

2. Be sure that an issue describes the problem you're fixing, or documents the design for the feature you'd like to add.

3. Make your changes in a new git branch:

     ```shell
    > git checkout -b feat--my-feature-name master
     ```
    Branch name needs to be start with one of the following:

    1. feat--*
    2. fix--*
    3. docs--*
    4. ci--*
    5. chore--*
    6. build--*
    7. perf--*
    8. refactor--*
    9. test--*

4. Ensure that the code passes all pre-commit checks and tests before submitting a PR.

    ```shell
    > make pre-commit
    ```

## Commit Message Guidelines <a name="commit-message-guidelines"></a>

To make it easy to adhere to our commit message guidelines, we use a prompt tool built by `commitlint` and it can be accessed by:

```shell
> make commit
```

### Commit Message Format <a name="commit-message-format"></a>

Each commit message consists of a **header**, a **body** and a **footer**.  The header has a special
format that includes a **type**, a **scope** and a **subject**:

```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

The **header** is mandatory and the **scope** of the header is optional.

Any line of the commit message cannot be longer than 100 characters! This allows the message to be easier
to read on GitHub as well as in various git tools.

The footer should contain a [closing reference to an issue](https://help.github.com/articles/closing-issues-via-commit-messages/) if any.

Samples:

```
docs(changelog): update changelog to beta.5
```
```
fix(release): need to depend on latest rxjs and zone.js

The version in our package.json gets copied to the one we publish, and users need the latest of these.
```

### Revert <a name="revert"></a>

If the commit reverts a previous commit, it should begin with `revert(*): `, followed by the header of the reverted commit. In the body it should say: `This reverts commit <hash>.`, where the hash is the SHA of the commit being reverted.

### Type <a name="type"></a>

Must be one of the following:

* **build**: Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm, poetry, docker)
* **ci**: Changes to our CI configuration files and scripts (example scopes: Circle, BrowserStack, SauceLabs)
* **chore**: All other changes like configuration files
* **docs**: Documentation only changes
* **feat**: A new feature
* **fix**: A bug fix
* **perf**: A code change that improves performance
* **refactor**: A code change that neither fixes a bug nor adds a feature
* **test**: Adding missing tests or correcting existing tests

### Scope <a name="scope"></a>

The scope should be the name of the npm package affected (as perceived by the person reading the changelog generated from commit messages).

The following is the list of supported scopes:

* **\***: no specific scope

### Subject <a name="subject"></a>

The subject contains a succinct description of the change:

* use the imperative, present tense: "change" not "changed" nor "changes"
* don't capitalize the first letter
* no dot (.) at the end

### Body <a name="body"></a>

Just as in the **subject**, use the imperative, present tense: "change" not "changed" nor "changes".
The body should include the motivation for the change and contrast this with previous behavior.

### Footer <a name="footer"></a>

The footer should contain any information about **Breaking Changes** and is also the place to
reference GitHub issues that this commit **Closes**.

**Breaking Changes** should start with the word `BREAKING CHANGE:` with a space or two newlines. The rest of the commit message is then used for this.

A detailed explanation can be found in this [document](https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit#).
