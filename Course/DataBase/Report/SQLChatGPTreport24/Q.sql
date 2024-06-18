CREATE TABLE MenuItem (
    mid INT,
    mname VARCHAR(255),
    mtype VARCHAR(255),
    price DECIMAL(10, 2),
    PRIMARY KEY (mid)
);

CREATE TABLE Guest (
    gid INT,
    tableid INT,
    PRIMARY KEY (gid)
);

CREATE TABLE Order (
    oid INT,
    gid INT,
    mid INT,
    quantity INT,
    date DATE,
    PRIMARY KEY (oid),
    FOREIGN KEY (gid) REFERENCES Guest(gid),
    FOREIGN KEY (mid) REFERENCES MenuItem(mid)
);

INSERT INTO MenuItem (mid, mname, mtype, price) 
VALUES (1, 'Burger', 'Main Course', 9.99), (2, 'Salad', 'Appetizer', 5.99), (3, 'Pizza', 'Main Course', 12.99), (4, 'Fries', 'Side Dish', 3.99);

INSERT INTO Guest (gid, tableid) 
VALUES (1, 10), (2, 5), (3, 8), (4, 3);

INSERT INTO Order (oid, gid, mid, quantity, date) 
VALUES (1, 1, 1, 2, '2022-01-01'), (2, 2, 2, 1, '2022-01-02'), (3, 3, 3, 3, '2022-01-03'), (4, 4, 4, 2, '2022-01-04');

WITH GuestOrderCount AS (
    SELECT o.mid, o.gid, COUNT(*) AS order_count
    FROM Order o
    GROUP BY o.mid, o.gid
),
MenuItemGuestCount AS (
    SELECT mid, COUNT(gid) AS guest_count
    FROM GuestOrderCount
    WHERE order_count = 1
    GROUP BY mid
)
SELECT mid, guest_count
FROM MenuItemGuestCount
ORDER BY guest_count DESC
LIMIT 1;