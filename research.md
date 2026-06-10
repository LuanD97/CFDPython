# Research: Salient topics across CFDPython Jupyter notebooks

## `lessons/01_Step_1.ipynb` — 1D linear convection
- **Core concepts:** Hyperbolic PDE transport, finite differences, explicit time marching.
- **Equation:** \(\partial_t u + c\,\partial_x u = 0\), discrete update \(u_i^{n+1}=u_i^n-c\frac{\Delta t}{\Delta x}(u_i^n-u_{i-1}^n)\).
- **Methods:** Forward-time/backward-space (FTBS), hat-function IC, fixed BC handling.
- **Algorithm:** Nested loops over time/space with temporary array `un=u.copy()`.
- **Experiments:** Grid refinement (`nx`), timestep (`dt`) changes, observe numerical diffusion.
- **Learning objectives:** Build first PDE solver and connect discretization to code.

## `lessons/02_Step_2.ipynb` — 1D nonlinear convection
- **Core concepts:** Nonlinearity from solution-dependent wave speed.
- **Equation:** \(\partial_t u + u\,\partial_x u = 0\), discrete \(u_i^{n+1}=u_i^n-u_i^n\frac{\Delta t}{\Delta x}(u_i^n-u_{i-1}^n)\).
- **Methods:** Same stencil as Step 1, but nonlinear convective coefficient.
- **Algorithm:** Modify Step-1 update line only; reuse full solver scaffold.
- **Experiments:** Parameter sensitivity, profile steepening/distortion.
- **Learning objectives:** See how mild equation change strongly affects numerics/solution behavior.

## `lessons/03_CFL_Condition.ipynb` — convergence/stability study
- **Core concepts:** CFL condition, stability limits for explicit schemes, convergence behavior.
- **Methods:** Wrap Step-1 solver in function, sweep `nx` while keeping `dt` fixed, compare profiles.
- **Algorithm:** Repeated simulation runs under varied discretization.
- **Experiments:** 41/61/71/85+ grid points; demonstrate eventual instability/blow-up when CFL violated.
- **Learning objectives:** Understand why stable timestep must scale with spatial resolution.

## `lessons/04_Step_3.ipynb` — 1D diffusion
- **Core concepts:** Parabolic PDEs, second derivative discretization.
- **Equation:** \(\partial_t u=\nu\partial_{xx}u\), central difference for \(\partial_{xx}u\), update \(u_i^{n+1}=u_i^n+\nu\frac{\Delta t}{\Delta x^2}(u_{i+1}^n-2u_i^n+u_{i-1}^n)\).
- **Methods:** Taylor-series derivation of 2nd-order central stencil; explicit time advance.
- **Algorithm:** Loop over interior nodes (`1..nx-2`), keep boundaries fixed.
- **Experiments:** Viscosity \(\nu\), sigma-based timestep choice, smoothing strength.
- **Learning objectives:** Translate diffusion physics into stable discrete operators.

## `lessons/05_Step_4.ipynb` — 1D Burgers’ equation (periodic)
- **Core concepts:** Convection + diffusion in one PDE; periodic BCs; exact-vs-numerical comparison.
- **Equation:** \(\partial_t u + u\partial_x u = \nu\partial_{xx}u\).
- **Methods:** Combine Steps 2+3 stencils, periodic domain \([0,2\pi]\), analytic IC/solution via transformed \(\phi\).
- **Algorithms/tools:** SymPy symbolic differentiation (`diff`), `lambdify` to numeric function.
- **Experiments:** Compare numerical and analytical curves over time.
- **Learning objectives:** First nonlinear-viscous benchmark with known exact solution.

## `lessons/06_Array_Operations_with_NumPy.ipynb` — vectorization performance
- **Core concepts:** Vectorized array operations vs Python loops.
- **Methods:** Slice-based updates (`u[1:]-u[:-1]`), 2D convection implemented both ways.
- **Algorithm:** Replace nested loops by whole-array stencil updates.
- **Experiments:** `%timeit` benchmark (loop seconds vs vectorized milliseconds-scale).
- **Learning objectives:** Write faster, cleaner CFD kernels using NumPy broadcasting/slicing.

## `lessons/07_Step_5.ipynb` — 2D linear convection
- **Core concepts:** Extend 1D advection to 2D Cartesian grid.
- **Equation:** \(\partial_t u + c\partial_x u + c\partial_y u=0\), backward differences in both directions.
- **Methods:** 2D indexing \((i,j)\), square hat IC in 2D, boundary \(u=1\) on edges.
- **Algorithm:** Time-marching on matrix field, 3D surface visualization.
- **Experiments:** Resolution/timestep effects on transported square pulse.
- **Learning objectives:** Manage multidimensional grids and stencils.

## `lessons/08_Step_6.ipynb` — 2D nonlinear convection (coupled u,v)
- **Core concepts:** Coupled nonlinear transport system.
- **Equations:**
  - \(\partial_t u + u\partial_x u + v\partial_y u = 0\)
  - \(\partial_t v + u\partial_x v + v\partial_y v = 0\)
