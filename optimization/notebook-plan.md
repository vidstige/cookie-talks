# Notebook plan

The decks stay abstract and dry. Each lecture from 3 onwards gets a
companion notebook that works one Middle-earth toy problem, in the
same order as the slides. Switch from deck to
notebook at section boundaries only, a few times per hour.

| Lecture | Toy problem | Status |
|---|---|---|
| 3, optimization | The Eye searches for the Ring | decided |
| 4, the perceptron | The Doors of Durin: when the letters shine, where the silver is, what it says | built |
| 5, attention | What's in a name: Elvish names and their meaning | open |

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

**I. One dimension.** The Ring is known to be on a straight road, so the
unknown is one number: the distance along the road. The cost along the road is
bracketed, then narrowed by halving. Its derivative is written out by
hand from the chain rule. Newton's method first solves an equation, where the
road crosses one Nazgûl's circle, then the derivative equals zero.

**II. Least squares.** Drop the road; the unknown is a point on the map.
Differences of squared distance readings are linear in the position, the
classic trilateration trick, so linear least squares gives an estimate in one
solve, with its residual orthogonal to the columns. Gauss–Newton refines it,
and also converges from a poor start.

**III. Several variables.** Every map shows the cost as a heatmap under its
contours. Gradient descent with a fixed step, too long a step, then the
zig-zag. The zig-zag appears for a real reason: with all the Nazgûl on one side
of the Ring, the residuals pin down distance well and direction badly, so the
bowl is long and thin. The Hessian is introduced there, where its eigenvalues
measure that. Adam runs on the identical landscape, and one map shows it with
gradient descent and Gauss–Newton.

The notebook stops there, to save time. Momentum, the wider landscape and
stochastic gradient descent stay on the slides only.
