"""Using a dictionary to representn an instructor's grade book."""

grade_book = {
	'Susan': [92,85,100],
	'Eduaro': [83,95,79],
	'Azzi': [91,89,82],
	'Alex': [97,91,92]
	}

all_grades_total = 0
all_grade_count = 0

for name, grades in grade_book.items():
	total = sum(grades)
	print(f'Average for{name} is {total/len(grades):.2f}')
	all_grades_total += total
	all_grade_count += len(grades)

print(f"Class's average is: {all_grades_total / all_grade_count:.2f}")

"""
Average forSusan is 92.33
Average forEduaro is 85.67
Average forAzzi is 87.33
Average forAlex is 93.33
Class's average is: 89.67
"""
