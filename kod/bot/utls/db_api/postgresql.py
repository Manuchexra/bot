import psycopg2
from psycopg2 import OperationalError

def create_connection():
    """Create and return a new database connection."""
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="manushka07",
            database="Marafon",  
            port="5432",
            host="127.0.0.1"
        )
        return connection
    except OperationalError as e:
        print(f"Error while connecting to PostgreSQL: {e}")
        return None

def execute_command(command):
    """Execute a database command and return the results."""
    connection = create_connection()
    if connection is None:
        return None
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(command)
            results = cursor.fetchall()
            connection.commit()
            return results
    except Exception as e:
        print(f"Error executing command: {e}")
        return None
    finally:
        connection.close()

# Example usage
if __name__ == "__main__":
    command = "SELECT * FROM Marafon;" 
    results = execute_command(command)
    if results is not None:
        for row in results:
            print(row)
