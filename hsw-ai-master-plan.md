# How Stuff Works: AI from scratch — master plan

Five lectures of one hour. They build on each other and are meant to be taken in order:
each one uses what the ones before it established. No prerequisites beyond arithmetic and
a willingness to look at notation.

This document specifies the structure of the series: the slide sequence of each lecture,
the mathematical arc it follows, and the dependencies between lectures. It does not
specify slide content. Visual and editorial style are in the appendix.

---

## How to use this document

Paste this file as a prompt and name a lecture:

> Build lecture 1 from this plan.

The builder is expected to:

1. Produce one self-contained HTML file per lecture. No build step; it opens by
   double-clicking.
2. Follow Appendix A exactly. The five decks must read as one series.
3. Follow *Presentation style* below exactly. It is the rule a first draft is most likely
   to break, and the most expensive one to repair afterwards.
4. Write the mathematical content for each slide listed below, at the level of a first
   encounter, together with speaker notes on every slide. Most of the writing goes in the
   notes.
5. Verify anything a slide asserts numerically: figure geometry, worked arithmetic,
   internal slide references.
6. Not add topics beyond the sequences below without asking — and say which listed topics
   were dropped, so this document can be brought back in line.

---

## Time model

| | |
|---|---|
| Material | 45 min |
| Quiz | 5 min, at the end |
| Questions and overrun | 10 min |

Budget in *concepts*, not in slides. Lecture 1 as delivered carries about twenty
concepts across twenty-two material slides, and runs the full 45 minutes. A slide
holding one short list and one figure costs well under two minutes; a slide with a
slider the room wants to play with costs four. Count the sliders and the load-bearing
slides first, then fill the rest in around them.

Slide count is therefore a consequence, not a target. Splitting one crowded slide into
three plain ones costs no extra time — the same words get said either way — so split
freely. There is no recap slide: the quiz serves that purpose and gets a response from
the room rather than a nod.

## Structure common to every lecture

| Slide | |
|---|---|
| 1 | Title. Lecture title only. |
| 2 | The series. Its subject, its five parts, and where this one sits in them. |
| 3 | Outline of this lecture. Its sections, in order. |
| 4 … | Material. |
| | Quiz — a title slide, then one slide per question. |
| | Questions? |
| | Thank you, naming what the next lecture does. |

Slide 2 is the same slide in all five decks, with the current lecture marked. It says
what each lecture needs from the ones before it, in a few words per lecture. Slide 3
differs per lecture and lists the section headings given below.

The quiz is multiple choice, four questions, four options each, one question per slide
so the room reads one thing at a time. Answers are hands up rather than paper, and the
answer with its reasoning lives in that slide's speaker notes — including what each
wrong option is a trap for. Pick distractors that are plausible mistakes, not filler.

## Presentation style

*The slide is not the script.*

A slide carries, at most, a heading, an optional one-line italic `.sub`, a short list or
a displayed equation, one `.claim`, and a figure with its caption. Three or four bullets,
each a fragment rather than a sentence. As a number to steer by: lecture 1 as delivered
averages 35 words of on-slide text per slide, and the draft that had to be rewritten
averaged 113.

Everything else is spoken, and everything spoken is written down in the speaker notes:
the derivation, the worked arithmetic, the caveat, the aside, the demonstration to run,
the forward reference. Notes run long on purpose — roughly a hundred words a slide — and
they are the place a sentence goes when it is true, worth saying, and would crowd the
slide. If prose is on the slide, the audience reads it instead of listening.

Interactive figures carry one idea and one cluster of controls. A segmented control that
switches a figure between four unrelated transforms is a slide doing four jobs; give
each its own slide and its own slider. Every such figure needs a resting state that
reads correctly before anything is touched.
---

# Lecture 1 — Vectors, bases and linear maps

**Status: delivered.** The table below is the deck as it stands, not a proposal. Where
lectures 2–5 still read as plans, this one reads as a record.

