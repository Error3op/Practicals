Step 1: Create the 'students' Table
CREATE TABLE students ( id INT, name VARCHAR(50), age INT, class VARCHAR(20));

Step 2: Create a Sequence Named 'stu'
CREATE SEQUENCE stu START WITH 1
INCREMENT BY 1
MINVALUE 1
MAXVALUE 100
NOCYCLE;

Step 3: Insert Values Using the sequence
INSERT INTO students VALUES ( stu.NEXTVAL, 'Alice', 20, 'CS');

INSERT INTO students VALUES ( stu.NEXTVAL,'Bob', 21, 'IT');

Step 4: Query the Table to View All Records
SELECT * FROM students;

-- Program to find the area of a circle in PL/SQL
DECLARE
    pi CONSTANT number := 3.14;
    r number := 5;
    a number;
begin
    a := pi * r * r;
    dbms_output.put_line('Area is' || ' ' || a);
end;

-- Conversion from character to number and number to character
DECLARE
    age1 varchar(20) := '20';
    age2 varchar(20) := '26';
    age3 number;
    age4 varchar(20);
begin
    dbms_output.put_line('value of age 1 ' || age1);
    dbms_output.put_line('value of age 2 ' || age2);
    age3 := to_number(age1);
    age3 := age3 - 2;
    dbms_output.put_line('value of age 3 ' || age3);
    age4 := to_char(age3);
    dbms_output.put_line('value of age 4 ' || age4);
end;

-- Scope of variables in PL/SQL
DECLARE
    n1 number := 20;
begin
    dbms_output.put_line(n1);
    declare
        n2 number := 80;
    begin
        dbms_output.put_line(n1);
        dbms_output.put_line(n2);
    end;
end;

-- PL/SQL Records
DECLARE
    Type m_emp_rec IS RECORD (code number(4), name varchar2(15), tel_no Number);
    emp m_emp_rec;
BEGIN
    emp.code := 10;
    emp.name := 'Raj';
    emp.tel_no := 765423;
    Dbms_output.put_line('Code' || 'Name' || 'Telephone Number');
    Dbms_output.put_line(emp.code || emp.name || emp.tel_no);
END;

-- Write a program to retrieve data from a database & store it in a record

CREATE TABLE Cus1 (
    cust_code NUMBER(4),
    cust_name VARCHAR2(15),
    tel_no NUMBER
);

INSERT INTO Cus1 VALUES (10, 'John Doe', 123456789);

DECLARE
    Type Cust_info IS RECORD (code number(4), name varchar2(15), telephone Number);
    Cus Cust_info;
BEGIN
    SELECT cust_code, cust_name, tel_no INTO cus
    FROM Cus1
    WHERE cust_code = 10;
    Dbms_output.put_line('CODE' || 'NAME' || 'TELEPHONE');
    DBMS_OUTPUT.NEW_LINE;
    Dbms_output.put_line(cus.code || cus.name || cus.telephone);
END;

-- Addition of two Variables
DECLARE
    a number := 75;
    b number := 87;
    c number;
BEGIN
    c := a + b;
    dbms_output.put_line(c);
END;

-- IF THEN ELSE
DECLARE
    salary Number := 9000;
BEGIN
    IF salary < 50000 THEN
        salary := salary + 15000;
    ELSE
        salary := salary + 5000;
    END IF;
    DBMS_OUTPUT.PUT_LINE(salary);
END;

-- IF - THEN - ELSIF - ELSE
DECLARE
    marks number;
begin
    marks := &marks;
    IF marks >= 80 THEN
        dbms_output.put_line('grade is a');
    ELSIF marks >= 60 THEN
        dbms_output.put_line('grade is b');
    ELSIF marks >= 50 THEN
        dbms_output.put_line('grade is f');
    ELSE
        dbms_output.put_line('grade is c');
    END IF;
END;

-- LOOP
DECLARE
    i NUMBER := 1;
BEGIN
    LOOP
        DBMS_OUTPUT.PUT_LINE ('Value of i: ' || i);
        i := i + 1;
        EXIT WHEN i > 10;
    END LOOP;
END;

-- Program Name: WHILE loop

DECLARE
  val number(2):=10;
BEGIN
  WHILE val<30
  LOOP
    Dbms_output.put_line ('val'|| ' '||val);
    val:= val+10;
  END LOOP;
END;

-- Program Name: Even number

