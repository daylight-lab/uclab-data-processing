# Data

This directory contains manipulated ICLab and scraped (clean) data from various sources as specified in the repo README, including final data files of country pair similarity indices and blocked domains used to power the public demo.

Below are explanations of key files.

### ICLab Data
- **data/iclab_combined_similarities.json** : similarity index data (see calculation in repo README)
- **data/iclab_common_domains** : country-specific pair domain data i.e. domains blocked in Country A that are also blocked in B
- **data/iclab_dropped_us_combined_similarities.json** : similarity index data *in the case that all websites blocked in the US according to the datasource are removed*
- **data/iclab_dropped_us_domains** : country-specific pair domain data *in the case that all websites blocked in the US according to the datasource are removed*

### Separate Datasources
- **data/separate_datasources_cleaned_data** : cleaned data scraped from the sources mentioned in the repo README
- **data/separate_datasources_combined_similarities.json** : similarity index data
- **data/separate_datasources_common_domains** : country-specific pair domain data
- **data/separate_datasources_cleaned_data/adversarial_data/combined_adversarial.csv** : list of domains blocked in Country A pairs that are based in Country B *for all country pairs in the dataset* [under active construction]
