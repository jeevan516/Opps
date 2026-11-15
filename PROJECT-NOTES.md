# Clean Code, OOP & Pydantic: project notes

_Last updated: 15 Nov 2026_

## Project
**Clean Code, OOP & Pydantic.** Hard-to-read Python is costly to maintain. The goal was to
practise turning "bad example" code into clean code: clear names, small functions, classes,
and validated data models, without changing what the code does.

- **Data:** `data/loans.csv`, a small loans table (30 rows, 9 columns: month, amount, borrower,
  term, interest rate, credit score, income, target).
- **Stack:** Python 3.13, pandas, scikit-learn (for the model-training refactor), Pydantic v2;
  Jupyter notebooks; Docker + Docker Compose; GitHub Actions.

## Approach
1. **Refactor variables** (notebook 01, 7 exercises): intent-revealing and pronounceable names,
   one word per concept, named constants instead of magic numbers, DRY column names,
   no mental mapping, regex named groups as explanatory variables.
2. **Refactor functions** (notebook 02, 9 exercises): one helper that trains and scores three
   scikit-learn models instead of copy-pasted code; one task per function; one level of
   abstraction; no side effects or mutated arguments; default arguments; no boolean flags;
   two or fewer parameters.
3. **Object-oriented programming** (notebook 03, 2 exercises): a first class and object, then a
   `BankAccount` class with deposit/withdraw checks and a subclass that overrides `withdraw`.
4. **Pydantic** (notebook 04, 2 exercises): a constrained model, then a `Person` model
   (name up to 50 characters, age 18–120, email pattern) with a `create_person` function.
5. **CI:** a GitHub Actions workflow runs all four notebooks top to bottom on every push and PR.
6. **Docker:** a Dockerfile (locked dependencies, non-root user) and Compose file with a
   JupyterLab service (localhost only, token from `.env`) and a `check` service that runs every notebook.

## Results
| Check | Result |
|---|---|
| Exercises completed | **20** across 4 notebooks (7 + 9 + 2 + 2) |
| CI "Notebooks" workflow, last run (27 Oct 2026) | **4 / 4 notebooks executed without errors** (GitHub Actions, run log) |
| CI history | 2 runs, both passed |
| Notebooks executed locally with saved outputs (15 Nov 2026, same nbconvert command as CI, `python3` kernel) | **4 / 4 ran top to bottom, 0 error cells** |
| Notebook 01: refactored loan summary | `Total loan amount for December: 7200`; price helper prints `117.60` after tax and discount |
| Notebook 02: one `train_model` helper for 3 models | Decision tree, random forest and Gaussian NB each score **100.0%** accuracy, same as the copy-pasted "bad example" (test split is only 6 of 30 rows, so this shows the refactor kept behaviour, not model quality) |
| Notebook 03: `BankAccount` with fee subclass | $100.00 → $150.00 after a $50 deposit → **$128.50** after a $20 withdrawal + $1.50 fee; overdraft raises `Insufficient funds to cover withdrawal and fee` |
| Notebook 04: Pydantic models | bad input to the constrained model caught as **7 validation errors**; invalid `Person` (name over 50 chars, age under 18, bad email) caught as **3 validation errors**; valid `Person` created |
| Automated tests (pytest) | none in the repo; the CI notebook run is the only check |

## Future engineering
- Move the `BankAccount`, `Person` and model-training helpers into a `src/` package with pytest tests.
- Add a linter and formatter (ruff) to CI so style rules are checked, not only that cells run.
- Add type checking (mypy or ty) now that the refactored code has type hints.
- Apply the same refactoring steps to a larger, real notebook (done later in the King County project).

## Update log
- 19 Oct 2026: repository created from the course template.
- 21 Oct 2026: BankAccount OOP exercise completed.
- 23 Oct 2026: refactoring and Pydantic exercises completed; GitHub Actions notebook CI added.
- 27 Oct 2026: Dockerfile, Docker Compose (JupyterLab + notebook check) and README run guide added.
- 15 Nov 2026: project notes created.
- 15 Nov 2026: executed all 4 notebooks in place (same nbconvert command as CI) so outputs are saved in the repo; results added above.
