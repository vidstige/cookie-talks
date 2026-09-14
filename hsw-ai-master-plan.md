# How Stuff Works: AI from scratch — master plan

Five lectures of one hour. Each is standalone and optional; attendance at earlier
lectures is not assumed. No prerequisites beyond arithmetic and a willingness to look at
notation.

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
3. Write the mathematical content for each slide listed below, at the level of a first
   encounter, together with speaker notes on every slide.
4. Verify anything a slide asserts numerically: figure geometry, worked arithmetic,
   internal slide references.
5. Not add topics beyond the sequences below without asking.

---

## Time model

| | |
|---|---|
| Material | 45 min, roughly 22 slides at two minutes |
| Quiz | 5 min, at the end |
| Questions and overrun | 10 min |

Each lecture below runs to 23 slides, the last of which is the quiz. There is no recap
slide: the quiz serves that purpose and gets a response from the room rather than a nod.

## Structure common to every lecture

| Slide | |
|---|---|
| 1 | Title. Lecture title only. |
| 2 | The series. Its subject, its five parts, that each is optional and standalone. |
| 3 | Outline of this lecture. Its sections, in order. |
| 4–22 | Material. |
| 23 | Quiz. |

Slide 2 is the same slide in all five decks, with the current lecture marked. Slide 3
differs per lecture and lists the section headings given below.

---

# Lecture 1 — Vectors, bases and linear maps

**Arc.** The conventional route. Vectors are introduced as geometric objects, then the
inner product, which makes norm, angle, orthogonality and projection available from the
start. Matrices arrive next as arrays with an arithmetic — the matrix–vector product and
the matrix product — and only then are reinterpreted as linear transformations, at which
point their columns are recognised as the images of the basis vectors. Span,
independence, basis and coordinates follow as a vector-space section, which puts change
of basis and similarity on a footing. Linear systems and spectral decomposition close.

**Why this ordering.** The inner product precedes coordinates, so the coordinates of a
vector in an orthonormal basis can be obtained by projection rather than by solving for
coefficients. The matrix product precedes the transformation interpretation, so
composition and non-commutativity are facts about an arithmetic already defined rather
than promises deferred to a later slide. Both are the standard textbook order.

| # | Slide |
|---|---|
| 1 | Vectors, bases and linear maps |
| 2 | The series |
| 3 | Outline |
| | **I. Vectors** |
| 4 | Vectors as geometric objects |
| 5 | Addition, scalar multiplication and linear combinations |
| 6 | The inner product: norm and angle |
| 7 | Orthogonality and orthogonal projection |
| | **II. Matrices** |
| 8 | Matrices and the matrix–vector product |
| 9 | The matrix product and the transpose |
| 10 | Matrices as linear transformations |
| 11 | The columns of a matrix are the images of the basis vectors |
| 12 | Rotation, scaling, shear, reflection; orthogonal matrices |
| 13 | Affine maps and homogeneous coordinates |
| | **III. Span, basis and coordinates** |
| 14 | Span and linear independence |
| 15 | Basis and dimension |
| 16 | Coordinates relative to a basis; orthonormal bases |
| 17 | Change of basis |
| 18 | Similar matrices |
| | **IV. Linear systems** |
| 19 | Systems of linear equations |
| 20 | Rank, null space, existence and uniqueness |
| | **V. Spectral decomposition** |
| 21 | Eigenvalues, eigenvectors and diagonalization |
| 22 | The singular value decomposition |
| 23 | Quiz |

Composition of transformations and the failure of commutativity are remarks on slide 9,
where the product is defined, not a separate slide. The figure showing one vector with
its components in two different bases belongs on slide 16, and slide 17 gives the
relation between the two coordinate vectors.

**Cut candidates, in order:** 18, 12, 14 folded into 15.

**Forward dependencies.** Slide 6 (inner product) is reused in lecture 5 for attention
scores. Slide 7 (projection) is reused in lecture 3 for least squares. Slide 13
(homogeneous coordinates) is reused in lecture 4 for the bias term. Slide 16 (orthonormal
bases) is reused in lecture 5 for multi-head projections. Slide 21 (eigenvalues) is
reused in lecture 3 for the condition number.

**Not covered, deliberately:** determinants beyond a remark, Gaussian elimination and the
LU/QR/Cholesky family, general inner-product spaces and metrics, Gram–Schmidt, complex
eigenvalues beyond a caveat.

---

# Lecture 2 — Basic calculus

**Arc.** The derivative is presented as the coefficient of the best local linear
approximation, from which the differentiation rules and the chain rule follow. Higher
derivatives give curvature and the Taylor expansion. The same construction is then
carried into several variables: partial derivatives, gradient, directional derivative,
Jacobian, Hessian. The lecture closes on the question of how a derivative is actually
obtained: by hand, by difference quotient, or automatically.

