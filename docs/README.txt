I'm investigating if I can use a pandoc filter to properly create links between different docs


Another suggestion is to do  something like:

<div id="fig:lalune">
![A voyage to the moon\label{fig:lalune}](lalune.jpg)

</div>

[The voyage to the moon](#fig:lalune).
