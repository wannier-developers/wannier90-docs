## This creates a latex file from the md
## Issues:
## - Should not put `%raw%`
##- Can only compile png and jpg (and pdf); svg and gif don't work
## - `\begin{align}` is put inside another layer of `\[` so it fails; use \begin{aligned} instead
## - custom macros defined in the local.js must be redefined (currently repeated in header.tex)
## 
## - PDF links to sections

user_guide.pdf: index.md markdown-sandbox.md header.tex pandocfilter.py before_body.tex
	pandoc -s --filter pandocfilter.py -H header.tex -B before_body.tex index.md markdown-sandbox.md -o $@

user_guide.tex: index.md markdown-sandbox.md header.tex pandocfilter.py before_body.tex
	pandoc -s --filter pandocfilter.py -H header.tex -B before_body.tex index.md markdown-sandbox.md -o $@