DECLARE
  counter number:= 1;
  n Number;
BEGIN
  WHILE counter <=12
  LOOP
    counter := counter+1;
    n := counter;
    IF mod(n,2) !=0 THEN
      CONTINUE;
    END IF;
    Dbms_output.put_line (n|| ' '||'Even number');
  END LOOP;
END;

-- Program Name: For Loop

DECLARE
  v0 number:=1;
  v1 number:=1;
  v2 number;
BEGIN
  Dbms_output.put_line (v0||' '||v1);
  v0:=v1;
  FOR i in 3..10 LOOP
    v2 := v0+v1;
    Dbms_output.put_line(v2);
    v0:=v1;
    v1:=v2;
  END LOOP;
END;

-- Program Name: CURSOR
CREATE TABLE INVENTORY (
    inv_no NUMBER PRIMARY KEY,      -- Inventory number, primary key
    iname VARCHAR2(10),             -- Item name
    unit_price NUMBER               -- Unit price of the item
);

DECLARE
  CURSOR c2 IS
    SELECT inv_no FROM inventory ORDER BY inv_no ASC;
    minvo INVENTORY.inv_no%type;
BEGIN
  OPEN c2;
  IF (c2%ISOPEN) THEN
    Dbms_output.put_line ('CURSOR IS OPEN ALREADY');
  END IF;
  FETCH c2 INTO minvo;
  Dbms_output.put_line (minvo);
  CLOSE c2;
END;

-- Program Name: CURSOR

DECLARE
  CURSOR c2 IS
    SELECT * FROM INVENTORY ORDER BY inv_no ASC;
    inv_rec c2%rowtype;
BEGIN
  OPEN c2;
  LOOP
    FETCH c2 INTO inv_rec;
    Dbms_output.put_line (inv_rec.inv_no|| ' '|| inv_rec.iname);
    EXIT WHEN (c2%rowcount =6);
  END LOOP;
  CLOSE c2;
END;

-- Program Name: CURSOR

CREATE TABLE INFORM (Cust_code int, organization varchar2 (10), salary int);

DECLARE
  CURSOR c1 is SELECT cust_code, salary, organization
               FROM INFORM ORDER BY cust_code asc;
BEGIN
  FOR rec in c1
  LOOP
    IF (c1%rowcount =1)
    THEN
      IF (rec.salary >90000) AND (rec.organization='Gamma')
      THEN
        UPDATE INFORM SET
        salary = salary +1000
        WHERE cust_code = rec.cust_code;
      END IF;
    END IF;
    IF (c1%rowcount =4)
    THEN
      IF (rec.organization ='self')
      THEN
        UPDATE INFORM SET salary = salary-2000
        WHERE cust_code = rec.cust_code;
      END IF;
    END IF;
  END LOOP;
END;

-- Program Name: NOTFOUND

DECLARE
  CURSOR c2 IS
    SELECT inv_no FROM INVENTORY where iname= 'INV7';
    minvo INVENTORY.inv_no%type;
BEGIN
  OPEN c2;
  FETCH c2 INTO minvo;
  IF (c2%NOTFOUND)
  THEN
    Dbms_output.put_line ('NO record with iname-INV7');
  ELSE Dbms_output.put_line ('Inventory found');
  END IF;
  CLOSE c2;
END;

-- Program Name: Flight

CREATE TABLE Flight ( Flight_NO int ,
                      Flight_name Varchar2(16),
                      Source varchar (17), Destination varchar(24));

DECLARE
  Cursor c1 is select flight_no,source,
               destination from flight for update of
               source;
  flight_s c1%rowtype;
BEGIN
  Open c1;
  LOOP
    FETCH c1 into flight_s;
    EXIT WHEN c1%NOTFOUND;
    IF (flight_s.source='delhi')
    THEN update flight set
      source = 'newdelhi'
      WHERE current of c1;
    END IF;
  END LOOP;
  CLOSE c1;
END;

-- Program Name: Exception

DECLARE
  mcode journey.p_code%type;
  m_perdiscount journey.PER_DISCOUNT%type;
  low_discount EXCEPTION;
BEGIN
  SELECT p_code, per_discount into mcode,
  m_perdiscount
  FROM JOURNEY
  WHERE p_code =:p_code;
  IF (m_perdiscount <20)
  THEN
    raise low_discount;
  ELSE
    Dbms_output.put_line(mcode|| ' '||'discount percent'|| ' '|| m_perdiscount);
  END IF;
