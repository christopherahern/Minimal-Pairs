# Introduction

This repository contains the source code for the presentation entitled
“Persistence as a diagnostic of grammatical status” at [DiGS15][digs15]
by [Aaron Ecay][aaron] and [Meredith Tamminga][meredith].

[digs15]: http://artsites.uottawa.ca/digs15/
[aaron]: http://www.ling.upenn.edu/~ecay/
[meredith]: http://www.meredithtamminga.com/

# Instructions

## Corpus data

In order to replicate the corpus portion of this analysis, you will need
a copy of the Penn Parsed Corpus of Middle English ([PPCME2][ppcme]) and
version 2.003.04 of the [CorpusSearch][corpussearch] program.

[ppcme]: http://www.ling.upenn.edu/histcorpora/PPCME2-RELEASE-3/
[corpussearch]: http://corpussearch.sourceforge.net/

To preform the replication, you should examine the `make-corpus.sh`
script in the `queries` subdirectory of this repository.

1. Edit the line of the file beginning `CS_COMMAND=` so that it points
to the location on your computer where the CorpusSearch program is.

2. You will also need to place a file named `ppcme2.out` in the
`queries` directory that contains the PPCME2 corpus (concatenating
together the `.psd` files from the corpus release suffices).

Once you have performed these two steps, you should run the
`make-corpus.sh` script.  The final output of this process is the
`coding.cod.ooo` file, a copy of which is also included in this
repository for the convenience of those who do not have access to the
PPCME2.  This file is the input to the next stage.

## Analysis

The analysis is provided in the form of R source code,, in two files in
the `scripts` subdirectory.  In order to use this code, you will need to
install the `stringr`, `ggplot2`, `plyr`, `reshape2`. and `tikzDevice`
packages (the last only if you intend to replicate the graphs for
compilation to PDF, and not merely interactively in the R console):

    install.packages(c("stringr","plyr","ggplot2", "reshape2"))
    install.packages(c("tikzDevice"), repos = c("http://R-Forge.R-project.org"))

(The `tikzDevice` package has to be installed from a non-default
repository, because it is not distributed on CRAN, the main R package
distribution network.)

You should set R’s working directory to the root of this repository
(e.g. with the `setwd()` function.)

Once you have done that, load the two scripts:

    source("scripts/data.R")
    source("scripts.graphs.R")

Then, load the data into R:

    neg <- cleanNegData()

Then, you can make the graphs:

    all.graphs()

Inspect the source in the `graphs.R` file for more detail about
individual graphs.

## Slide show

In order to recreate the slide show from the LaTeX source, you will need
several LaTeX packages; consult the `presentation.tex` and
`digs-slides.cls` files for exact details.  You should compile the
slides using the `lualatex` program, and `biber` for the bibliography.

The easiest way to install all the necessary programs is the
[TeXlive][texlive] distribution.

[texlive]: https://www.tug.org/texlive/

# Comments

If you have comments on the presentation, the analysis, or any aspect of
the work, please feel free to email <ecay@ling.upenn.edu>.
