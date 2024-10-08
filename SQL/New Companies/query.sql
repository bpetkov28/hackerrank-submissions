SELECT Company.company_code, Company.founder, COUNT(DISTINCT(Employee.lead_manager_code)), COUNT(DISTINCT(Employee.senior_manager_code)), COUNT(DISTINCT(Employee.manager_code)), COUNT(DISTINCT(Employee.employee_code))
FROM Company
INNER JOIN Employee
ON Company.company_code = Employee.company_code
GROUP BY Company.company_code, Company.founder;