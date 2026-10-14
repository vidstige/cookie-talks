# How Stuff Works: AI from scratch — master plan

Five lectures of one hour, meant to be taken in order.

**Lecture 1 assumes nothing beyond arithmetic and a willingness to look at notation.**
Every lecture after it assumes the ones before: their material is used, not rebuilt. A
result established earlier is recalled in a sentence where it is needed — named, not
re-derived — and then used. Nothing outside the series is ever assumed.

This document specifies the shape of the series: what each lecture covers, in what
order, and what it takes from the ones before it. It does not specify slide content, and
it does not record how a lecture came out — a built deck is its own record, in its HTML
and its speaker notes. Visual and editorial style are in the appendix.

---

## How to use this document

Paste this file as a prompt and name a lecture:

> Build lecture 1 from this plan.

The builder is expected to:

1. Produce one self-contained HTML file per lecture. No build step; it opens by
   double-clicking.
2. Follow Appendix A exactly. The five decks must read as one series.
3. Follow *Presentation style* below exactly. It is the rule a first draft is most
   likely to break, and the most expensive one to repair afterwards.
4. Read the decks of the preceding lectures first, and build on what they established
   rather than teaching it again.
5. Write the mathematical content for each topic listed below, at the level of a first
   encounter, together with speaker notes on every slide. Most of the writing goes in
   the notes.
6. Verify anything a slide asserts numerically: figure geometry, worked arithmetic,
   internal slide references.
7. Not add topics beyond the outlines below without asking — and say which listed topics
   were dropped, so this document can be brought back in line.

---

## Time model

| | |
|---|---|
| Material | 45 min |
| Quiz | 5 min, at the end |
| Questions and overrun | 10 min |

Budget in *concepts*, not in slides: about twenty concepts fill the 45 minutes. A slide
holding one short list and one figure costs well under two minutes; a slide with a
slider the room wants to play with costs four. Count the sliders and the load-bearing
slides first, then fill the rest in around them.

Slide count is therefore a consequence, not a target. Splitting one crowded slide into
three plain ones costs no extra time — the same words get said either way — so split
freely; thirty-odd slides is what twenty concepts look like once no slide holds two of
them. There is no recap slide: the quiz serves that purpose and gets a response from the
room rather than a nod.

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

*The slide is not the script, and every word on it is spoken to the room.*

**Write for the audience, never about the deck.** Nothing on a slide may refer to the
deck's own structure or to the lecturer's plan for it. "The example for this section",
"no derivatives yet", "the second of the three cases", "as promised earlier" are notes
to the author that have leaked onto the screen. Say the mathematical thing instead:
*One number goes in, one number comes out.* Headings and `.sub` lines break this rule
first, so write them last and read them back as if from the third row. The plan for the
hour belongs in the speaker notes, and there it is welcome.

**Meet the audience where it is.** Lecture 1 assumes arithmetic and nothing else; every
later lecture assumes the series so far and nothing else. A term is defined before it is
used, unless an earlier lecture defined it — then it is recalled in a sentence and used.
A rule is built up through the simplest cases that show it — a constant, then a line,
then a square, then the general power — and each case may have its own slide. Assume
nothing about a topic the series has not covered, however standard: a function nobody
has differentiated yet cannot appear in an example.

**A slide carries little.** At most a heading, an optional one-line italic `.sub`, a
short list or a displayed equation, one `.claim`, and a figure with its caption. Three
or four bullets, each a fragment rather than a sentence; a full stop in a bullet is a
sign it belongs in the notes. As a number to steer by: a delivered deck averages about
35 words of on-slide text per slide, and a draft that has to be rewritten averages 113.

**A definition box holds the definition.** The general statement goes in the `.eq` box;
a worked instance goes underneath it in a bare one, never inside the same box. Where the
example *is* the lesson — a differentiation rule, a first encounter with notation — it
earns its place on the slide; otherwise the arithmetic is spoken, and lives in the
notes.

