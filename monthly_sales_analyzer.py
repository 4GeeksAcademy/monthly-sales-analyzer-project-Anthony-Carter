# Example data
sales_data = [
    {"day": 1, "product_a": 202, "product_b": 142, "product_c": 164},
    {"day": 2, "product_a": 206, "product_b": 121, "product_c": 338},
    {"day": 3, "product_a": 120, "product_b": 152, "product_c": 271},
    {"day": 4, "product_a": 174, "product_b": 137, "product_c": 266},
    {"day": 5, "product_a": 199, "product_b": 153, "product_c": 301},
    {"day": 6, "product_a": 230, "product_b": 199, "product_c": 202},
    {"day": 7, "product_a": 101, "product_b": 137, "product_c": 307},
    {"day": 8, "product_a": 137, "product_b": 179, "product_c": 341},
    {"day": 9, "product_a": 287, "product_b": 70, "product_c": 310},
    {"day": 10, "product_a": 157, "product_b": 71, "product_c": 238},
    {"day": 11, "product_a": 148, "product_b": 108, "product_c": 319},
    {"day": 12, "product_a": 287, "product_b": 64, "product_c": 339},
    {"day": 13, "product_a": 289, "product_b": 100, "product_c": 257},
    {"day": 14, "product_a": 154, "product_b": 113, "product_c": 280},
    {"day": 15, "product_a": 150, "product_b": 184, "product_c": 170},
    {"day": 16, "product_a": 172, "product_b": 67, "product_c": 281},
    {"day": 17, "product_a": 188, "product_b": 109, "product_c": 163},
    {"day": 18, "product_a": 108, "product_b": 139, "product_c": 202},
    {"day": 19, "product_a": 229, "product_b": 133, "product_c": 241},
    {"day": 20, "product_a": 210, "product_b": 57, "product_c": 324}
]

def total_sales_by_product(data, product_key):
    """Calculates the total sales of a specific product in 30 days."""
    
    total_sales = 0
    
    for i in range(len(data)):
       total_sales = total_sales + data[i][product_key]

    return total_sales




c





def best_selling_day(data):
    """Finds the day with the highest total sales."""
    
    
    day1 = {"day": 1, "product_a": 202, "product_b": 142, "product_c": 164}
    day2 = {"day": 2, "product_a": 206, "product_b": 121, "product_c": 338}
    day3 = {"day": 3, "product_a": 120, "product_b": 152, "product_c": 271}
    day4 = {"day": 4, "product_a": 174, "product_b": 137, "product_c": 266}
    day5 = {"day": 5, "product_a": 199, "product_b": 153, "product_c": 301}
    day6 = {"day": 6, "product_a": 230, "product_b": 199, "product_c": 202}
    day7 = {"day": 7, "product_a": 101, "product_b": 137, "product_c": 307}
    day8 = {"day": 8, "product_a": 137, "product_b": 179, "product_c": 341}
    day9 = {"day": 9, "product_a": 287, "product_b": 70, "product_c": 310}
    day10 = {"day": 10, "product_a": 157, "product_b": 71, "product_c": 238}
    day11 = {"day": 11, "product_a": 148, "product_b": 108, "product_c": 319}
    day12 = {"day": 12, "product_a": 287, "product_b": 64, "product_c": 339}
    day13 = {"day": 13, "product_a": 289, "product_b": 100, "product_c": 257}
    day14 = {"day": 14, "product_a": 154, "product_b": 113, "product_c": 280}
    day15 = {"day": 15, "product_a": 150, "product_b": 184, "product_c": 170}
    day16 = {"day": 16, "product_a": 172, "product_b": 67, "product_c": 281}
    day17 = {"day": 17, "product_a": 188, "product_b": 109, "product_c": 163}
    day18 = {"day": 18, "product_a": 108, "product_b": 139, "product_c": 202}
    day19 = {"day": 19, "product_a": 229, "product_b": 133, "product_c": 241}
    day20 = {"day": 20, "product_a": 210, "product_b": 57, "product_c": 324}

    highest_day = 0
    
    for i in range(len(data)):
       highest_day = max("product_a", "product_b", "product_c")
        
    return highest_day





def days_above_threshold(data, product_key, threshold):
    """Counts how many days the sales of a product exceeded a given threshold."""
    
    threshold > 300
    for i in range(len(data)):
        if threshold > threshold + data[i]["product_c"]:
            return threshold
    





def top_product(data):
    """Determines which product had the highest total sales in 30 days."""
    pass
    total_salesa = 0
    total_salesb = 0
    total_salesc = 0
    
    for i in range(len(data)):
        total_salesa = total_salesa + data[i]["product_a"]
        total_salesb = total_salesb + data[i]["product_b"]
        total_salesc = total_salesc + data[i]["product_c"]
    return total_salesa, total_salesb, total_salesc
    


# Function tests
print("Total sales of product_a:", total_sales_by_product(sales_data, "product_a"))
print("Average daily sales of product_b:", average_daily_sales(sales_data, "product_b"))
print("Day with highest total sales:", best_selling_day(sales_data))
print("Days when product_c exceeded 300 sales:", days_above_threshold(sales_data, "product_c", 300))
print("Product with highest total sales:", top_product(sales_data))
