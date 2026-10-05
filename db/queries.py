def safe_query(conn, query, params):
    return conn.execute(query, params)
