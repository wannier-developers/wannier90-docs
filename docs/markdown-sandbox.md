# Some content

## This is page 2

Let's see if footnotes work[^myfootnote].

[//]: # (This will go at the bottom of the page)

[^myfootnote]: Some footnote content

I think this is probably the simplest way to have citations[^mycit].


[^mycit]: N. Marzari and D. Vanderbilt, **Phys. Rev. B 56**, 12847 (1997).


Goto [home page](index)

Some<sup>superscript</sup> and some<sub>subscript</sub>.

## A numbered list

[//]: # (I explicitly create anchor tags here)


1. <a name="point1"></a>Some content one
1. <a name="point2"></a>Some content two
1. <a name="point3"></a>Some content three

## A table

| head1        | head two          | three |
|:-------------|:------------------|:------|
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good `oreos`      | hmm   |
| ok           | good `zoute` drop | yumm  |


Read the [Markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#tables)

## A parameters table

[//]: # (This is a comment: leave empty lines around)
[//]: # (Note that every header automatically gets a anchor that can be linked to by putting to lowercase and replacing spaces with dashes)

| Keyword | Type | Description |
|:--------|:----:|:------------|
| `num_wann` | I | Number of WF |
| `unit_cell_cart` | P | Unit cell vectors in Cartesian coordinates |

## An itemized list

- Line 1
- Line 2
- Line 3






## Some python code
```python
import sys

def myf(a):
    return a
```


## Some fortran code
```fortran
SUBROUTINE me

INTEGER :: a

CALL somefunction(a)

! A comment
IF (a .ne. 3) THEN
    WRITE(*,*) "some string"
END IF

END SUBROUTINE
```

## Some uncolored text
```
This
is 
some output file   output
```

## Footnotes will appear here below
