DECLARE @parameter INT;
SET @parameter = 20;
WHILE @parameter > 0
BEGIN
    SELECT
        REPLICATE('* ', @parameter);
    SET @parameter = @parameter - 1;
END;