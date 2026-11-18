# Task: Deep Dictionary Navigation
# Instructions: Extract 'year'. If any key is missing, return "Unknown".

def get_vehicle_year(data):
    if 'specs' in vehicle and 'model_info' in vehicle['specs']:
    return(vehicle['specs']['model_info']['year'])
  else:
    return "Unknown"

# Test Case
vehicle = {'specs': {'model_info': {'year': 2024}}}
# Expected: 2024
print(get_vehicle_year(vehicle))
