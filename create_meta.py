import pandas as pd
import json, os
 
def createMeta():
    # check existing product_metadata.json
    if os.path.exists("product_metadata.json"):
        product_metadata = json.load(open("product_metadata.json", "r"))
        return product_metadata

    MAX_TEXT_LENGTH=1000  # Maximum num of text characters to use
 
    def auto_truncate(val):
        """Truncate the given text."""
        return val[:MAX_TEXT_LENGTH]
    
    # Load Product data and truncate long text fields
    all_prods_df = pd.read_csv("product_data.csv", converters={
        'bullet_point': auto_truncate,
        'item_keywords': auto_truncate,
        'item_name': auto_truncate
    })  

    # Replace empty strings with None and drop
    all_prods_df['item_keywords'].replace('', None, inplace=True)
    all_prods_df.dropna(subset=['item_keywords'], inplace=True)
    
    # Reset pandas dataframe index
    all_prods_df.reset_index(drop=True, inplace=True)

    # Num products to use (subset)
    NUMBER_PRODUCTS = 2500  
    
    # Get the first 2500 products
    product_metadata = ( 
        all_prods_df
        .head(NUMBER_PRODUCTS)
        .to_dict(orient='index')
    )

    # save the product metadata to a json file
    with open('product_metadata.json', 'w') as f:
        json.dump(product_metadata, f) 

    return product_metadata