**Arc.** Vectors come first as geometric objects, then as coordinates in an arbitrary
basis — skewed, unlovely — and only then as coordinates in a square one, presented as a
choice rather than as what coordinates are. Length and the inner product arrive after
that, turning right angles into a number. Matrices appear where they are actually needed:
a system of linear equations, written \(Ax = b\). That gives the matrix–vector product a
reason to exist before it is given a name, and substituting one system into another gives
the matrix product, its non-commutativity and the identity. Only then is a matrix reread
as a transformation of space, at which point its columns are recognised as the images of
the basis vectors and a whole figure can be pushed through one. Two decompositions close
the lecture, briefly.

**Why this ordering.** A matrix introduced as a transformation has to carry an arithmetic
nobody asked for. A matrix introduced as the bookkeeping of a linear system has that
arithmetic forced on it: multiplication is what substituting one system into another does,
the identity is the system that changes nothing, the inverse is the system run backwards.
The transformation reading then arrives as a reinterpretation of something already
familiar, which is the one moment in the lecture worth spending real time on.

| # | Slide | |
|---|---|---|
| 1 | Vectors, bases and linear maps | |
| 2 | The series | |
| 3 | Outline | |
| | **I. Vectors** | |
| 4 | Vectors as geometric objects | |
| 5 | Addition, scalar multiplication and linear combinations | |
| 6 | Coordinates in a basis | drag |
| 7 | Orthogonality | |
| 8 | Cartesian coordinates | |
| 9 | The norm | |
| 10 | The inner product | |
| 11 | Orthogonal projection | |
| | **II. Linear systems** | |
| 12 | Systems of linear equations | |
| 13 | The matrix product | click |
| 14 | The transpose | click |
| 15 | The identity matrix | |
| 16 | The inverse | |
| | **III. Basis vectors and transforms** | |
| 17 | Matrices as linear transformations | |
| 18 | The columns of a matrix are the images of the basis vectors | drag |
| 19 | Rotation | slider |
| 20 | Scaling | slider |
| 21 | Shear | slider |
| 22 | Translation is the odd one out | slider |
| 23 | Combining transforms | slider |
| | **IV. Matrix decomposition** | |
| 24 | Eigenvalues and eigenvectors | |
| 25 | LU | |
| | **V. Quiz** | |
| 26 | Quiz | |
| 27 | What is \(u \cdot v\)? | |
| 28 | Which picture is *not* a linear map? | |
| 29 | A map sends \(e_1 \mapsto (0,1)\) and \(e_2 \mapsto (-2,0)\). What is its matrix? | |
| 30 | What is an eigenvector of a matrix \(A\)? | |
| 31 | Questions? | |
| 32 | Thank you | |

Thirty-two slides, nine of them interactive. That is not a slide count anyone should
copy; it is what twenty concepts look like once no slide holds two of them. The five
transform slides, 19 to 23, were one slide with a segmented control in the plan and are
now the part of the hour that works best.

**Coordinates are given twice, and that is the point.** Slide 6 defines coordinates
against an arbitrary basis: two draggable vectors off a common line, weights that exist
and are unique, a grid that is not square. Slide 7 asks what right angles buy — each
coordinate readable on its own, by a perpendicular drop rather than by a line parallel to
the other basis vector — and only slide 8 adds a common step and calls the result
Cartesian, presenting it as a *choice*. Slides 9 and 10 then turn length and the right
angle into numbers.

The ordering here was corrected during drafting: the plan originally put the square
frame before orthogonality. Orthogonality first is better, because the square frame is
then the answer to a question the room has already been asked.

Nothing in slides 4–8 may use length, which is not defined until slide 9. A Cartesian
basis is therefore described on slide 8 as one vector together with its quarter turn,
which fixes the step without measuring anything, and slide 10 states plainly that the
coordinate formula for the inner product is reading a Cartesian frame.

**The matrix–vector product has no slide of its own.** It is introduced on slide 12 as
the notation the system forces — entry \(i\) of \(Ax\) is row \(i\) of \(A\) against
\(x\), which is the left-hand side of equation \(i\) — with the column reading,
\(Ax = x_1a_1 + x_2a_2\), named in the notes. A separate slide for it repeated the
systems slide and was dropped.

