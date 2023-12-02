DROP TABLE IF EXISTS public.items CASCADE;
DROP SEQUENCE IF EXISTS public.items_id_seq;
DROP TABLE IF EXISTS public.orders CASCADE;
DROP SEQUENCE IF EXISTS public.orders_id_seq;
DROP TABLE IF EXISTS public.items_orders CASCADE;
DROP SEQUENCE IF EXISTS public.items_orders_id_seq;


CREATE SEQUENCE IF NOT EXISTS public.items_id_seq;
CREATE TABLE public.items (
    id SERIAL PRIMARY KEY,
    name text,
    unit_price real,
    quantity int
);

-- Create the second table.
CREATE SEQUENCE IF NOT EXISTS public.orders_id_seq;
CREATE TABLE public.orders (
    id SERIAL PRIMARY KEY,
    customer_name text,
    order_date DATE 
);

-- Create the join table.
CREATE SEQUENCE IF NOT EXISTS public.items_orders_id_seq;
CREATE TABLE public.items_orders (
    item_id int,
    order_id int,
    constraint fk_item foreign key(item_id) references items(id) on delete cascade,
    constraint fk_order foreign key(order_id) references orders(id) on delete cascade,
    PRIMARY KEY (item_id, order_id)
);


INSERT INTO public.items (name, unit_price, quantity) VALUES
('Coffee Grinder', 19.99, 20),
('Coffee Beans', 11.99, 10),
('Espresso Maker', 349.99, 13),
('Coffee Machine Cleaner', 24.50, 30);


INSERT INTO public.orders (customer_name, order_date) VALUES
('Yaz', '2023-10-22'),
('Ali', '2023-11-29'),
('Maya', '2023-11-20'),
('Ruby', '2023-12-1');

INSERT INTO public.items_orders (item_id, order_id) VALUES
(1, 1),
(1, 2),
(2, 3),
(2, 1),
(3, 3),
(3, 4),
(2, 4),
(4, 1),
(4, 2),
(4, 4);