**Everything else is spoken, and everything spoken is written down** in the speaker
notes: the derivation, the worked arithmetic, the caveat, the aside, the demonstration
to run, the forward reference. Notes run long on purpose — roughly a hundred words a
slide — and they are where a sentence goes when it is true, worth saying, and would
crowd the slide. If prose is on the slide, the audience reads it instead of listening.
The notes should be the longest thing in a slide's markup; if they are not, the slide is
carrying prose that belongs in them.

**Interactive figures carry one idea and one cluster of controls.** A segmented control
that switches a figure between four unrelated transforms is a slide doing four jobs;
give each its own slide and its own slider. Every such figure needs a resting state that
reads correctly before anything is touched.

**Every slide says what to drop if the hour runs long,** in its notes, once the timing
is known. Load-bearing slides — the ones a later lecture depends on — say so instead.

---

# Lecture 1 — Vectors, bases and linear maps

**Status: delivered.** `linear-algebra/lecture-1.html`.

**Assumes:** arithmetic. This is the one lecture in the series with no prerequisite
inside it.

**Arc.** Vectors come first as geometric objects, then as coordinates in an arbitrary
basis — skewed, unlovely — and only then as coordinates in a square one, presented as a
choice rather than as what coordinates are. Length and the inner product arrive after
that, turning right angles into a number. Matrices appear where they are actually
needed: a system of linear equations, written \(Ax = b\). That gives the matrix–vector
product a reason to exist before it is given a name, and substituting one system into
another gives the matrix product, its non-commutativity and the identity. Only then is a
matrix reread as a transformation of space, at which point its columns are recognised as
the images of the basis vectors and a whole figure can be pushed through one. Two
decompositions close the lecture, briefly.

**Why this ordering.** A matrix introduced as a transformation has to carry an
arithmetic nobody asked for; a matrix introduced as the bookkeeping of a linear system
has that arithmetic forced on it. The transformation reading then arrives as a
reinterpretation of something already familiar, which is the one moment in the lecture
worth spending real time on.

**Outline.**

**I. Vectors** — vectors as geometric objects; addition, scalar multiplication and
linear combinations; coordinates in a basis; orthogonality; Cartesian coordinates; the
norm; the inner product; orthogonal projection

**II. Linear systems** — systems of linear equations; the matrix product; the transpose;
the identity; the inverse

**III. Basis vectors and transforms** — matrices as linear transformations; the columns
as the images of the basis vectors; rotation, scaling, shear and translation, one slider
each; combining transforms

**IV. Matrix decomposition** — eigenvalues and eigenvectors; LU

**V. Quiz**

**Carried forward:** the inner product, projection, the inverse, eigenvalues, and the
homogeneous coordinates of the translation slide.

---

# Lecture 2 — Basic calculus

**Status: built.** `calculus/lecture-2.html`.

**Assumes lecture 1:** vectors and coordinates throughout, and the matrix product for
the Jacobian and the chain rule in section III.

**Arc.** Organised by the shape of the function, and says so: one number in and one out,
then several in and one out, then several in and several out. Each section opens on a
slide that states the shape, gives the general form and an example, and every section
after the first is the first one again with more coordinates. Section I is deliberately
slow at the start — a constant, a line, a square, and only then the power rule. The
lecture closes on how a derivative is actually obtained: by hand, by difference quotient,
or automatically, with forward mode worked and its cost stated, so lecture 4 has a reason
to want reverse mode.

**Outline.**

**I. One number in** — A function of one number; rates of change and the difference
quotient; the derivative; the slope of a constant, of a line, of \(x^2\); the rules for
powers, constant multiples, sums and the exponential; the chain rule; the second
derivative

**II. Vector in** — A function with vector input; partial derivatives; one slice at a
time; the gradient; the Hessian

**III. Vector out** — A function with vector output; the Jacobian; the chain rule in
several variables

**IV. Obtaining derivatives** — by hand, by difference quotient, by program; the
forward, backward and central differences; forward-mode automatic differentiation and
its cost

**V. Quiz**

**Carried forward:** the gradient, the second derivative and the Hessian, the Jacobian
and the chain rule, and the cost of forward mode as the reason reverse mode exists.