- **Methods:** Explicit coupled updates for both velocity components.
- **Algorithm:** Simultaneous updates using `un`, `vn` copies; enforce edge BCs \(u=v=1\).
- **Experiments:** Observe coupled wave evolution in 2D.
- **Learning objectives:** Handle multi-field coupling in PDE solvers.

## `lessons/09_Step_7.ipynb` — 2D diffusion
- **Core concepts:** 2D Laplacian diffusion.
- **Equation:** \(\partial_t u=\nu(\partial_{xx}u+\partial_{yy}u)\).
- **Methods:** 5-point stencil, explicit update with `dx`, `dy`, `nu`, sigma-based `dt`.
- **Algorithm:** Vectorized interior update `u[1:-1,1:-1] = ...` plus boundary resets.
- **Experiments:** Run `diffuse(nt)` for varying `nt`; visualize progressive smoothing.
- **Learning objectives:** Implement stable 2D parabolic solver efficiently.

## `lessons/10_Step_8.ipynb` — 2D Burgers’ equation
- **Core concepts:** Full 2D convection-diffusion for \(u,v\), shock-like steepening + viscous smoothing.
- **Equations:** Coupled Burgers with convective and diffusive terms for both components.
- **Methods:** Merge Step 6 convective terms with Step 7 diffusion terms.
- **Algorithm:** Coupled explicit time march on 2D arrays with hat IC for both fields.
- **Experiments:** Track distortion/relaxation of initial square pulse in both velocity components.
- **Learning objectives:** Milestone nonlinear 2D system before pressure-coupled NS.

## `lessons/11_Defining_Function_in_Python.ipynb` — modular coding
- **Core concepts:** Function definitions (`def`), arguments, returns, modular reuse.
- **Methods/examples:** `simpleadd`, `fibonacci`, repeated calls in loops.
- **Algorithms:** Basic iteration inside reusable function blocks.
- **Experiments:** Call functions with different inputs; print sequence outputs.
- **Learning objectives:** Refactor CFD code into maintainable reusable units for later steps.

## `lessons/12_Step_9.ipynb` — 2D Laplace equation
- **Core concepts:** Elliptic PDE, steady-state/equilibrium solve via iteration.
- **Equation:** \(\partial_{xx}p+\partial_{yy}p=0\), five-point central difference operator.
- **Methods:** Iterative relaxation until L1-norm change below tolerance.
- **Boundary conditions:** \(p=0\) at \(x=0\), \(p=y\) at \(x=2\), Neumann \(\partial p/\partial y=0\) at top/bottom.
- **Algorithms:** `laplace2d()` solver + `plot2D()` visualization.
- **Experiments:** Convergence threshold effects, compare with provided analytical series solution.
- **Learning objectives:** Solve steady elliptic problem and introduce convergence criteria.

## `lessons/13_Step_10.ipynb` — 2D Poisson equation
- **Core concepts:** Laplace + source term relaxation dynamics.
- **Equation:** \(\partial_{xx}p+\partial_{yy}p=b\).
- **Methods:** Pseudo-time iterations from zero initial field; zero-Dirichlet boundaries.
- **Experiment setup:** Two source spikes \(+100\) and \(-100\) at quarter/three-quarter domain points.
- **Algorithm:** Iterative stencil update with source forcing; reusable 3D plotting.
- **Learning objectives:** Understand role of source term and pressure-field relaxation behavior.

## `lessons/14_Step_11.ipynb` — 2D incompressible Navier–Stokes cavity flow
- **Core concepts:** Pressure-velocity coupling, momentum + pressure Poisson equation (PPE).
- **Equations:** Discretized \(u,v\) momentum plus PPE derived from continuity constraint.
- **Methods:** Build RHS term `b` for PPE, iterative pressure solve (`nit` inner loop), explicit velocity update.
- **Boundary conditions:** Lid-driven cavity (top lid moving, no-slip elsewhere), mixed pressure BCs.
- **Experiments:** Run many timesteps; visualize velocity vectors/contours and pressure field.
- **Learning objectives:** Assemble full incompressible NS solver from prior building blocks.

## `lessons/15_Step_12.ipynb` — 2D channel flow with Navier–Stokes (periodic)
- **Core concepts:** Pressure-driven channel flow by adding body-force/source \(F\) to \(u\)-momentum.
- **Methods:** Periodic BCs in streamwise direction, wall no-slip in transverse direction, PPE with periodic handling.
- **Algorithms:** `build_up_b`, `pressure_poisson_periodic`, coupled updates for periodic domain until near-steady flow.
- **Experiments:** Observe flow acceleration/establishment under forcing and periodic constraints.
- **Learning objectives:** Final NS variant showing effect of forcing + periodic boundaries.

## Cross-notebook themes
- Incremental reuse: each step composes prior discretization pieces.
- Progression: 1D advection/diffusion → 2D coupled systems → elliptic pressure equations → full incompressible NS.
- Numerical literacy: stability (CFL), consistency of stencils, boundary-condition handling, convergence checks.
- Python literacy: vectorization, modular functions, plotting/diagnostics.
