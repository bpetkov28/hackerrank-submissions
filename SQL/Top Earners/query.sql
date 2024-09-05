SELECT MAX(Salary*Months) AS total_earnings, COUNT(employee_id) FROM Employee
WHERE Salary*Months = (SELECT MAX(Salary*Months) FROM Employee);