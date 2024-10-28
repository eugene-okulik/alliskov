-- Добавление нового студента
insert into students (name, second_name, group_id) 
values ('Jason', 'Voorhees', null);
	
-- Добавление новых книг
insert into books (title, taken_by_student_id)
values
('The Jungle Book', (select s.id from students s where s.name = 'Jason' and s.second_name = 'Voorhees')),
('It', (select s.id from students s where s.name = 'Jason' and s.second_name = 'Voorhees')),
('Harry Potter and Automated Testing in Python', (select s.id from students s where s.name = 'Jason' and s.second_name = 'Voorhees'));

-- Добавление новой группы
insert into `groups` (title, start_date, end_date)
values ('Dumb and Dumber', 2024, 2026);

-- Закрепление студента в группе
update students
set group_id = (
	select g.id from `groups` g
	where g.title = 'Dumb and Dumber'
	)
where name = 'Jason'
and second_name = 'Voorhees';

-- Добавление учебных предметов
insert into subjets (title)
values ('Fishing for Dummies'), ('Advanced Elven'), ('Skyboarding');

select * from subjets s
where s.title in ('Fishing for Dummies', 'Advanced Elven', 'Skyboarding');

-- Добавление занятий по предметам
insert into lessons (title, subject_id)
values
('Small Fishes', (select s.id from subjets s where s.title = 'Fishing for Dummies')),
('Fishing Rods Types', (select s.id from subjets s where s.title = 'Fishing for Dummies')),
('Elven For Job Interviews', (select s.id from subjets s where s.title = 'Advanced Elven')),
('Elven For Vacation Trip', (select s.id from subjets s where s.title = 'Advanced Elven')),
('Safety Equipment', (select s.id from subjets s where s.title = 'Skyboarding')),
('Board Handling', (select s.id from subjets s where s.title = 'Skyboarding'));

-- Добавление студенту оценок по занятиям
insert into marks (value, lesson_id, student_id)
values
(
'4',
(select l.id from lessons l where l.title = 'Small Fishes'),
(select s.id from students s where s.name = 'Jason' and s.second_name = 'Voorhees')
),
(
'2',
(select l.id from lessons l where l.title = 'Fishing Rods Types'),
(select s.id from students s where s.name = 'Jason' and s.second_name = 'Voorhees')
),
(
'5',
(select l.id from lessons l where l.title = 'Elven For Job Interviews'),
(select s.id from students s where s.name = 'Jason' and s.second_name = 'Voorhees')
),
(
'5',
(select l.id from lessons l where l.title = 'Elven For Vacation Trip'),
(select s.id from students s where s.name = 'Jason' and s.second_name = 'Voorhees')
),
(
'3',
(select l.id from lessons l where l.title = 'Safety Equipment'),
(select s.id from students s where s.name = 'Jason' and s.second_name = 'Voorhees')
),
(
'2',
(select l.id from lessons l where l.title = 'Board Handling'),
(select s.id from students s where s.name = 'Jason' and s.second_name = 'Voorhees')
);

-- Получить все оценки студента
select * from marks m
where m.student_id = (
	select s.id from students s
	where s.name = 'Jason'
	and s.second_name = 'Voorhees');

-- Получить все книги, находящиеся у студента
select * from books b
where b.taken_by_student_id = (
	select s.id from students s
	where s.name = 'Jason'
	and s.second_name = 'Voorhees');

-- Получить всю информацию о студенте
select s.name as 'First Name', s.second_name as 'Second Name',
b.title as 'Books Taken By The Student', g.title as 'Student\'s Group Title',
m.value as 'Marks', l.title as 'Lesson Name', s2.title as 'Subject Name'
from students s
join books b on b.taken_by_student_id = s.id
join `groups` g on g.id = s.group_id
join marks m on m.student_id = s.id
join lessons l on l.id = m.lesson_id
join subjets s2 on s2.id = l.subject_id
where s.name = 'Jason'
and s.second_name = 'Voorhees';
