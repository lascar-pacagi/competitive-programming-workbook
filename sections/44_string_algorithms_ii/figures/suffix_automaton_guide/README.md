# Suffix automaton guide figures

These twelve figures were adapted from the user-supplied
`suffix_automaton_guide.qmd` for Chapter 4 of the Section 44 lesson.
The original explanation's examples, state numbering, groups, character
transitions, and suffix links are preserved. Labels are translated into
English, pale metadata is darkened, and the widest graphs use landscape
pages in the lesson.

The SVG files are editable sources. The PDF files are vector exports used
by `lesson.qmd`. After editing an SVG, rebuild the exports with Inkscape:

```bash
python3 sections/44_string_algorithms_ii/figures/suffix_automaton_guide/build.py
```

Figures 1 and 5 show `aba`; figures 2, 11, and 12 show `abcbc`; figure 3
shows `abcbcd`; figure 4 illustrates shortening suffixes of `abcbc`.
Figures 6 and 7 show the first two extension cases. Figures 8-10 show
`ab` becoming `abb`. The red suffix link in figure 9 is deliberately
invalid and belongs only to the intermediate conflict illustration.
