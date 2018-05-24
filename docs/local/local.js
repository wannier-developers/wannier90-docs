MathJax.Hub.Config({
        TeX: {
	    Macros: {
		bm: ["\\boldsymbol{#1}",1]
		    }
	},
	tex2jax: {
	    skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'],
		inlineMath: [['$','$']]
		}
    });
MathJax.Ajax.loadComplete("https://wannier-developers.github.io/wannier-docs/local/local.js");
