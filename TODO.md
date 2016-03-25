TO-DO
2016-03-25:
There are 4 parts heavily related but the code doesn't reflect it.
Courses-Groups-Gropings-Enrollments

- There could be several courses (academic levels)

- Each group is related to a course. FIXME: This is not taken into account at the model level.

- Each group have a set of students and a tutor (teacher)

- A student can only be in a group

- It should be possible when adding students to a group only show students enrolled in the group's course

- Grouping is the "teaching unit" a set of students that have a subject together at the same time.

- Each group has a grouping of the same name FIXME: How to make this relation work properly: Now when a group is created a grouping with the same name is also created. But nothing happens when a student is added/removed or a group/grouping removed.The models don't reflect this relation.

- A student can be in more than a grouping

- Gropings can be related to more than a group and course. (In my school are a few religion students and the ones of 1st and 2nd grades are together in the same class.)

- Enrollments track which student is in which course and what ar it's subjects.

Groups, Groupings and Enrollments have a year field, because they change each school year.

There has to be a way to track what year is the application working in, for not have to choose the same each time. Managers will have to change their working year to desing the next one or to finish the previous. Maybe an app to track key-value settings:
workingyear = 2015-2016