**Elimination is deliberately absent.** How a system is actually solved — elimination,
pivoting, rank, the null space, the conditions for existence and uniqueness — is skipped.
The inverse slide says only that the inverse undoes the system, that not every matrix has
one, and that forming it is not how software solves anything; the LU slide says what
software does instead.

**Span, independence, basis and dimension are absent too.** They were slides 15 and 16 of
the plan and were cut in drafting: every use they had was already carried by a picture.
"Two vectors off a common line" does the work of independence on the coordinates slide,
and dragging one column arrow onto the other does the work of rank deficiency on the
draggable-arrows slide. Restoring them is the first thing to reconsider if the hour ever
comes in short.

**The logo.** Slide 17 is the first appearance of the Volumental logo, as a point cloud
pushed through a transformation. It recurs throughout section III and in section IV. It
must not appear before slide 17 — in particular not on the title slide, whose figure is
one arrow measured against two frames — so that its arrival coincides with the
reinterpretation it illustrates.

**The transforms are one slider each.** Rotation, scaling, shear, translation and the
composition of two of them get a slide apiece, each with its own figure, its own controls
and a live matrix readout. An earlier draft put all four behind one segmented control on
one slide; splitting them is the single largest improvement in the deck. Reflection is a
remark on the scaling slide — a negative scale — rather than a slide. Scaling sliders
reach zero, so the figure can be collapsed onto a line deliberately; that collapse is
this deck's only account of a matrix that cannot be undone, and it is reached again by
dragging on slide 18. Sliders must not advance the deck; see Appendix A.

**Determinants are not covered at all.** The plan had a live determinant readout on the
transforms slide. It was cut: a number nobody can yet interpret is noise, and the two
things it was there to show — area scaling and the collapse to a line — are both visible
in the figure. The readouts show the matrix itself, and \(Q^{\mathsf T}Q = I\) on the
rotation slide.

**Cut candidates — to confirm after the next delivery.** The deck as it stands carries no
per-slide cut guidance; the plan's rule that every slide says what to drop if time is
short was not followed, and the honest reason is that the timing is not known yet. On
paper the order is 25 (LU), 14 (the transpose), 21 (shear). Slides 6, 7 and 8 are not cut
candidates: they are the sequence the rest of the lecture reads coordinates through.
Slide 18 is not a cut candidate at any price.

**Forward dependencies.** Slide 10 (the inner product) is reused in lecture 5 for
attention scores. Slide 11 (projection) is reused in lecture 3 for least squares. Slide 16
(the inverse) is reused in lecture 3 for the normal equations. The homogeneous coordinates
of slides 22 and 23 are reused in lecture 4 for the bias term. Slide 24 (eigenvalues) is
reused in lecture 3 for the condition number.

Lecture 5 wanted orthonormal bases for multi-head projections, and this deck no longer
has a change-of-basis slide to point at. Orthogonality (7), Cartesian coordinates (8) and
the orthogonality of a rotation (19) are what is available; lecture 5 must build the rest
itself or accept the gap.

**Not covered, deliberately:** elimination and the solution of systems in any form; span,
independence, basis and dimension as named concepts; rank and the null space;
determinants; change of basis and similar matrices; eigendecomposition; the SVD; the
QR/Cholesky family; inner products other than the Cartesian one; general metrics;
Gram–Schmidt; complex eigenvalues beyond a caveat.

---

## A note on lectures 3–5

Their tables below were written before lecture 1 was built, at the old granularity: one
line per topic, several topics to a slide, twenty-three slides to a deck. Read them as
lists of *concepts in order*, not as slide sequences. Expect each to split into thirty or
so slides once the presentation-style rules above are applied, and renumber the
cross-references in this document when it happens. Lecture 2 has been rewritten at the
new granularity and no longer needs this caveat.

---

# Lecture 2 — Basic calculus

**Status: plan, revised.** Slimmed against what lectures 3 and 4 actually consume; see
*What was cut* below. Written at one concept per line, so the table is close to the slide
sequence rather than a topic list.

