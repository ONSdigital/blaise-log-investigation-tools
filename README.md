# Blaise Log Investigation Tools 🔎

Python Jupyter Notebook for GCP log investigation.

## Repository Layout

- `src/helpers/` shared helpers
- `notebooks/` focused notebooks

## Setup

1. Use `poetry install` to install the dependencies.
1. Authenticate with GCP using `gcloud auth login`.
1. Set your default GCP project with `gcloud config set project <project-id>`.
1. App authenticate with GCP using `gcloud auth application-default login`.
1. Run `make notebook` to start the notebook server.
	- If port `8888` is already in use (for example after an unclean shutdown), run `make kill` first.
1. In your browser, open the local Jupyter page (usually `http://127.0.0.1:8888/tree`) and choose any notebook from `notebooks/`.

## Linting

- Run `make lint` to run lint checks.
- Run `make lint-fix` to apply auto-fixes and formatting.

## Type Checking

- Run `make typecheck` to run static type checks.
- Type checking is powered by Pyright and configured for strict checking in `pyproject.toml`.

## Testing

- Run `make test` to execute tests.
- Coverage is enforced at 100% for the `helpers` package under `src/`.
- Notebook files are not part of test coverage because coverage is scoped to `helpers`.

## Current Notebooks

`notebooks/warning_and_error_count_by_resource.ipynb`

- Queries Cloud Logging for warning and error entries.
- Supports flexible time windows (`lookback_hours` or explicit start/end timestamps).
- Plots separate warning and error charts by resource type.

`notebooks/error_count_over_time.ipynb`

- Queries Cloud Logging for error entries only.
- Supports flexible time windows (`lookback_hours` or explicit start/end timestamps).
- Plots a scatter chart of error count over time.

`notebooks/nisra_case_updates_over_time.ipynb`

- Queries Cloud Logging for NISRA case update entries.
- Supports flexible time windows (`lookback_hours` or explicit start/end timestamps).
- Plots scatter charts for all entries and subsets containing `opn` and `lms`.

## Contributing Notebooks

- If you create a useful notebook, add it to `notebooks/`.
- Commit and push the notebook so others can reuse and improve it.
- Include a short description in this README under Current Notebooks.
