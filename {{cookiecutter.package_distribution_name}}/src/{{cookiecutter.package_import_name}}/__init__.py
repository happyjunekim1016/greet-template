"""{{ cookiecutter.package_description }}."""


def greet(name: str) -> str:
    """Return a greeting; use 'world' when name is blank."""
    name = name.strip() or "world"
    return f"Hello, {name}!"
