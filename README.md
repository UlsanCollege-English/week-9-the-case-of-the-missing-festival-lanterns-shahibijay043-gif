[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/QtC5AQlU)
# Week 9 Homework: The Case of the Missing Festival Lanterns


## Student Info

Name: SHAHI BIJAY
Student number: 2412083 
GitHub username: Your Shahibijay043 

---

## Summary

In this assignment, I practiced working with sets, dictionaries, tuples, and data analysis in Python.
I implemented a system to track lantern records, detect duplicates, identify missing and unexpected lanterns, count lanterns by section, and verify correct placement.
This project helped me improve my understanding of collection-based problem solving, dictionary management, and data validation techniques.
I also learned how to carefully handle edge cases while keeping the code clean, readable, and organized.

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

Approach
seen_lanterns
I used a set to track all lanterns that appeared in the festival log.
duplicate_lanterns
I checked whether a lantern had already been seen before adding it to the duplicate set.
count_by_section
I used a dictionary to count how many lanterns appeared in each festival section.
wrong_section_lanterns
I compared actual sections with expected sections and stored mismatched entries.
missing_lanterns
I used set difference to find lanterns that were expected but never seen.
unexpected_lanterns
I used set difference to find lanterns that appeared unexpectedly in the log.