import lxml
from lxml import html
from bs4 import BeautifulSoup

# Fill this with the elements you want to inject into the file
elements_to_inject = []

# Which file do you want to add the new elements to
file_to_inject_new_elements_to = input("Welcome to ELEMENTS INJECTOR!\nWhich file do you want to inject the new elements into?")

# Opens the file you told it to manipulate
with open(file_to_inject_new_elements_to) as the_file:
  txt = the_file.read()
  soup = BeautifulSoup(txt, 'lxml')

# The wrapping element we are going to target
element_wrappers = soup.find_all('p', attrs={'class': 'email-wrapper'})

# Create the tag of the new element
new_element = soup.new_tag('a')

# Increment variable
i = 0

# Loop through all the element wrappers
for element_wrapper in element_wrappers:
  # Append our new element and its values from the elements_to_inject array
  element_wrapper.append(soup.new_tag('a', attrs={'href': elements_to_inject[i]}))
  # Increment by 1 on each pass
  i += 1

# Used for testing
# print(soup)

# Write the output as a new file named output.html
with open("output.html", "w", encoding='utf-8') as file:
    file.write(str(soup))