**Left for lecture 3 to introduce:** the directional derivative, stationary points and
the second-derivative test, and the quadratic approximation.

---

# Lecture 3 — Numerical optimization

**Status: built.** `optimization/lecture-3.html`.

**Assumes lectures 1 and 2:** eigenvalues and orthogonal projection from lecture 1;
the gradient, the Hessian and the Jacobian from lecture 2, whose derivatives it may
now take as available.

**Arc.** A sequence of algorithms of increasing sophistication for finding the argument
that minimizes a function. It opens on local minima, the trap every method shares, and
stays in one dimension until Newton's method: comparisons first, then the slope, and
Newton's method introduced as an equation solver before it is pointed at the derivative.
Least squares opens the several-variable material: the linear problem a formula solves
outright, then the nonlinear one, solved by applying that formula again at every step.
The rest of that material walks downhill: descent directions, gradient descent, and the
cheap repairs for the zig-zag that networks are trained with. The lecture closes
on constraints and stochastic descent.

**Outline.**

**I. One dimension** — the minimization problem; local minima; bracketing a minimum;
halving the bracket; the stationary condition; stationary points, with a peak, a pause
and a dip; Newton's method for equations; Newton's method for a minimum

**II. Least squares** — linear least squares; the normal equations, which state the
objective, then the condition that its gradient vanishes, then the solve; nonlinear
least squares; Gauss–Newton

**III. Several variables** — descent directions; gradient descent; fixed step lengths;
conditioning and the zig-zag; momentum; Adam

**IV. The wider landscape** — constrained optimization, in brief; stochastic gradient
descent

**V. Quiz**

The quiz has five questions and stays easy: the problem statement, zero slope at a
minimum, Gauss–Newton against Newton, the direction of gradient descent, and what Adam
remembers. The "in brief" topic is one slide and stays that way: it exists to show where the
subject continues, not to cover it. Updates are written as iterations, x_{n+1} from
x_n, never as assignments.

The pause on the stationary-points slide stands in for plateaus, and its speaker notes
tell the three kinds apart by the second derivative. Saddle points are not covered. Of the topics lecture 2 handed forward, the quadratic
approximation survives only as the second reading of Newton's step, in the speaker
notes. Dropped to make room for the notebook: golden-section search, line search, the
quadratic approximation as its own slide, Levenberg–Marquardt with trust regions, least
squares as orthogonal projection, global methods, the second-derivative test with
its saddle, and Newton's method in several variables, whose Hessian cost is now a
paragraph in the Gauss–Newton notes. Lecture 1's projection is still paid off, in a
line on the normal-equations slide: the residual is orthogonal to every column.

**Carried forward:** stochastic gradient descent and step-length behaviour, which
lecture 4 trains with.

---

# Lecture 4 — The multilayer perceptron

**Assumes lectures 1–3:** affine maps and homogeneous coordinates from lecture 1; the
chain rule in several variables from lecture 2, which is the whole of backpropagation;
gradient descent and its step length from lecture 3.

**Arc.** The object first, the training second. A multilayer perceptron is defined as a
parametric family of functions built by alternating affine maps with a fixed
nonlinearity, and the necessity of that nonlinearity is established before it is
introduced. XOR provides a network whose weights can be chosen by hand, which motivates
the second half: choosing them by minimization instead. A single toy problem in the
plane — two interleaving classes, so the decision boundary can be watched during
training — carries the training material from the moment it is introduced.

**Outline.**

**I. The network** — a parametric family of functions; a composition of linear maps is
linear; the affine layer and the activation function; activation functions; the
multilayer perceptron; the forward pass and batches; XOR and the limits of one layer; a
network with weights chosen by hand

**II. Training** — the toy problem; loss functions; squared error and cross-entropy;
training as minimization over the parameters; many parameters, one scalar output;
reverse-mode differentiation; backpropagation for a two-layer network; the training
loop; initialization and step length; overfitting and validation; what a multilayer
perceptron cannot do

**III. Quiz**

