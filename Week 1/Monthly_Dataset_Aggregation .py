import pandas as pd



months = [
    "202401", "202402", "202403", "202404", "202405", "202406",
    "202407", "202408", "202409", "202410", "202411", "202412",
    "202501", "202502", "202503", "202504", "202505", "202506",
    "202507", "202508", "202509", "202510", "202511", "202512",
    "202601", "202602", "202603", "202604", "202605", "202606",
    "202607", "202608"
]


sold_files = []
for month in months:
    sold_month = pd.read_csv(
        f"CRMLSSold{month}.csv", encoding="latin-1", low_memory=False
    )
    print(f"CRMLSSold{month}.csv before concatenation: {len(sold_month)} rows")
    sold_files.append(sold_month)

sold_rows_before_concat = sum(len(file) for file in sold_files)
print("Sold rows before concatenation:", sold_rows_before_concat)

sold = pd.concat(sold_files, ignore_index=True)
print("Sold rows after concatenation:", len(sold))

print("Sold rows before Residential filter:", len(sold))
sold = sold[sold["PropertyType"] == "Residential"]
print("Sold rows after Residential filter:", len(sold))

sold.to_csv("Combined_Sold_Residential.csv", index=False)


listing_files = []
for month in months:
    listing_month = pd.read_csv(
        f"CRMLSListing{month}.csv", encoding="latin-1", low_memory=False
    )
    print(f"CRMLSListing{month}.csv before concatenation: {len(listing_month)} rows")
    listing_files.append(listing_month)

listing_rows_before_concat = sum(len(file) for file in listing_files)
print("Listing rows before concatenation:", listing_rows_before_concat)

listing = pd.concat(listing_files, ignore_index=True)
print("Listing rows after concatenation:", len(listing))

print("Listing rows before Residential filter:", len(listing))
listing = listing[listing["PropertyType"] == "Residential"]
print("Listing rows after Residential filter:", len(listing))

listing.to_csv("Combined_Listings_Residential.csv", index=False)


print("Finished. Two combined CSV files were created.")
