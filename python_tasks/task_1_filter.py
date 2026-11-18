# Task: List Comprehension & Filtering
# Instructions: Complete the function to return only even IDs 
# greater than 100, sorted in descending order.

def filter_orders(order_ids):
     filtered = []
  for id in order_ids:
      if id > 100:
        if id % 2 == 0:
          filtered.append(id)
  filtered.sort(reverse=True)
  return filtered
          
# Test Case
test_data = [10, 105, 120, 44, 202, 300, 75, 110]
# Expected Output: [300, 202, 120, 110]
print(filter_orders(test_data))
