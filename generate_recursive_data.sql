with recursive calender as(
select cast('2024-01-01' as date) as date_value,
1 as level
union all
select dateadd(day,1, date_value),
level+1
from rr
where date_value < '2024-12-31'
)
select date_value
from calender
order by 1;
