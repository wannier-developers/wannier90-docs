MathJax.Hub.Config({
        TeX: {
	    Macros: {
		bm: ["\\boldsymbol{#1}",1],
		bvec: ["\\bm{\\mathrm{#1}}",1]
		    }
	},
	tex2jax: {
	    skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'],
	    inlineMath: [['$','$']]
	    }
    });
MathJax.Ajax.loadComplete("http://wannier-developers.github.io/wannier90-docs/assets/js/config/local.js");
