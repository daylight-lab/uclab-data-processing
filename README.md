# Internet blocking as a proxy of policy alignment

The code in this demo generates a proxy of policy alignment: similarities in website blocking. For every pair of countries, we generate a weight representing the degree of similarity in observed website blocking.

## Using our data

To use our data, simply [download the CSV of computed metrics](https://github.com/daylight-lab/website-blocking-proxy/blob/master/data/metrics.csv). `Overall_Similarity` is the proxy measure. Subscores represent censored category similarity (simliarity of content blocked) and blocking proportion similarity (proportion of observations that result in blocking; a proxy for blocking volume).

To replicate our metrics, clone this repo and follow the instructions in the Jupyter notebook in `notebooks/`. All required data are included in `data/` or linked to in the notebook.

## Acknowledgements
Currently, the demo is [using measurements taken by the Information Controls Lab (ICLab)](https://iclab.org/post/iclab_data/).

We are combining these data with categorizations from [Fortiguard's web filter](https://fortiguard.com/webfilter).

## License
BSD-3
