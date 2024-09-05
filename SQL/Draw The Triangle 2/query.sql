DECLARE @parameter INT
SET @parameter = 1;
WHILE @parameter < 21
BEGIN
    SELECT
        REPLICATE('* ', @parameter);
    SET @parameter = @parameter +1;
END;