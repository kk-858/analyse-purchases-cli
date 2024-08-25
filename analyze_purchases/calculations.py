import polars as pl

def calculate_statistics(data):
    purchases_df = pl.DataFrame(data).explode('items')

    # Extract the necessary fields into separate columns
    purchases_df = purchases_df.with_columns([
        pl.col('items').struct.field('product_name').alias('product_name'),
        pl.col('items').struct.field('quantity').alias('quantity'),
        pl.col('items').struct.field('price').alias('price').cast(pl.Float64)
    ])

    # Calculate purchase value for each item
    purchases_df = purchases_df.with_columns([
        (pl.col('quantity') * pl.col('price')).alias('purchase_value')
    ])

    # Total volume of spend
    total_volume_spend = purchases_df['purchase_value'].sum()

    # Average purchase value
    average_purchase_value = purchases_df['purchase_value'].mean()

    # Maximum purchase value
    maximum_purchase_value = purchases_df['purchase_value'].max()

    # Median purchase value
    median_purchase_value = purchases_df['purchase_value'].median()

    # Number of unique products purchased
    unique_products_count = purchases_df['product_name'].n_unique()

    return {
        "total_volume_spend": total_volume_spend,
        "average_purchase_value": average_purchase_value,
        "maximum_purchase_value": maximum_purchase_value,
        "median_purchase_value": median_purchase_value,
        "number_of_unique_products_purchased": unique_products_count
    }