**Notebook.** A separate `.ipynb`, built with the deck. NumPy only, no framework, so
nothing is hidden: dataset, explicit forward pass, explicit backward pass matching the
backpropagation slide, training loop plotting the boundary periodically, and a set of
deliberate breakages to run — zero initialization, step length far too large,
nonlinearity removed. Under about 150 lines of code.

Cross-entropy has a probabilistic justification this series does not supply. Say so on
the slide rather than implying the choice is arbitrary.

**Carried forward:** the affine layer, the activation function and the training loop,
which lecture 5 assembles into a transformer block.

---

# Lecture 5 — The attention mechanism

**Assumes lectures 1–4:** the inner product and linear maps from lecture 1; the layers,
the loss and the training loop from lecture 4. Nothing from lecture 2 beyond what
lecture 4 already uses.

**Arc.** The problem is stated first: variable-length sequences in which every position
must consult the others, which a fixed-width network cannot express. Attention is then
built in stages — mixing with fixed weights, then with content-dependent weights, then
with weights obtained from inner products — so that the final formula assembles from
parts already justified. The transformer block, residual connections and stacking
follow. The lecture closes by returning to invariance: the coordinates of a learned
vector carry little meaning individually, and the operations a transformer is built
from — linear maps and inner products — are precisely those that do not depend on a
choice of basis. That is the closing argument of the series.

**Outline.**

**I. The problem** — sequences of variable length; why a fixed-width network cannot do
this; from tokens to vectors

**II. Constructing attention** — mixing with fixed weights; content-dependent weights;
queries, keys and values; scores as inner products; scaling by the square root of the
dimension; the softmax; the attention operation; a worked example

**III. Variants and structure** — self-attention and cross-attention; causal masking;
multi-head attention; permutation invariance and positional encoding

**IV. The transformer** — the transformer block; residual connections; stacked blocks,
logits and sampling; invariance revisited

**V. Quiz** — and what this series did not cover.

Multi-head attention wants orthonormal bases, which lecture 1 does not supply beyond
orthogonality, Cartesian coordinates and the orthogonality of a rotation. This lecture
builds the rest itself or accepts the gap.

---

# Open question for the series

**Probability.** Cross-entropy in lecture 4 and the softmax in lecture 5 both rest on
probability the series never develops. The current decision is to acknowledge the gap on
the slide and continue. A sixth lecture on probability, expectation and likelihood is
the obvious extension if there is appetite.

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

## Figures

Definitions are geometric first and in coordinates second, wherever both are available.

Three-dimensional figures get an opaque tile so the graph paper does not read through
them. The surface is depth-sorted quads with a nearly opaque fill, so whatever lies
behind it shows through dimmed rather than crossing it; that dimming is the only depth
cue a line drawing has. Each figure is framed once, at the camera it opens on, and the
viewer turns it with a drag and scales it with the wheel or two fingers.

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

## Notation

Fixed across the series, so a symbol means the same thing in every deck.

Derivatives are \(\frac{df}{dx}\) throughout. The prime is named once, in lecture 2, and
otherwise not used: it cannot say which variable it differentiates with respect to. The
one exception is Newton's method in one dimension in lecture 3, written
\(x_{n+1}=x_n-f'(x_n)/f''(x_n)\), because the ratio of a value and a slope at one point
reads more clearly with primes. Gradients are
rows, so \(\nabla f\,h\) is a matrix times a step and the gradient is visibly the one-row
Jacobian. A Jacobian is \(m\times n\): one row per output, one column per input.

No notation slide anywhere. Symbols are introduced where they are first needed.

## Editorial rules

Headings are mathematical, in sentence case, and name their subject rather than
advertising it.

No motivational preamble and no slide arguing that the material is worth learning.

Nothing about performance, hardware, or making code fast.

Forward references are stated explicitly, and paid off explicitly when they arrive.

Omissions are named in a sentence rather than passed over.

Headings name one thing. A heading joined by "and" or a semicolon is two slides.

Cross-references name their target rather than numbering it, in both the decks and this
document — "the projection slide in lecture 1", never a slide number.

Avoid: all-caps labels, decorative numbering, new notation introduced before it is
needed, more than one `.claim` per slide, and any paragraph of prose on a slide.
