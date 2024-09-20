create table students(
id int AUTOINCREMENT(1,1),
name varchar(50)
);

insert into students(name) values('ram'),('bheem'),('shyam'),('sraavs'),('kousi');
select * from students;


with cte as (
select *, lead(id) over(order by id) as next_id,
lead(name) over(order by id) as next_student,

lag(name) over(order by id) as last_student
from students
)

select id, 
    case when id%2 != 0 and next_id is not null and next_id % 2 = 0 then next_student
        when id%2 = 0 and next_id is not null and next_id % 2 != 0 then last_student
        else name end as name_of_student
from cte;
