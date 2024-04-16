import sqlite3
import csv
import os

class DatabaseExporter:
    def __init__(self, database_file):
        self.database_file = database_file

    def export_to_csv(self):
        # Get the current working directory
        cwd = os.getcwd()

        # Connect to the database
        conn = sqlite3.connect(self.database_file)
        cursor = conn.cursor()

        # Get the list of tables in the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        # Create a folder to store CSV files if it doesn't exist in the current directory
        folder_name = './data/csv_files'
        csv_folder_path = os.path.join(cwd, folder_name)
        if not os.path.exists(csv_folder_path):
            os.makedirs(csv_folder_path)

        # Iterate over each table
        for table in tables:
            table_name = table[0]
            csv_file_path = os.path.join(csv_folder_path, f"{table_name}.csv")

            # Fetch all rows from the table
            cursor.execute(f"SELECT * FROM {table_name};")
            rows = cursor.fetchall()

            # Get column names
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            column_names = [col[1] for col in columns]

            # Write rows to CSV file
            with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(column_names)
                csv_writer.writerows(rows)

            print(f"Table '{table_name}' exported to '{csv_file_path}'")

        # Close database connection
        conn.close()

# Main function to run the script
def main():
    # Replace 'vivino.db' with your database file path
    database_file = 'data/vivino.db'

    # Create DatabaseExporter instance
    exporter = DatabaseExporter(database_file)

    # Export database to CSV files
    exporter.export_to_csv()

# Entry point of the script
if __name__ == "__main__":
    main()