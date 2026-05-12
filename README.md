[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/QtC5AQlU)
# Week 9 Homework: The Case of the Missing Festival Lanterns


## Student Info

Name: SHAHI BIJAY
Student number: 2412083 
GitHub username: Your Shahibijay043 

---

## Summary

This program analyzes lantern activity during the festival and creates a report about the lantern data.  
The function receives expected lanterns, a lantern log, and the correct section for each lantern.  
It checks which lanterns were seen, missing, duplicated, unexpected, or placed in the wrong section.  
The program also counts how many lanterns appeared in each section.  
The final result is returned as a dictionary containing all analysis information.

---

## Approach

- First, I created sets and dictionaries to store lantern information.
- During the loop, I checked whether a lantern was already seen to detect duplicates.
- I counted how many lanterns appeared in each section using a dictionary.
- I checked whether lanterns were placed in the correct section.
- After the loop, I used set difference operations to find missing and unexpected lanterns.
- Finally, I returned all results inside one dictionary.

---

## How I Used Dictionaries and Sets

1. Which parts of your solution used sets?

- I used sets for `seen_lanterns`, `missing_lanterns`, `unexpected_lanterns`, and `duplicate_lanterns`.

2. Which parts of your solution used dictionaries?

- I used dictionaries for `count_by_section` and `wrong_section_lanterns`.

3. Why were dictionaries or sets better than using only lists?

- Sets made it easy to avoid duplicates and quickly compare lantern groups.
- Dictionaries made it easier to store counts and section information using keys.
- They were faster and cleaner than using only lists.

Your explanation:

```text
Sets were useful for checking duplicates and comparing lantern collections.
Dictionaries were useful for storing section counts and wrong section details.
Using dictionaries and sets made the solution simpler and more efficient.

Time complexity: O(n)
Space complexity: O(n)

Explanation:
The program loops through lantern_log one time.
There are no nested loops in the solution.
Extra sets and dictionaries are created to store seen lanterns,
duplicates, counts, and wrong section information.