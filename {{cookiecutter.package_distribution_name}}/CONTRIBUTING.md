# Contributing to {{ cookiecutter.package_distribution_name }}

## Set up for development

```bash
python -m pip install -e .
```

## Run the tests

```bash
python -c "from {{ cookiecutter.package_import_name }} import greet; print(greet('Hee'))"
```

Expected output: `Hello, Hee!`

## Send a change

1. Create a branch from `main` and commit your change.
2. Push the branch.
3. Open a pull request into `main`.
