#Data gathering step: Extracting the data
def get_rentals_by_store_date(engine):
    import pandas as pd
    query = '''select 
    s.store_id as store_id, 
    date_format(p.payment_date,'%%Y-%%m-%%d') as Date, 
    count(p.rental_id) as Rentals,
    sum(p.amount) as Benefit
    from sakila.store as s
    join sakila.payment as p
    on s.manager_staff_id = p.staff_id
    group by store_id, Date
    having year(Date) = 2005
    order by Date;'''
    data = pd.read_sql_query(query, engine)
    return data

def get_top5_titles_by_store(engine):
    import pandas as pd
    query = '''select * from (
    select store_id, title, Rentals, row_number() over(partition by store_id) as Ranking from
    (select i.store_id, f.title, count(r.rental_id) as Rentals  from sakila.rental as r
    join sakila.payment as p
    on r.rental_id = p.rental_id
    join sakila.inventory as i
    on r.inventory_id = i.inventory_id
    join sakila.film as f
    on i.film_id = f.film_id
    group by store_id, title
    order by store_id, Rentals desc) as s1) as s2
    where Ranking <= 5;'''
    data = pd.read_sql_query(query, engine)
    return data



