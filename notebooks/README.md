# Notebooks

This directory contains code for manipulating ICLab data as well as scraped data from various sources as specified in the repo README.

Below are explanations of key files:
(ICLab data)
- iclab-data-files : calculates similarity indices, lists of all overlapping domains between country pairs *from ICLab data*
  - similarity index data => data/iclab_combined_similarities.json
  - country-specific pair domain data => data/iclab_common_domains
- Because no sites are known to be blocked in the US, the iclab-data-files notebook also makes parallel calculations for similarity indices and overlapping domains in the case that all websites found in the data to be blocked in the US are dropped.
  - similarity index data => data/iclab_dropped_us_combined_similarities.json
  - country-specific pair domain data => data/iclab_dropped_us_domains

(separate datasources)
- scrape-blocked-websites : contains code for scraping relevant data / sources by country from the links listed in the repo README
  - cleaned data => data/separate_datasources_cleaned_data
- preliminary-blocked-site-overlap : calculates similarity indices, lists of all overlapping domains between country pairs
  - similarity index data => data/separate_datasources_combined_similarities.json
  - country-specific pair domain data => data/separate_datasources_common_domains
- adversarial-blocking : an exploration of how adversarial relationships between country pairs can be calculated (in this case, what is currently used to power the demo is Country A => Country B calculations based on websites blocked in A that originate in B) [under active construction]
  - list of domains blocked in Country A pairs that are based in Country B => data/separate_datasources_cleaned_data/adversarial_data/combined_adversarial.csv
