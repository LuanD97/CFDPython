# Why the formulas for $u_{i+1}$ and $u_{i-1}$ around $u_i$ look like that

Context: finite-difference grid in 1D.

- Grid point index: $i$
- Position: $x_i$
- Spacing: $\Delta x$
- Neighbor positions:
  - right neighbor: $x_{i+1} = x_i + \Delta x$
  - left neighbor: $x_{i-1} = x_i - \Delta x$

Goal: express values at neighbors ($u_{i+1}, u_{i-1}$) using value and derivatives at center ($u_i$).

---

## 1) Mental picture first (no equations yet)

Imagine curve $u(x)$. Pick center point at $x_i$.

If you move a tiny step right ($+\Delta x$), function value changes by:

1. slope effect (first derivative),
2. curvature effect (second derivative),
3. higher-shape effects (third derivative, fourth, ...).

If you move same tiny step left ($-\Delta x$), same idea, but odd-direction effects flip sign.

That is whole reason signs differ between $u_{i+1}$ and $u_{i-1}$.

---

## 2) Taylor expansion around center $x_i$

General Taylor series around $x_i$:

$$
u(x_i + h) = u(x_i) + h u'(x_i) + \frac{h^2}{2!}u''(x_i) + \frac{h^3}{3!}u'''(x_i) + \cdots
$$

Set $h = +\Delta x$:

$$
u_{i+1} = u_i + \Delta x\,u_i' + \frac{\Delta x^2}{2}u_i'' + \frac{\Delta x^3}{6}u_i''' + \frac{\Delta x^4}{24}u_i'''' + \cdots
$$

Set $h = -\Delta x$:

$$
u_{i-1} = u_i - \Delta x\,u_i' + \frac{\Delta x^2}{2}u_i'' - \frac{\Delta x^3}{6}u_i''' + \frac{\Delta x^4}{24}u_i'''' - \cdots
$$

Pattern:

- odd powers of $\Delta x$: signs flip ($+,-,+,-$ etc)
- even powers: signs stay same

Reason: $(-\Delta x)^n$ is:

- negative when $n$ odd,
- positive when $n$ even.

---

## 3) Why CFD class uses these two lines so much

Because adding/subtracting them cancels selected terms cleanly.

### Subtract: get first derivative formula

$$
u_{i+1} - u_{i-1} = 2\Delta x\,u_i' + \frac{2\Delta x^3}{6}u_i''' + \cdots
$$

So

$$
u_i' = \frac{u_{i+1}-u_{i-1}}{2\Delta x} - \frac{\Delta x^2}{6}u_i''' + \cdots
$$

Numerical approximation:

$$
u_i' \approx \frac{u_{i+1}-u_{i-1}}{2\Delta x}
$$

Error is $O(\Delta x^2)$, called second-order accurate central difference.

### Add: get second derivative formula

$$
u_{i+1} + u_{i-1} = 2u_i + \Delta x^2 u_i'' + \frac{\Delta x^4}{12}u_i'''' + \cdots
$$

Rearrange:

$$
u_i'' = \frac{u_{i+1}-2u_i+u_{i-1}}{\Delta x^2} - \frac{\Delta x^2}{12}u_i'''' + \cdots
$$

Numerical approximation:

$$
u_i'' \approx \frac{u_{i+1}-2u_i+u_{i-1}}{\Delta x^2}
$$

Also second-order accurate.

---

## 4) Small geometric intuition for sign flips

At center $x_i$:

- If slope $u_i'$ positive, moving right increases $u$, moving left decreases $u$ -> opposite signs.
- Curvature $u_i''$ bends both sides same way near center -> same sign contribution both sides.
- Third derivative measures change of curvature direction -> opposite signs again.

So odd/even derivative contributions alternate sign naturally.

---

## 5) Why this matters for Step 3 (convection update)

In step-style CFD lessons, PDE derivative term (like $\partial u/\partial x$) must become algebraic formula on grid.

Those neighbor expansions justify finite-difference replacement:

- forward, backward, or central derivative formulas
- each with known truncation error order
- stability/accuracy tradeoffs in update equation

So equations for $u_{i\pm1}$ are not random identities. They are local polynomial model of smooth function around $x_i$, then used to derive discrete derivative operators.

---

## 6) Quick visual mnemonic

Think:

$$
\text{neighbor} = \text{center} + (\text{slope term}) + (\text{curvature term}) + \cdots
$$

Right side ($+\Delta x$): slope term positive.

Left side ($-\Delta x$): slope term negative.

Even-order shape terms keep same sign both sides.

That single rule explains both formulas.

---

If useful, next step I can append one section mapping this directly to your exact Step 3 update equation term-by-term.