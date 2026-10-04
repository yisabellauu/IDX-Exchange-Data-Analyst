# IDX-Exchange-Data-Analyst

# WEEK 1
## CRMLS Monthly Data Concatenation

This Python script combines 32 monthly CRMLS Sold files and 32 monthly CRMLS Listing files from January 2024 through August 2026.

After concatenation, both datasets are filtered to PropertyType == 
‘Residential’ only

The filtered datasets are saved as:

- `Combined_Sold_Residential.csv`
- `Combined_Listings_Residential.csv`

### Sold Dataset

| Processing stage | Row count |
|---|---:|
| Before concatenation | 714,371 |
| After concatenation | 714,371 |
| Before Residential filter | 714,371 |
| After Residential filter | 480,487 |


### Listing Dataset

| Processing stage | Row count |
|---|---:|
| Before concatenation | 990,384 |
| After concatenation | 990,384 |
| Before Residential filter | 990,384 |
| After Residential filter | 629,792 |


