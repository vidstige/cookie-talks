# Notebook plan

The decks stay abstract and dry. Each lecture from 3 onwards gets a
companion notebook that works one Middle-earth toy problem, told from
Sauron's side, in the same order as the slides. Switch from deck to
notebook at section boundaries only, a few times per hour.

| Lecture | Toy problem | Status |
|---|---|---|
| 3, optimization | The Eye searches for the Ring | decided |
| 4, the perceptron | Something with the Palantíri, perhaps screen time | open |
| 5, attention | Tolkien names, or words of the Black Speech | open |

**On the Palantíri.** The mechanics of the stones — their fixed
orientation, the bearing a stone must be turned to, who is looking at
the other end — make a geometry problem, not a good match for a
perceptron. A perceptron toy needs labels whose hidden truth the room
cannot write down as a rule or a formula. Screen time is the leading
candidate: the Mouth logs the Dark Lord's hours on the stone and the
number of hobbits glimpsed, and predicts whether tomorrow is a bearable
day for the staff.

## Lecture 3 — the Eye searches for the Ring

Each Nazgûl senses its distance to the Ring, with noise. The Ring's
position is the unknown. The objective is the sum of squared distance
residuals over all readings. One function, every section acts on it.

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
