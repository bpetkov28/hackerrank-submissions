SELECT
    CASE 
        WHEN A = B AND B = C THEN 'Equilateral'
        WHEN ((A = B AND B != C) OR (A = C AND C != B) OR (C = B AND B != A)) AND (A + B > C) AND (A + C > B) AND (B + C > A) THEN 'Isosceles'
        WHEN A != B AND B != C AND C != A AND (A + B > C) AND (A + C > B) AND (B + C > A) THEN 'Scalene'
        ELSE 'Not A Triangle'
    END
FROM TRIANGLES;