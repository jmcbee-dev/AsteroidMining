import math

from matplotlib import pyplot as plt
import  psycopg2

conn = psycopg2.connect(database="postgres", user="jacob", password=None)
cursor = conn.cursor()

def execute_query(query):
    cursor.execute(query)
    return cursor.fetchall()

def count_plot():
    c = execute_query("""SELECT *, (a_data - c_type - m_type - s_type)
    AS
    unkown
    FROM(
        SELECT
            (
            SELECT
    count(*)
    FROM
    c_type
    )   AS
    c_type,
    (
        SELECT count( *)
    FROM
    m_type
    )   AS
    m_type,
    (
        SELECT count( *)
    FROM
    s_type
    )   AS
    s_type,
    (
        SELECT count( *)
    FROM
    asteroid_data
    )   AS
    a_data
    ) AS
    a;
    """)
    labels = 'C Type', 'M Type', 'S Type', 'Unkown'
    c_reduce = [e / c[0][3] for i, e in enumerate(c[0]) if i / 3 != 1]
    explode = (0.1, 0.1, 0.1, 0)
    fig, ax = plt.subplots()
    ax.pie(c_reduce, autopct='%1.1f%%', explode=explode)
    ax.axis('equal')
    ax.set_title('Total Known Asteroid Count')
    # plt.savefig("total_counts")
    return

def polar_plot():
    c = execute_query("""
    -- c_type 

        SELECT diameter, semi_major
        FROM c_type
        WHERE semi_major < 3 AND diameter IS NOT NULL
    """)
    s = execute_query("""
        -- s_type 

            SELECT diameter, semi_major
            FROM s_type
            WHERE semi_major < 3 AND diameter IS NOT NULL
        """)
    m = execute_query("""
            -- m_type 

                SELECT diameter, semi_major
                FROM m_type
                WHERE semi_major < 3 AND diameter IS NOT NULL
            """)

    r_c = []
    r_s = []
    r_m = []
    theta_c = []
    theta_m = []
    theta_s = []
    area_c = []
    area_s = []
    area_m = []
    count = 0
    for d, p in c:
        r_c.append(p)
        area_c.append((d / 2) ** 2 / 400)
        theta_c.append(2 * math.pi * count)
        count += 0.0073

    for d, p in s:
        r_s.append(p)
        area_s.append((d / 2) ** 2 / 400)
        theta_s.append(2 * math.pi * count)
        count += 0.0073

    for d, p in m:
        r_m.append(p)
        area_m.append((d / 2) ** 2 / 400)
        theta_m.append(2 * math.pi * count)
        count += 0.0073

    labels = 'C Type', 'M Type', 'S Type'

    fig = plt.figure()
    ax = fig.add_subplot(projection='polar')
    ax.set_xticklabels([])

    p = ax.scatter(theta_c, r_c, s=area_c, alpha=0.75, c="blue")
    p2 = ax.scatter(theta_s, r_s, s=area_s, alpha=0.75, c="green")
    p3 = ax.scatter(theta_m, r_m, s=area_m, alpha=0.75, c="red")
    earth = ax.scatter(theta_m[-1], [1.0], s=[50.0], alpha=1, c="black")
    sun = ax.scatter([0], [0.0], s=[600], alpha=1, c="yellow")
    ax.legend([p, p2, p3, earth, sun], ['C Type', 'S Type', 'M Type', 'Earth', 'Sun'])
    ax.set_title('Asteroid Distances from Sun')

    fig.set_size_inches(10, 10)
    plt.savefig("polar", dpi=300)
    return

if __name__ == '__main__':
    labels = 'Carbon', 'Metals', 'Silicon', 'Total weight of Earth'
    v = [1386868647.94871, 138927618.32884833, 133813134.13807245]
    #density in kg/m^3
    d = [2250, 12000, 2330]
    d = [e*1000000000*0.20 for e in d]
    w = [d[0]*v[0], d[1]*v[1], d[2]*v[2]]
    w.append(5.972e+24)
    fig = plt.figure(figsize= (10,5))
    plt.yscale('log')
    plt.bar(labels, w, width=0.4)
    plt.bar(labels, [0,0,0,0.30*w[3]], bottom=[0,0,0,0], width=0.4)
    plt.title("Mass Comparisons")
    plt.savefig("mass")
    exit(0)