EXCEPTION
  WHEN low_discount THEN
    Dbms_output.put_line (mcode|| ' '||'low discount');
END;

-- Program Name: Exception

DECLARE
  mbonus FLOAT;
  msalary inform.salary%type;
  mcustcode inform.cust_code%type;
  over_salary EXCEPTION;
BEGIN
  SELECT cust_code,salary INTO mcustcode,
         msalary FROM inform
         WHERE cust_code =20;
  IF (msalary > 98000)
  THEN
    raise over_salary;
  ELSE
    mbonus := msalary* .20;
    msalary := msalary + mbonus;
    Dbms_output.put_line ( mcustcode|| ' '||
    msalary|| ' '|| mbonus);
  END IF;
EXCEPTION
  WHEN over_salary
  THEN
    msalary := msalary +500;
    Dbms_output.put_line ('over salary'|| ' '||
    mcustcode|| ' '||msalary|| ' '|| 'No Bonus');
  WHEN OTHERS
  THEN
    Dbms_output.put_line ('salary out of range');
END;
-- Program Name: PROCEDURE

CREATE OR REPLACE PROCEDURE Bonus(pcust_code IN NUMBER, mbonus OUT number) AS
  msalary FLOAT;
  mcode number;
BEGIN
  SELECT cust_code, salary INTO mcode, msalary
  FROM inform
  WHERE cust_code = pcust_code;
  mbonus := msalary * .10;
  Dbms_output.put_line ('mcode'|| ' '||mcode||' '|| 'mbonus'|| ' '||mbonus);
END Bonus;

DECLARE
  gbonus number(6);
BEGIN
  Bonus(10, gbonus);
  Dbms_output.put_line ('gbonus:'|| ' '||gbonus);
END;
-- Program Name: PROCEDURE - Calculate Area of Circle

CREATE OR REPLACE PROCEDURE area_of_circle(
  r IN NUMBER, area OUT NUMBER) AS
  CONSTANT pi := 3.14;
BEGIN
  area := pi * r * r;
  DBMS_OUTPUT.PUT_LINE ('area_of_circle'|| ' '||area);
END;

DECLARE
  r NUMBER := 5;
  area NUMBER;
BEGIN
  area_of_circle (r, area);
  DBMS_OUTPUT.PUT_LINE ('Area:'|| ' '||area);
END;
-- Program Name: PROCEDURE - Add Two Numbers

CREATE OR REPLACE PROCEDURE add_numbers(
  a IN NUMBER, b IN NUMBER, result OUT NUMBER) AS
BEGIN
  result := a + b;
END;

DECLARE
  a NUMBER := 5;
  b NUMBER := 7;
  result NUMBER;
BEGIN
  add_numbers(a, b, result);
  DBMS_OUTPUT.PUT_LINE ('result :'|| ' '||result);
END;
-- Program Name: TRIGGER

CREATE TABLE Trans1(Cust_code int, invoice int, qty int, amt int);

-- Insert Sample Data
INSERT INTO Trans1 VALUES (11, 23, 4, 1234);
INSERT INTO Trans1 VALUES (12, 34, 5, 3234);

CREATE TABLE Trans_changes(Cust_code int, amt int);

CREATE OR REPLACE TRIGGER T_transaction1
AFTER INSERT ON Trans1
FOR EACH ROW
DECLARE
BEGIN
  INSERT INTO Trans_changes(Cust_code, amt)
  VALUES(:new.Cust_code, :new.amt);
END T_transaction1;
-- Program Name: TRIGGER - Passenger Fare Update

CREATE TABLE passengers(pass_code int, flight_no int, pass_name varchar(20), fare int);

-- Insert Sample Data
INSERT INTO passengers VALUES (23, 42, 'she', 78);
INSERT INTO passengers VALUES (83, 41, 'vai', 79);

CREATE TABLE t_fare(pass_code int, fare int);

CREATE OR REPLACE TRIGGER t_fares
AFTER INSERT OR UPDATE ON passengers
FOR EACH ROW
BEGIN
  IF (:new.fare != :old.fare) THEN
    INSERT INTO t_fare(pass_code, fare)
    VALUES (:new.pass_code, :new.fare);
  END IF;
END;

-- Update Sample Data
UPDATE passengers SET fare=19000 WHERE pass_code=23;
