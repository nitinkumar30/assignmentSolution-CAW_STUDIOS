# importing necessary modules
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Define the URL of the webpage
url = "https://testpages.herokuapp.com/styled/tag/dynamic-table.html"

# Initialize a Chrome driver
driver = webdriver.Chrome()

# Open window in full screen window
driver.maximize_window()

# Launch the webpage
driver.get(url)

# Find the "Table Data" button using XPath
table_data_button = driver.find_element(By.XPATH, "//summary[text()='Table Data']")

# Click on the button to display the data input
table_data_button.click()

# Define the data to be entered
# data = '''[
#     {"name": "Bob", "age": 20, "gender": "male"},
#     {"name": "George", "age": 42, "gender": "male"},
#     {"name": "Sara", "age": 42, "gender": "female"},
#     {"name": "Conor", "age": 40, "gender": "male"},
#     {"name": "Jennifer", "age": 42, "gender": "female"}
# ]'''


with open('input_json.json', 'r') as f:
    data = json.load(f)


# Convert the data dictionary to a JSON string
data_str = json.dumps(data)


time.sleep(2)

# Find the input field for data using XPath
data_input = driver.find_element(By.XPATH, "//textarea[@id='jsondata']")

# Clear the input field if there exist any data in it
data_input.clear()

# Enter the defined data into the input field
data_input.send_keys(data_str)


time.sleep(5)

# Find the "Refresh Table" button using XPath
refresh_button = driver.find_element(By.XPATH, "//button[text()='Refresh Table']")

# Click the button to refresh the table with new data
refresh_button.click()

# Locate the table body using XPath
table_body = driver.find_element(By.XPATH, "//table[@id='dynamictable']")

# Extract all table rows using tag name
rows = table_body.find_elements(By.TAG_NAME, 'tr')

# Initialize an empty list to store the extracted data
table_data = []
# time.sleep(5)

# Loop through each row in the table
for row in rows:

    # Extract all table cells within each row using tag name
    cells = row.find_elements(By.TAG_NAME, 'td')

    # Initialize an empty list to store data from each row
    row_data = []

    # Loop through each cell in the current row
    for cell in cells:

        # Extract the text content of each cell
        row_data.append(cell.text)

    # Append the entire row_data list to the table_data list
    table_data.append(row_data)

time.sleep(5)
# Close the browser window
driver.quit()

# Define the expected data after removing the first element
expected_data = [[item['name'], str(item['age']), item['gender']] for item in data]

# Deleting the first element from original table data
del table_data[0]
print("Original data of table - \n", table_data)
print("Expected data of table - \n", expected_data)

# Assert that the extracted data is equal to the expected data
assert table_data == expected_data, "The data in the table does not match the expected data!"

# Print confirmation message
print("The data in the table matches the expected data!")
