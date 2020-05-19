module.exports = {
  extends: ["@commitlint/config-conventional"],
  rules: {
    "header-max-length": [2, "always", 100],
    "type-enum": [2, "always", [
        "build",
        "ci",
        "chore",
        "docs",
        "feat",
        "fix",
        "perf",
        "refactor",
        "revert",
        "test",
      ]
    ],
    "scope-empty": [2, "never"],
    "scope-enum": [2, "always", [
        "*",
      ]
    ],
    "subject-empty": [2, "never"],
  }
};
