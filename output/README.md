# output/

This folder contains all of our computed metrics.


## metrics.csv

This CSV file contains similarity metrics between all country pairs in our dataset.

- `pair` - A tuple of alpha-2 country codes (e.g., `('CO', 'PE')`).
- `country_code_alpha2_A` - The country code of the country A (e.g., `'CO'`)
- `country_code_alpha2_B` - The country code of the country A (e.g., `'PE'`)
- `country_code_alpha3_A`/`B` - Same as above, but with alpha-3 country code (e.g., `COL`/`PER`).
- `Overall_Similarity` - Simliarity of content blocked. Computed as cosine distance between content blocking category proportions (see `metadata.csv`).

## metadata.csv

This CSV file contains per-country blocking metrics.

- `alpha3`/`alpha2` - These identify the country by their ISO 2- or 3-letter country code.
- `num_observations` - The number of total observations (GET requests) made in this country across the dataset.
- `num_observations_blocked` - The number of observations that were marked as blocked. You can compute the proportion of observations blocked by dividing this number over `num_observations`.
- `num_unique_sites_measured` - The number of unique websites (URLs) that were queried across the dataset.
- `num_unique_sites_blocked` - The number of unique websites (URLs) that were marked as blocked.

The remaining columns report the proportion of blocked websites that belong to each Fortiguard category. You can recover the number of observations blocked in each category by taking the proportion for a given category and multiplying it by `num_observations_blocked`. For example, if South Korea's score for File Sharing and Storage websites is `1.891588538227915`, and its `num_observations_blocked` is `30292`, you can infer that 1100 blocking observations are associated with the File Sharing and Storage category.

## JSON

Each .CSV has an accompanying .JSON file. The formats are the same, except each row is stored as an object in a hash map, where the keys are represented either by Alpha-3 country codes (e.g., `'UKR'`) or by pairs of Alpha-3 country codes (e.g., `'UKR->AUS'`).
