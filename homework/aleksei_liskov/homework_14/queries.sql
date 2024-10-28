-- Добавление нового студента
insert into students (name, second_name, group_id) 
values ('Jason', 'Voorhees', null);
	
-- Добавление новых книг
insert into books (title, taken_by_student_id)
values
('The Jungle Book', 3488),
('It', 3488),
('Harry Potter and Automated Testing in Python', 3488);

-- Добавление новой группы
insert into `groups` (title, start_date, end_date)
values ('Dumb and Dumber', 2024, 2026);

-- Закрепление студента в группе
update students
set group_id = 2176
where id = 3488;

-- Добавление учебных предметов
insert into subjets (title)
values ('Fishing for Dummies'), ('Advanced Elven'), ('Skyboarding');

-- Добавление занятий по предметам
insert into lessons (title, subject_id)
values
('Small Fishes', 3206),
('Fishing Rods Types', 3206),
('Elven For Job Interviews', 3207),
('Elven For Vacation Trip', 3207),
('Safety Equipment', 3208),
('Board Handling', 3208);

-- Добавление студенту оценок по занятиям
insert into marks (value, lesson_id, student_id)
values
('4', 6563, 3488),
('2', 6564, 3488),
('5', 6565, 3488),
('5', 6566, 3488),
('3', 6567, 3488),
('2', 6568, 3488);

-- Получить все оценки студента
select * from marks m
where m.student_id = 3488;

-- Получить все книги, находящиеся у студента
select * from books b
where b.taken_by_student_id = 3488;

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
where s.id = 3488;