**Arc.** The derivative is presented as the coefficient of the best local linear
approximation, from which a handful of rules and the chain rule follow. The second
derivative gives curvature and the quadratic approximation, which is as far as expansion
goes. The same construction is then carried into several variables: partial derivatives,
gradient, directional derivative, Jacobian, Hessian, and the chain rule as a product of
Jacobians. The lecture closes on how a derivative is actually obtained: by hand, by
difference quotient, or automatically — with forward mode worked and its cost stated, so
that lecture 4 has a reason to want reverse mode.

| # | Slide | |
|---|---|---|
| 1 | Basic calculus | |
| 2 | The series | |
| 3 | Outline | |
| | **I. The derivative in one variable** | |
| 4 | Rates of change and the difference quotient | |
| 5 | The derivative as best local linear approximation | slider |
| 6 | Differentiation rules | |
| 7 | The chain rule | slider |
| | **II. Local behaviour** | |
| 8 | Stationary points | |
| 9 | The second derivative | |
| 10 | The quadratic approximation | slider |
| | **III. Several variables** | |
| 11 | Functions of several variables | |
| 12 | Partial derivatives | |
| 13 | The gradient | drag |
| 14 | Directional derivatives | slider |
| 15 | The Jacobian | |
| 16 | The Hessian | |
| 17 | The chain rule in several variables | |
| | **IV. Obtaining derivatives** | |
| 18 | By hand, by difference quotient, by program | |
| 19 | Numerical differentiation and the step size | slider |
| 20 | Forward-mode automatic differentiation | |
| 21 | The cost of forward mode | |
| | **V. Quiz** | |
| 22 | Quiz | |
| 23–26 | Four questions | |
| 27 | Questions? | |
| 28 | Thank you | |

Eighteen material slides, six of them interactive, against twenty-two in lecture 1. The
budget is deliberately below lecture 1's: three of the slides — 5, 7 and 13 — are
load-bearing for the rest of the series and should get the time the cut material frees.

**What each later lecture takes from here.** Lecture 3 needs the gradient (13) and the
directional derivative (14) for descent directions and line search; the stationary-point
condition (8) as the thing an algorithm searches for; the second derivative (9), the
quadratic approximation (10) and the Hessian (16) for Newton's method and for
conditioning; the Jacobian (15) and the chain rule (7) for Gauss–Newton. Lecture 4 needs
the chain rule in several variables (17) — that is the whole of backpropagation — and the
cost of forward mode (21) as the reason reverse mode exists. Lecture 5 needs nothing
beyond what lecture 4 already uses. Every slide in the table is on that list or is the
step immediately before one that is.

**The limit has no slide of its own.** Slide 4 writes the difference quotient and says
"as \(h\) shrinks"; slide 5 shows it on a slider. That is the whole treatment. No
epsilon-delta argument, no discussion of when the limit fails to exist beyond a remark
that a corner has no tangent.

**The rules are one slide.** Sum, scalar multiple, power and exponential, in a short
table, because those are the ones the later lectures differentiate. Product and quotient
rules are named in the notes as existing and are not used anywhere in the series; sine and
cosine likewise. The chain rule gets its own slide because it is the one that matters.

