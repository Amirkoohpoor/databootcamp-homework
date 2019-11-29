CREATE TABLE "departments" (
    "dept_no" varchar   NOT NULL,
    "dept_name" varchar   NOT NULL,
    CONSTRAINT "pk_departments" PRIMARY KEY (
        "dept_no"
     )
);

CREATE TABLE "dept_emp" (
    "emp_no" int   NOT NULL,
    "dept_no" varchar   NOT NULL,
    "from_date" date   NOT NULL,
    "to_date" date   NOT NULL
);

CREATE TABLE "dept_manager" (
    "dept_no" varchar   NOT NULL,
    "emp_no" int   NOT NULL,
    "from_date" date   NOT NULL,
    "to_date" date   NOT NULL
);

CREATE TABLE "employees" (
    "emp_no" int   NOT NULL,
    "birth_date" date   NOT NULL,
    "first_name" varchar   NOT NULL,
    "last_name" varchar   NOT NULL,
    "gender" varchar   NOT NULL,
    "hire_date" date   NOT NULL,
    CONSTRAINT "pk_employees" PRIMARY KEY (
        "emp_no"
     )
);

CREATE TABLE "salaries" (
    "emp_no" int   NOT NULL,
    "salaries" int   NOT NULL,
    "from_date" date   NOT NULL,
    "to_date" date   NOT NULL
);

CREATE TABLE "titles" (
    "emp_no" int   NOT NULL,
    "title" varchar   NOT NULL,
    "from_date" date   NOT NULL,
    "to_date" date   NOT NULL
);

ALTER TABLE "dept_emp" ADD CONSTRAINT "fk_dept_emp_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "dept_emp" ADD CONSTRAINT "fk_dept_emp_dept_no" FOREIGN KEY("dept_no")
REFERENCES "departments" ("dept_no");

ALTER TABLE "dept_manager" ADD CONSTRAINT "fk_dept_manager_dept_no" FOREIGN KEY("dept_no")
REFERENCES "departments" ("dept_no");

ALTER TABLE "dept_manager" ADD CONSTRAINT "fk_dept_manager_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "salaries" ADD CONSTRAINT "fk_salaries_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "titles" ADD CONSTRAINT "fk_titles_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

select * from employees
join dept_emp
on employees.emp_no = dept_emp.emp_no
join dept_manager
on employees.emp_no = dept_manager.emp_no
join salaries
on employees.emp_no = salaries.emp_no
join titles
on employees.emp_no = titles.emp_no

1. List the following details of each employee: employee number, last name, first name, gender, and salary.
select employees.emp_no, last_name, first_name, gender, salaries 
from employees
inner join salaries on employees.emp_no = salaries.emp_no

2. List employees who were hired in 1986.
select * from employees
where hire_date > '1986-01-01' and hire_date < '1986-12-30'


3. List the manager of each department with the following information:
department number, department name, 
the manager's employee number, last name, 
first name, and start and end employment dates'.
select dept_manager.dept_no, dept_name, employees.emp_no, last_name, first_name, from_date, to_date 
from employees
inner join dept_manager on employees.emp_no = dept_manager.emp_no
inner join departments on dept_manager.dept_no = departments.dept_no

4. List the department of each employee with the following information:
employee number, last name, first name, and department name.
select employees.emp_no,last_name,first_name, dept_name 
from employees
inner join dept_emp on employees.emp_no = dept_emp.emp_no
inner join departments on dept_emp.dept_no = departments.dept_no

5. List all employees whose first name is "Hercules" and last names begin with "B."
select * from employees
where first_name = 'Hercules' and last_name like 'B%'

6. List all employees in the Sales department, including their employee number,
last name, first name, and department name.
select employees.emp_no,last_name,first_name, dept_name 
from employees
inner join dept_emp on employees.emp_no = dept_emp.emp_no
inner join departments on dept_emp.dept_no = departments.dept_no
where dept_name = 'Sales'


7. List all employees in the Sales and Development departments,
including their employee number, last name, first name, and department name.
select employees.emp_no,last_name,first_name, dept_name 
from employees
inner join dept_emp on employees.emp_no = dept_emp.emp_no
inner join departments on dept_emp.dept_no = departments.dept_no
where dept_name = 'Sales' or dept_name = 'Development'

8. In descending order, list the frequency count of employee last names,
i.e., how many employees share each last name.
select distinct(last_name)
from employees 
order by last_name DESC

