-- 1. Отримати всі завдання певного користувача
select *
from tasks
where user_id = 1;

-- 2. Вибрати завдання за певним статусом
select *
from tasks
where status_id = (
		select id from status where name = 'new'
);

-- 3. Оновити статус конкретного завдання
update tasks
set status_id = (
    select id from status where name = 'in progress'
)
where id = 1;

-- 4. Отримати список користувачів, які не мають жодного завдання
select *
from users
where id not in (select distinct user_id from tasks);

-- 5. Додати нове завдання для конкретного користувача
insert into tasks (title, description, status_id, user_id)
values (
    'New task',
    'New created task',
    (select id from status where name = 'new'),
    1
);

-- 6. Отримати всі завдання, які ще не завершено
select *
from tasks
where status_id = (
		select id from status where name != 'completed'
);

-- 7. Видалити конкретне завдання
delete from tasks 
where id = 1;

-- 8. Знайти користувачів з певною електронною поштою
select *
from users
where email like '%example%';

-- 9. Оновити ім'я користувача
update users
set fullname = 'Justin Reye'
where fullname = 'Justin Reyes';

-- 10. Отримати кількість завдань для кожного статусу
with grouped_tasks as (
    select 
        status_id,
        count(id) as task_count
    from tasks
    group by status_id
)
select
    s.name as status,
    gt.task_count
from status s 
inner join grouped_tasks gt 
    on s.id = gt.status_id
order by gt.task_count desc;

-- 11. Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти
select *
from tasks
where user_id in (
	select id from users
	where email like '%example%'
);

-- 12. Отримати список завдань, що не мають опису
select *
from tasks
where description is null
	or description = '';

-- 13. Вибрати користувачів та їхні завдання, які є у статусі 'in progress'
select
    u.id as user_id,
    u.fullname,
    t.id as task_id,
    t.title,
    t.description
from users u
inner join tasks t
    on u.id = t.user_id
inner join status s
    on t.status_id = s.id
where s.name = 'in progress';

-- 14. Отримати користувачів та кількість їхніх завдань
select
    u.id as user_id,
    u.fullname,
    u.email,
    count(t.id) as task_count
from users u
left join tasks t
    on u.id = t.user_id
group by
    u.id,
    u.fullname,
    u.email
order by task_count desc;