**Expansion stops at degree two.** Taylor polynomials as a topic were cut. What lecture 3
needs is the quadratic model \(f(x+h)\approx f(x)+f'(x)h+\tfrac12 f''(x)h^2\), and that is
slide 10, presented as "the linear approximation, plus curvature". The general series, its
remainder and its convergence are not mentioned. Slide 16 does the same in several
variables with the Hessian, and that is the second-order expansion lecture 3 uses.

**The chain rule in several variables is Jacobians multiplied.** Slide 17 says the
derivative of a composition is the matrix product of the Jacobians, which is the matrix
product from lecture 1 read as "rates compose". Backpropagation in lecture 4 is this slide
evaluated in a particular order; say so.

**Obtaining derivatives stays here, and closes the deck.** Slide 18 names the three
routes. Slide 19 revisits the difference quotient with a finite \(h\) and shows the
trade-off between truncation and cancellation on a slider — that is the floating block
of the earlier plan, collapsed to one slide and settled here rather than in lecture 3.
Slide 20 carries (value, derivative) pairs through the rules of slide 6 and the chain
rule of slide 7, so that forward mode is seen to be the chain rule made mechanical.
Slide 21 states the cost: one pass per input, which a function of a million parameters
and one output cannot afford. Reverse mode is named as the fix and left for lecture 4.

**Coordination note.** Slide 8 states the condition \(f' = 0\) at stationary points as a
fact about local behaviour. Lecture 3 does not restate it as a definition; it arrives at
the same condition as the thing an algorithm searches for.

**Cut candidates, in order:** 21 (say the cost in a sentence on slide 20), 19, 12
(define partials on the gradient slide). Slides 5, 7 and 13 are not cut candidates.

**Forward dependencies.** Slide 5 (linear approximation) is the picture lecture 3 uses
for every descent step. Slide 7 (chain rule) is the whole of backpropagation in
lecture 4. Slide 13 (gradient) and slide 16 (Hessian) are the objects lecture 3
manipulates. Slide 21 (cost of forward mode) is the reason lecture 4 needs reverse mode.

**What was cut, and why.** The limit as a slide (folded into 4 and 5); product and
quotient rules (named, not taught; unused later); higher derivatives beyond the second
and Taylor polynomials as a topic (replaced by the quadratic approximation, which is all
lecture 3 needs); the second-order expansion as a slide separate from the Hessian
(merged into 16). Restoring Taylor polynomials is the first thing to reconsider if the
hour comes in short, since they are the natural continuation of slide 10.

**Not covered, deliberately:** integration; series, convergence and the Taylor remainder;
multivariable integration; differential equations; any epsilon-delta argument; implicit
differentiation; reverse-mode differentiation (lecture 4).

---

# Lecture 3 — Numerical optimization

**Arc.** A sequence of algorithms of increasing sophistication for finding the argument
that minimizes a function. It begins in one dimension with comparisons only and no
derivatives, then introduces the descent-direction-plus-line-search pattern that every
later method instantiates. First derivatives enter with Newton's method, second
derivatives later. Least squares is treated twice, algebraically and geometrically. The
lecture closes on the wider landscape: the pathologies that defeat local methods, and
two directions — global search and constrained problems — named so that the boundary of
what has been covered is visible.

| # | Slide |
|---|---|
| 1 | Numerical optimization |
| 2 | The series |
| 3 | Outline |
| | **I. One dimension, without derivatives** |
| 4 | The minimization problem |
| 5 | Bracketing a minimum |
| 6 | Bisection and golden-section search |
| | **II. Descent directions and step lengths** |
| 7 | Descent directions and line search |
| 8 | Newton's method in one dimension |
| | **III. Several variables** |
| 9 | Steepest descent |
| 10 | Fixed step lengths |
| 11 | Conditioning and the zig-zag |
| 12 | Momentum |
| 13 | Per-coordinate step lengths |
| 14 | Newton's method in several variables |
| | **IV. Least squares** |
| 15 | Linear least squares and the normal equations |
| 16 | Least squares as orthogonal projection |
| 17 | Nonlinear least squares and Gauss–Newton |
| 18 | Levenberg–Marquardt and trust regions |
| | **V. The wider landscape** |
| 19 | Stationary points, local minima, saddle points, plateaus |
| 20 | Global methods, in brief |
| 21 | Constrained optimization, in brief |
| 22 | Stochastic gradient descent |
| 23 | Quiz |

Slide 11 uses the eigenvalues of the Hessian; slide 16 uses orthogonal projection. Both
are recalled in a sentence, with a pointer back to the slide in lecture 1 that established
them — by name, "the eigenvalues slide" and "the projection slide", not by number.

Slides 20 and 21 are one slide each and are meant to stay that way. Slide 20 follows
directly from slide 19: every method in this lecture finds a local minimum, so the
question of how one searches globally has to at least be named — grid and random search,
multiple starts, simulated annealing, population methods. Slide 21 marks the other
boundary: the whole lecture has assumed the argument may be anything at all, and the
moment it may not, the subject changes. State the feasible set, mention that equality
constraints are handled by Lagrange multipliers and inequalities by the KKT conditions,
and stop there.

**Cut candidates, in order:** 18, 13, 12. Slides 20 and 21 are already minimal and
should not be shortened further; they exist to show where the subject continues.

**Not covered, deliberately:** Lagrange multipliers and the KKT conditions worked through
rather than named, linear and convex programming, conjugate gradients, BFGS and the
quasi-Newton family in any detail, and the global methods of slide 20 beyond a list.

---

# Lecture 4 — The multilayer perceptron

**Arc.** The object first, the training second. A multilayer perceptron is defined as a
parametric family of functions built by alternating affine maps with a fixed
nonlinearity, and the necessity of that nonlinearity is established before it is
introduced. XOR provides a network whose weights can be chosen by hand, which motivates
the second half: choosing them by minimization instead. A single toy problem in the plane
carries the training material, with an accompanying notebook.

| # | Slide |
|---|---|
| 1 | The multilayer perceptron |
| 2 | The series |
| 3 | Outline |
| | **I. The network** |
| 4 | A parametric family of functions |
| 5 | A composition of linear maps is linear |
| 6 | The affine layer and the activation function |
| 7 | Activation functions |
| 8 | The multilayer perceptron |
| 9 | The forward pass, and batches |
| 10 | XOR and the limits of one layer |
| 11 | A network with weights chosen by hand |
| | **II. Training** |
| 12 | A toy problem in the plane |
| 13 | Loss functions |
| 14 | Squared error and cross-entropy |
| 15 | Training as minimization over the parameters |
| 16 | Many parameters, one scalar output |
| 17 | Reverse-mode differentiation |
| 18 | Backpropagation for a two-layer network |
| 19 | The training loop |
| 20 | Initialization and step length |
| 21 | Overfitting and validation |
| 22 | What a multilayer perceptron cannot do |
| 23 | Quiz |

**Toy problem.** Two interleaving classes in the plane, so that the decision boundary can
be plotted and watched during training. Introduced at slide 12 and used for everything
after it.

**Notebook.** A separate `.ipynb`, built with the deck. NumPy only, no framework, so
nothing is hidden: dataset, explicit forward pass, explicit backward pass matching slide
18, training loop plotting the boundary periodically, and a set of deliberate breakages
to run (zero initialization, step length far too large, nonlinearity removed). Under
about 150 lines of code.

**Slide 14 carries an admission.** Cross-entropy has a probabilistic justification that
this series does not supply. Say so on the slide rather than implying the choice is
arbitrary.

**No notation slide.** Symbols are introduced where first needed.

**Not covered, deliberately:** convolutional and recurrent architectures, normalization
layers, dropout beyond a remark, hyperparameter search, anything about scale.

---

# Lecture 5 — The attention mechanism

**Arc.** The problem is stated first: variable-length sequences in which every position
must consult the others, which a fixed-width network cannot express. Attention is then
built in stages — mixing with fixed weights, then with content-dependent weights, then
with weights obtained from inner products — so that the final formula assembles from
parts already justified. The transformer block, residual connections and stacking follow.
The lecture closes by returning to invariance.

| # | Slide |
|---|---|
| 1 | The attention mechanism |
| 2 | The series |
| 3 | Outline |
| | **I. The problem** |
| 4 | Sequences of variable length |
| 5 | Why a fixed-width network cannot do this |
| 6 | From tokens to vectors |
| | **II. Constructing attention** |
| 7 | Mixing with fixed weights |
| 8 | Content-dependent weights |
| 9 | Queries, keys and values |
| 10 | Scores as inner products |
| 11 | Scaling by the square root of the dimension |
| 12 | The softmax |
| 13 | The attention operation |
| 14 | A worked example |
| | **III. Variants and structure** |
| 15 | Self-attention and cross-attention |
| 16 | Causal masking |
| 17 | Multi-head attention |
| 18 | Permutation invariance and positional encoding |
| | **IV. The transformer** |
| 19 | The transformer block |
| 20 | Residual connections |
| 21 | Stacked blocks, logits and sampling |
| 22 | Invariance revisited: inner products and linear maps |
| 23 | Quiz, and what this series did not cover |

Slide 22 is the closing argument of the series: the coordinates of a learned vector carry
little meaning individually, and the operations a transformer is built from — linear maps
and inner products — are precisely those that do not depend on a choice of basis.

**Cut candidates, in order:** 20, 16, 14.

**Not covered, deliberately:** encoder-decoder architectures in detail, tokenization,
attention-cost reductions, pretraining and fine-tuning procedure, everything after the
architecture.

---

# Open questions for the series

**Probability.** Cross-entropy in lecture 4 and the softmax in lecture 5 both rest on
probability the series never develops. The current decision is to acknowledge the gap on
the slide and continue. A sixth lecture on probability, expectation and likelihood is the
obvious extension if there is appetite.

**Numerical differentiation.** Settled: it is one slide at the end of lecture 2, together
with forward-mode automatic differentiation, so that lecture 3 may assume derivatives are
available and lecture 4 only has to add reverse mode.

**Load-bearing slides.** If any of these does not land, later lectures suffer: in
lecture 1, the inner product (10) and the columns of a matrix as the images of the basis
vectors (18); then 2/5 (the derivative as linear approximation), 2/7 (the chain rule),
2/13 (the gradient), 3/7 (descent direction and line search), 4/5 (a composition of
linear maps is linear), 5/10 (scores as inner products). The lecture 3–5 numbers are at
the old granularity and will move.

---

# Appendix A — Style specification

## Palette

Black on white, print-like. Colour is confined to figures and code.

```css
:root{
  --paper:#ffffff;
  --ink:#000000;        /* body text, headings, structural rules */
  --ink-2:#3f4750;      /* subtitles, speaker notes */
  --ink-3:#767f89;      /* captions, dim asides, top rail */
  --rule:#dcdfe3;       /* hairlines, panel borders */
  --grid:#eceef1;       /* graph-paper background */

  --madder:#a4402c;     /* FIGURES: the object under discussion */
  --prussian:#1c4e73;   /* FIGURES: first frame of reference, axes, basis one */
  --verdigris:#2b6f68;  /* FIGURES: second frame, or a result */
  --construct:#c3c9cf;  /* FIGURES: scaffolding — grids, helpers, right angles */

  --code-bg:#f7f7f5;
  --code-fg:#252a30;
  --code-comment:#8a9199;   /* italic */
  --code-key:#1c4e73;       /* weight 500 */
  --code-lit:#2b6f68;

  --stage-w:1280px;
  --stage-h:720px;
}
```

Each figure colour holds one fixed meaning across all five decks: madder for the object
under discussion, prussian for the first frame of reference, verdigris for a second frame
or a result, construct for scaffolding. Anything coloured means something, and the
caption says what. No colour for variety.

## Typography

Spectral (weights 300, 400, 500, 600, italic 400) for prose; its serif sits with KaTeX's
Computer Modern rather than against it. JetBrains Mono (400, 500) for code, figure
labels, captions and the top rail. KaTeX supplies the mathematical typeface.

| Element | Size / weight |
|---|---|
| `h1`, title slide | 68px / 600, line-height 1.04, tracking −.02em |
| `h2`, all others | 41px / 600, line-height 1.13, tracking −.015em |
| `.sub` | 21px italic, `--ink-2` |
| `p` | 22px / 400, line-height 1.55, max-width 64ch |
| `li` | 23px, line-height 1.5, max-width 52ch |
| `.eq` | 20px |
| `.claim` | 25px, line-height 1.38 |
| `figcaption` | 13px mono, `--ink-3` |
| `.rail` | 12.5px mono, `--ink-3` |
| `pre` | 17px mono |

## Layout

A fixed 1280×720 logical slide, scaled by CSS transform to the viewport, so layout is
identical on any projector. Padding `62px 80px 70px`.

A top rail at 26px carries the section name at left and `n / total` at right, above a 1px
hairline. It is generated in JS from a `data-where` attribute.

A 48px graph-paper grid in `--grid` sits behind the stage.

Column grids: `.two` (1fr 1fr), `.two.wide-left` (1.3fr 1fr), `.two.wide-right`
(1fr 1.3fr), `.panels` for two side-by-side figures.

Components: `.claim`, a 3px solid black left rule for the one sentence per slide worth
remembering, at most one per slide; `.eq`, a bordered pale panel around display
mathematics, with `.eq.bare` for none; `pre`, code on `--code-bg` behind a 2px
`--prussian` left rule; `.controls`, a row of labelled `input[type=range]` under a figure,
each slider showing its current value in mono beside its label; `.readout`, a live matrix
in `.mat` beside a mono `.note`, under an interactive figure; `.hint`, one mono line
under an interactive figure saying what is draggable; `.mc`, the quiz options, ruled rows
with a mono letter in the first column; `.series`, the five-lecture list on slide 2, each
entry a bold title over a mono `small` of its contents.

## Mechanics

KaTeX 0.16.9 from `cdnjs.cloudflare.com`: stylesheet, `katex.min.js`, and
`contrib/auto-render.min.js`. Omit the `integrity` attributes — an unverifiable SRI hash
blocks the script silently and no mathematics renders. Auto-render with `$$…$$` for
display and `\(…\)` for inline.

Navigation by arrow keys, space, Enter, PageUp, PageDown, Home, End; click to advance
except on buttons, links, form controls, the overview, and code blocks.
Arrow keys belong to a focused slider, not to the deck. `N` opens the speaker notes in a
separate window, so only the deck goes on the shared screen; arrow keys navigate from
either window. `O` is a thumbnail overview, `F` full screen, `Esc` closes panels. The URL
hash carries the slide number so a single slide can be linked. A print stylesheet emits
one page per slide for print-to-PDF. One draw-in animation on the title figure only;
`prefers-reduced-motion` respected. Interactive figures are the exception and are not
animations: nothing moves until the viewer moves a control, and every such figure has a
state it opens in that reads correctly with nothing touched.

## Slide markup

```html
<section class="slide" data-where="Section name">
  <h2>Heading</h2>
  <p class="sub">One italic line framing the slide. Optional, and often absent.</p>
  <div class="two wide-left">
    <div>
      <div class="eq">$$\dots$$</div>
      <ul><li>Three or four fragments</li></ul>
      <p class="claim">The one sentence worth remembering.</p>
    </div>
    <figure>
      <svg viewBox="0 0 330 300" role="img" aria-label="…"></svg>
      <figcaption>One line saying what the figure shows.</figcaption>
    </figure>
  </div>
  <aside class="notes"><h4>Speaker notes</h4><p>…</p><p>…</p><p>…</p></aside>
</section>
```

An interactive figure replaces `<figure>` with `<figure class="demo" data-demo="name">`
and adds `.controls`, `.readout` and a `.hint` line under the svg.

Note the shape of it: the notes are the longest thing in the section. If they are not,
the slide is carrying prose that belongs in them.

## Editorial rules

Headings are mathematical, in sentence case, and name their subject rather than
advertising it.

No motivational preamble and no slide arguing that the material is worth learning.

Nothing about performance, hardware, or making code fast.

Definitions are geometric first and in coordinates second, wherever both are available.

Forward references are stated explicitly, and paid off explicitly when they arrive.

Omissions are named in a sentence rather than passed over.

Headings name one thing. A heading joined by "and" or a semicolon is two slides.

Every slide carries speaker notes: the prose that is not on the slide, what to emphasise,
any demonstration worth doing, the worked arithmetic to say out loud, and what to cut if
time is short.

Worked numbers are spoken, not printed. A slide shows the formula; the notes carry the
example, with the arithmetic done so the lecturer can read it off.

Bullets are fragments, not sentences. A full stop in a bullet is a sign it belongs in the
notes.

Cross-references name their target rather than numbering it, in both the decks and this
document.

Avoid: all-caps labels, decorative numbering, new notation introduced before it is
needed, more than one `.claim` per slide, and any paragraph of prose on a slide.
