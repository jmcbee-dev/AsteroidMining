-- General counts of likely asteroids types

SELECT *, (a_data - c_type - m_type - s_type) AS unkown 
FROM (
    SELECT 
    (
        SELECT count(*)
        FROM c_type
    )   AS c_type,
    (
        SELECT count(*) 
        FROM m_type
    )   AS m_type,
    (
        SELECT count(*)
        FROM s_type
    )   AS s_type,
    (
        SELECT count(*)
        FROM asteroid_data
    )   AS a_data
) AS a;

-- Approximating the amount of materials
-- that could be expected from mining


SELECT 
    -- c_type approx volume in km^3
    (
        SELECT SUM(4*PI()*POWER((diameter/2),3)/3)
        FROM c_type
    )   AS volume_c,

    -- m_type approx volume in km^3
    (   
        SELECT SUM(4*PI()*POWER((diameter/2),3)/3)
        FROM m_type
    )   AS volume_m,

    -- s_type approx volume in km^3
    (
        SELECT SUM(4*PI()*POWER((diameter/2),3)/3)
        FROM s_type
    )   AS volume_s,
    
    -- remaining volume of unkown type
    (        
        SELECT SUM(4*PI()*POWER((diameter/2),3)/3)
        FROM unkown
    )   AS volume_u