| # | Slide |
|---|---|
| 1 | Basic calculus |
| 2 | The series |
| 3 | Outline |
| | **I. The derivative in one variable** |
| 4 | Rates of change and the difference quotient |
| 5 | The limit |
| 6 | The derivative as best local linear approximation |
| 7 | Rules: power, sum, product, quotient |
| 8 | The chain rule |
| | **II. Local behaviour** |
| 9 | Stationary points and extrema |
| 10 | Higher derivatives and curvature |
| 11 | Taylor polynomials |
| | **III. Several variables** |
| 12 | Functions of several variables |
| 13 | Partial derivatives |
| 14 | The gradient |
| 15 | Directional derivatives |
| 16 | The Jacobian |
| 17 | The Hessian and the second-order expansion |
| 18 | The chain rule in several variables |
| | **IV. Obtaining derivatives** |
| 19 | Symbolic, numerical and automatic differentiation |
| 20 | Forward-mode automatic differentiation |
| 21 | The cost of forward mode |
| 22 | Numerical differentiation: the difference quotient in practice † |
| 23 | Step size: truncation against cancellation † |
| 24 | Quiz |

**† Floating block.** Slides 22–23 sit here or at the front of lecture 3, whichever has
time left after the rest is written. They are self-contained and do not affect the
numbering of anything before them. If they move, slide 19 keeps a forward reference to
them.

**Coordination note.** Slide 9 states the condition f′ = 0 at stationary points as a fact
about local behaviour. Lecture 3 does not restate it as a definition; it arrives at the
same condition as the thing an algorithm searches for.

**Forward dependencies.** Slide 8 (chain rule) is the whole of backpropagation in
lecture 4. Slide 14 (gradient) and slide 17 (Hessian) are the objects lecture 3
manipulates. Slide 21 (cost of forward mode) is the reason lecture 4 needs reverse mode.

**Not covered, deliberately:** integration, series convergence, multivariable integration,
differential equations, any epsilon-delta argument.

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
are re-established in a sentence, since attendance at lecture 1 is not assumed.

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

**Numerical differentiation.** Floating between lecture 2 (slides 22–23) and the start of
lecture 3. Decide once both are drafted and time is known.

**Load-bearing slides.** If any of these does not land, later lectures suffer: 1/11 (the
matrix of a transformation), 1/16 (the inner product), 2/6 (the derivative as linear
approximation), 2/8 (the chain rule), 3/7 (descent direction and line search), 4/5 (a
composition of linear maps is linear), 5/10 (scores as inner products).

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
| `li` | 21px, line-height 1.5, max-width 60ch |
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
`--prussian` left rule.

## Mechanics

KaTeX 0.16.9 from `cdnjs.cloudflare.com`: stylesheet, `katex.min.js`, and
`contrib/auto-render.min.js`. Omit the `integrity` attributes — an unverifiable SRI hash
blocks the script silently and no mathematics renders. Auto-render with `$$…$$` for
display and `\(…\)` for inline.

Navigation by arrow keys, space, Enter, PageUp, PageDown, Home, End; click to advance
except on buttons, links, the notes panel, the overview, and code blocks. `N` toggles
speaker notes, `O` a thumbnail overview, `F` full screen, `Esc` closes panels. The URL
hash carries the slide number so a single slide can be linked. A print stylesheet emits
one page per slide for print-to-PDF. One draw-in animation on the title figure only;
`prefers-reduced-motion` respected.

## Slide markup

```html
<section class="slide" data-where="Section name">
  <h2>Heading</h2>
  <p class="sub">One italic line framing the slide.</p>
  <div class="two wide-left">
    <div><!-- prose, lists, .eq, .claim --></div>
    <figure>
      <svg viewBox="0 0 330 300" role="img" aria-label="…"></svg>
      <figcaption>Two lines saying what the figure shows.</figcaption>
    </figure>
  </div>
  <aside class="notes"><h4>Speaker notes</h4><p>…</p></aside>
</section>
```

## Editorial rules

Headings are mathematical, in sentence case, and name their subject rather than
advertising it.

No motivational preamble and no slide arguing that the material is worth learning.

Nothing about performance, hardware, or making code fast.

Definitions are geometric first and in coordinates second, wherever both are available.

Forward references are stated explicitly, and paid off explicitly when they arrive.

Omissions are named in a sentence rather than passed over.

Every slide carries speaker notes: what to emphasise, any demonstration worth doing, and
what to cut if time is short.

Avoid: all-caps labels, decorative numbering, new notation introduced before it is
needed, and more than one `.claim` per slide.
