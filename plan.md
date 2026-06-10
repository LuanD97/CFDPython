# Implementation Plan

## Goal
Work through CFDPython notebooks in learning order, validate results at each stage, then refactor stable notebook code into reusable Python package with tests and runnable examples.

## Tasks
1. **Environment + baseline run**
   - File: `README.md`, `requirements.txt`
   - Changes: No repo change. Create local env (`python -m venv .venv` or conda), install deps, launch Jupyter.
   - Acceptance: Can open `lessons/00_Quick_Python_Intro.ipynb`; imports `numpy`, `matplotlib`, `scipy`, `sympy` run without error.

2. **Stage 0: Python/Jupyter prep (if rusty)**
   - File: `lessons/00_Quick_Python_Intro.ipynb`
   - Changes: Execute all cells, tweak 2–3 array/plot params.
   - Acceptance: Understand slicing, loops, plotting; no execution errors.

3. **Stage 1: 1D transport/diffusion core**
   - File: `lessons/01_Step_1.ipynb`, `lessons/02_Step_2.ipynb`, `lessons/03_CFL_Condition.ipynb`, `lessons/04_Step_3.ipynb`, `lessons/05_Step_4.ipynb`
   - Changes: Run in order. Record stable/unstable `dt, dx` combos from CFL notebook. Compare Burgers numerical vs analytical curve.
   - Acceptance: Reproduce expected plots; can explain FTBS update, nonlinear term impact, diffusion smoothing, CFL stability rule.

4. **Milestone mini-project A: 1D solver harness**
   - File: start from `lessons/05_Step_4.ipynb` logic
   - Changes: Build small notebook/script that runs linear convection, nonlinear convection, diffusion, Burgers via shared function signature (`stepper(u, params)` style).
   - Acceptance: One command toggles PDE mode; outputs side-by-side plots + runtime summary.

5. **Stage 2: performance + 2D advection/diffusion**
   - File: `lessons/06_Array_Operations_with_NumPy.ipynb`, `lessons/07_Step_5.ipynb`, `lessons/08_Step_6.ipynb`, `lessons/09_Step_7.ipynb`, `lessons/10_Step_8.ipynb`
   - Changes: First run loop version, then vectorized version; capture speedup. Execute 2D steps in order and verify BC behavior at domain edges.
   - Acceptance: Vectorized kernel faster than loop kernel; 2D fields evolve as expected (transport/steepening/smoothing).

6. **Milestone mini-project B: 2D experiment matrix**
   - File: start from `lessons/10_Step_8.ipynb` logic
   - Changes: Sweep `(nx, ny, dt, nu)` over small grid; log stability + qualitative outcome (diffusive, sharp, unstable).
   - Acceptance: Table/CSV with parameter sets and outcomes; identify safe operating region.

7. **Stage 3: elliptic pressure + full Navier–Stokes**
   - File: `lessons/11_Defining_Function_in_Python.ipynb`, `lessons/12_Step_9.ipynb`, `lessons/13_Step_10.ipynb`, `lessons/14_Step_11.ipynb`, `lessons/15_Step_12.ipynb`
   - Changes: Use function notebook as refactor guide, then run Laplace/Poisson before cavity/channel NS. Track convergence metric (L1 or residual) for pressure solve each case.
   - Acceptance: Cavity and channel cases run end-to-end; pressure iteration converges; velocity/pressure plots physically plausible.

8. **Milestone mini-project C: reproduce canonical CFD cases**
   - File: from Steps 11–12
   - Changes: Reproduce lid-driven cavity and periodic channel with at least 2 grid sizes. Compare centerline velocity trend and convergence behavior across resolutions.
   - Acceptance: Short report with plots + notes on grid sensitivity and solver iteration cost.

9. **Transition notebooks -> reusable package/modules**
   - File: `cfdpython/__init__.py` (new), `cfdpython/grids.py` (new), `cfdpython/boundary_conditions.py` (new), `cfdpython/solvers/advection.py` (new), `cfdpython/solvers/diffusion.py` (new), `cfdpython/solvers/burgers.py` (new), `cfdpython/solvers/poisson.py` (new), `cfdpython/solvers/navier_stokes.py` (new), `cfdpython/plotting.py` (new), `tests/test_solvers.py` (new), `examples/` (new notebooks or scripts)
   - Changes: Extract pure compute kernels from notebooks into functions with explicit inputs/outputs; keep plotting separate; add smoke tests and regression checks (shape, BC enforcement, residual decrease).
   - Acceptance: `pytest` passes for core kernels; example scripts reproduce notebook-equivalent plots with imported package functions.

## Files to Modify
- `plan.md` - engagement plan (this document).
- Future execution artifacts (recommended): `research.md` (append findings), selected notebooks under `lessons/` (execution notes only).

## New Files
- `cfdpython/` package files listed in Task 9 - reusable solver library.
- `tests/test_solvers.py` - automated verification for extracted kernels.
- `examples/` scripts/notebooks - reproducible runs outside teaching notebooks.
- Optional: `docs/roadmap.md` - track stage completion + checkpoint results.

## Dependencies
- Task 2 depends on Task 1.
- Task 3 depends on Task 2.
- Task 4 depends on Task 3.
- Task 5 depends on Task 3 (and benefits from Task 4 abstractions).
- Task 6 depends on Task 5.
- Task 7 depends on Task 5.
- Task 8 depends on Task 7.
- Task 9 depends on Tasks 4–8 (refactor only after behavior verified).

## Risks
- Old pinned versions in `requirements.txt` may conflict with modern Python; use compatible env or relax pins carefully.
- Notebook state/order issues can hide bugs; always `Restart & Run All` before accepting results.
- Explicit schemes unstable if CFL/diffusion constraints violated; checkpoint stability bounds each stage.
- Refactor risk: mixing plotting and solver math. Keep pure numerical kernels isolated to avoid hard-to-test modules.
- Navier–Stokes cases computationally heavier; runtime may require reducing grid for quick checks, then rerun full-size for validation.
