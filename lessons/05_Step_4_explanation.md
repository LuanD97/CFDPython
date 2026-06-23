# Step 4 notes: Why forward time, backward space (upwind)

## 1) Why forward differencing in time?

We solve initial value problem (IVP): data known at present time level, unknown at next time level.

At time level $n$, values $u_i^n$ are known. We want $u_i^{n+1}$.

Forward-time difference:

$$
\frac{\partial u}{\partial t}\Big|_i^n \approx \frac{u_i^{n+1} - u_i^n}{\Delta t}
$$

This gives direct marching formula: compute future from present.

Reason chosen in early CFD lessons:

- simple explicit update,
- cheap per step,
- clear numerics,
- stability handled by CFL/time-step limits.

If fully implicit time discretization used, unknowns at $n+1$ appear on both sides; must solve system each step.

---

## 2) Why backward differencing in space for convection term?

For linear convection:

$$
u_t + c\,u_x = 0
$$

If $c>0$, flow moves left $\to$ right. Information at grid point $x_i$ comes from left (upstream).

So use upstream-biased derivative:

$$
u_x(x_i) \approx \frac{u_i - u_{i-1}}{\Delta x}
$$

This is called backward difference in index direction, but physically it is **upwind** when $c>0$.

If $c<0$ (flow right $\to$ left), upstream side is right, so upwind formula switches to:

$$
u_x(x_i) \approx \frac{u_{i+1} - u_i}{\Delta x}
$$

So rule:

- $c>0$ $\Rightarrow$ backward-in-space is upwind,
- $c<0$ $\Rightarrow$ forward-in-space is upwind.

Core meaning of upwind: use side where characteristics come from.

---

## 3) Why this pairing in Step 4 (Burgers)

Typical discretized form:

$$
\frac{u_i^{n+1}-u_i^n}{\Delta t}
+ u_i^n\,\frac{u_i^n-u_{i-1}^n}{\Delta x}
= \nu\,\frac{u_{i+1}^n-2u_i^n+u_{i-1}^n}{\Delta x^2}
$$

Interpretation:

- forward time: march from $n$ to $n+1$,
- backward space in convection term: upwind for positive local velocity,
- central second derivative in diffusion term: symmetric physical smoothing.

For Burgers, convection speed is local ($c=u$), so upwind direction is pointwise:

- if $u_i>0$, use $\frac{u_i-u_{i-1}}{\Delta x}$,
- if $u_i<0$, use $\frac{u_{i+1}-u_i}{\Delta x}$.

---

## 4) One-line memory aid

$$
\text{Time: forward to reach future.}\quad
\text{Convection space: upwind to follow information direction.}
$$
