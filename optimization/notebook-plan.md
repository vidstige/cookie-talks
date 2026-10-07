# Lecture 3 notebook — the Eye searches for the Ring

The deck stays abstract. This notebook is its companion: one toy problem,
worked in NumPy in the same order as the slides, so that every method in
the lecture is applied in turn to the same objective function. Markdown
cells restate the slide's formula; code cells apply it; each cell ends in
a map with the path drawn on it.

Switch from the deck to the notebook at section boundaries only, four or
five times in the hour. The notebook's headers match the deck's sections
so each switch lands on the right cell.

## The problem

Each Nazgûl senses its distance to the Ring, with noise. The Ring's
position is the unknown. The objective is the sum of squared distance
residuals over all readings. One function, every section acts on it.

## Cells, by section

**I. One dimension, without derivatives.** The Ring is known to be on the
East Road, so the unknown is one number: the distance along the road. One
Nazgûl's reading gives a function of that number. Bracket a minimum, then
bisection, then golden-section search.

**II. Descent directions and step lengths.** Newton in one dimension on
the same function, the derivative written out by hand from the chain
rule.

**III. Several variables.** Drop the road; the unknown is a point on the
map. Steepest descent with a fixed step, then the zig-zag. The zig-zag
appears for a real reason: with all the Nazgûl on one side of the Ring,
the residuals pin down distance well and direction badly, so the bowl is
long and thin. Momentum, per-coordinate step lengths and Newton run on
the identical landscape, and one map shows all four paths.

**IV. Least squares.** Where the problem is at home. Differences of
squared distance readings are linear in the position, the classic
trilateration trick, so linear least squares gives a first estimate.
Gauss–Newton refines it. With the Nazgûl nearly in a line the Jacobian
is ill-conditioned, and Levenberg–Marquardt earns its cell.

**V. The wider landscape.** With two Nazgûl there are two exact
solutions, mirror images across the line joining them: two minima with a
saddle between, on the same function. Multistart from several places on
the map is the global-methods cell. Constrain the Ring to the road again
and the Lagrange picture appears. Finally the readings arrive one at a
time and the estimate moves after each: stochastic gradient descent, and
the hand-off to lecture 4's training loop.

## Implementation notes

- NumPy and matplotlib only. The objective, its gradient and its Jacobian
  are written once and reused by every cell.
- Budget: about 150 lines of code, as for the lecture 4 notebook.
- Nazgûl positions are fixed per cell and chosen to produce the
  pathology that cell is about: one-sided for the zig-zag, nearly
  collinear for Levenberg–Marquardt, two of them for the mirror minima.
- Verify when building that the chosen positions actually produce the
  long thin bowl and the ill-conditioned Jacobian the text claims.
