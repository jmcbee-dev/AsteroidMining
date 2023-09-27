DROP TABLE IF EXISTS c_type;
DROP TABLE IF EXISTS s_type;
DROP TABLE IF EXISTS m_type;
DROP TABLE IF EXISTS unkown;
DROP TABLE IF EXISTS asteroid_data;
CREATE TABLE asteroid_data (
    id VARCHAR(1024),
    spkid SERIAL,
    full_name VARCHAR(255),
    pdes VARCHAR(50),
    name VARCHAR(255),
    prefix VARCHAR(1),
    neo BOOLEAN,
    pha BOOLEAN,
    H FLOAT,
    diameter FLOAT,
    albedo FLOAT,
    diameter_sigma FLOAT,
    orbit_id VARCHAR(20),
    epoch FLOAT,
    epoch_mjd FLOAT,
    epoch_cal FLOAT,
    equinox VARCHAR(6),
    e FLOAT,
    a FLOAT,
    q FLOAT,
    i FLOAT,
    om FLOAT,
    w FLOAT,
    ma FLOAT,
    ad FLOAT,
    n FLOAT,
    tp FLOAT,
    tp_cal FLOAT,
    per FLOAT,
    per_y FLOAT,
    moid FLOAT,
    moid_ld FLOAT,
    sigma_e FLOAT,
    sigma_a FLOAT,
    sigma_q FLOAT,
    sigma_i FLOAT,
    sigma_om FLOAT,
    sigma_w FLOAT,
    sigma_ma FLOAT,
    sigma_ad FLOAT,
    sigma_n FLOAT,
    sigma_tp FLOAT,
    sigma_per FLOAT,
    class VARCHAR(50),
    rms FLOAT,
    PRIMARY KEY (spkid)
)

--\copy aseteroid_data from dataset.csv csv header;

-- Find probable C-type Asteroids
-- These are mostly carbonous and the most common


SELECT id, diameter, a as semi_major, q as perihelion 
INTO TABLE c_type
FROM asteroid_data
WHERE albedo < 0.10;


-- Find probable M-type Asteroids

SELECT id, diameter, a as semi_major, q as perihelion 
INTO TABLE m_type
FROM asteroid_data
WHERE albedo > 0.10 AND albedo < 0.20;

-- Find probable S-type Asteroids

SELECT id, diameter, a as semi_major, q as perihelion 
INTO TABLE s_type
FROM asteroid_data
WHERE albedo > 0.20;
