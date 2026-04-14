# mockapp instructions

## environment
- target Python version: 3.12
- project layout uses `src/`
- package name: `mockapp`
- do not rely on IDE-specific behavior
- do not rely on `PYTHONPATH` hacks
- do not run files by script path when package execution is available

## canonical commands
- install project and test dependency:
  - `python -m pip install -e . pytest`
- run tests:
  - `python -m pytest`
- run application:
  - `python -m mockapp`

## import rules
- application imports must be absolute, starting from `mockapp`
- do not import from `src`
- keep `__init__.py` in real packages
- prefer package/module execution over direct script execution

## pytest rules
- pytest configuration lives in `pyproject.toml`
- keep `--import-mode=importlib`
- tests are under `tests/`

## coding rules for this mock project
- keep changes minimal and explicit
- prefer simple functions over unnecessary abstractions
- when changing behavior, update or add tests
- before finishing, run:
  - `python -m pytest`

## notes for local IDE alignment
- PyCharm may mark `src` as Sources Root for code analysis
- this must not be treated as a runtime dependency
- runtime truth is: virtual environment + editable install + commands above
