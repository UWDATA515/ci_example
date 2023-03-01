# Continuous Integration Example Repository

![Build/Test Workflow](https://github.com/UWDATA515/ci_example/actions/workflows/build_test.yml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/UWDATA515/ci_example/badge.svg?branch=main)](https://coveralls.io/github/UWDATA515/ci_example?branch=main)

## GitHub Actions Workflow

In this example repository, we demonstrate how to use GitHub Actions to
perform continuous integration.

Prerequisite: an `environment.yml` file that contains the minimum
necessary packages to run your code. This will be used to create a
virtual environment in the virtual machine that runs your tests on
GitHub's servers.

The workflow configuration is in `.github/workflows/build_test.yml`.
Take a look at that file to see how the workflow itself is built. This
configuration draws heavily from GitHub's guidance on
[Python workflows](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python),
so take a look at the documentation for more details and explanation.

A full guide to GitHub Actions lives in [GitHub's documentation](https://docs.github.com/en/actions).

You can add a build status badge to your README.md by following [these instructions](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge).
That's the little badge that you see at the top of this README! It will
report the main branch's workflow status, so that you can always
immediately see whether main is broken or not.


## Code Coverage

One important aspect of continuous integration is *code coverage*, or
the percentage of your code that is tested ("covered") by your test cases.
There are numerous coverage tools for different programming languages,
but the one we are using in this example is the `coverage` package
(check out its documentation [here](https://coverage.readthedocs.io)).

In order to compute code coverage, you run the tests through the
`coverage` package, and then use it to output a report. That report
can then be uploaded to a website called Coveralls, which specializes
in showing you helpful code coverage diagrams and statistics and tracks
code coverage over time.

In continuous integration, it's good to make sure that you have good
code coverage, and that code coverage doesn't *decrease* when you add
or change code (ie you want to make sure that you write tests for
your code).

After running a workflow that has coverage enabled, go to
https://coveralls.io to see your coverage information! Authenticate
with your GitHub account.

Since we've configured this workflow to run every time a pull request
is created, Coveralls will comment on the corresponding PR with the
code coverage information!

Create a .coveragerc file that specifies what should be included in the coverage calculations, e.g.

```
[report]
omit =  
    *__init__*
    tests/*
exclude_lines =
    if __name__ == .__main__.:
```

In this example, we're excluding the main block lines (hard to test
via unit tests), test files themselves, and `__init__.py` files from
code coverage calculations. If you're doing any heavy lifting in your
`__init__.py`, then you shouldn't remove it from coverage reporting!

If you used this repo as a template and include the workflow steps to
report coverage information to Coveralls, you will also have coverage data that you can get a badge for. To do that, sign in to https://coveralls.io with your GitHub account. On the left hand side select ADD REPOS and flip the slider switch for the repo you want. Look for the box at the bottom of the page labeled BADGE YOUR REPO: CODEBASE and click the EMBED button to get a list of the ways to embed and copy the markdown one and paste it in your README.
