# Step 4 — Periodic Boundary section breakdown

Source: `lessons/05_Step_4.ipynb` → **Periodic Boundary Conditions** block.

## Big picture

Burgers update at grid point `i`:

\[
 u_i^{n+1} = u_i^n
 - u_i^n\frac{\Delta t}{\Delta x}(u_i^n-u_{i-1}^n)
 + \nu\frac{\Delta t}{\Delta x^2}(u_{i+1}^n-2u_i^n+u_{i-1}^n)
\]

Two indices, two meanings:

- `i` = space index (position on x-grid)
- `n` = time index (time step)

So:

- `u_i^n` = value at point `i`, old time
- `u_i^{n+1}` = value at point `i`, next time
- `u_{i+1}^n` = value at right neighbor, old time

---

## Your exact question

> what does `u_n(i+1)` mean when `u_i` already at end frame?

At right edge, periodic BC says domain wraps.

Meaning:

- right neighbor of last physical point = first physical point
- mathematically: `u(x=2π,t) = u(x=0,t)`

So `i+1` past right edge is not "out of bounds" physically. It maps to front of domain.

---

## How notebook code handles this

```python
for i in range(1, nx-1):
    ... use un[i+1], un[i-1]

u[0] = ... (un[0] - un[-2]) ... (un[1] - 2*un[0] + un[-2])
u[-1] = u[0]
```

### Nuance 1: why special update for `u[0]`

`u[0]` needs left neighbor. Periodic left neighbor of `x=0` is `x=2π-Δx`.
In array with duplicated endpoint, that index is `-2`.

So `un[-2]` used, not `un[-1]`.

### Nuance 2: why `u[-1] = u[0]`

Grid built with:

```python
x = linspace(0, 2*pi, nx)
```

This includes both endpoints `0` and `2π`.
Those are same physical location for periodic domain.

So last entry `u[-1]` is enforced equal to first entry `u[0]`.

### Nuance 3: where `u_{i+1}` at edge actually appears

In interior loop, max `i` is `nx-2`.
Then `i+1 = nx-1`, valid index.
And because previous step enforced `u[-1]=u[0]`, this acts like wrapped neighbor.

---

## Why `un = u.copy()` matters

Notebook does:

```python
un = u.copy()
```

Then computes all new `u[...]` from old `un[...]`.

If you skip copy, early updated cells contaminate later cells in same time step. Scheme changes unintentionally.

---

## Mental model

Think ring, not line.

- right edge connected to left edge
- no true "end"
- neighbor queries use modulo behavior conceptually

Equivalent conceptual form:

- left neighbor index: `(i-1) % (nx-1)`
- right neighbor index: `(i+1) % (nx-1)`

(`nx-1` because last point duplicates first in this notebook setup.)

---

## Common confusion: `u_i^{n+1}` vs `u_{i+1}^n`

- `u_i^{n+1}`: same position, next time
- `u_{i+1}^n`: next position, same time

Subscript shift = space move.
Superscript shift = time move.

Different shifts. Easy mix-up.

---

## One-line answer

When `i` at domain end, `u_{i+1}^n` means wrapped point at domain start because periodic boundary condition identifies right edge with left edge.
