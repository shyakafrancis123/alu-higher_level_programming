4. Only differents
mandatory
Write a function that returns a set of all elements present in only one set.

Prototype: def only_diff_elements(set_1, set_2):
You are not allowed to import any module
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
only_diff_elements = __import__('4-only_diff_elements').only_diff_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))

guillaume@ubuntu:~/$ ./4-main.py
['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: alu-higher_level_programming
Directory: python-more_data_structures
File: 4-only_diff_elements.py
