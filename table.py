from operator import itemgetter


# Class Table is used to represent a table in a Relational Database
class Table:
    def __init__(self):
        self.rows = []

    # Sorts the Table's rows by the keys defined in columns_to_order_by
    def self_sort(self, columns_to_order_by):
        # Creates a list of functions to call
        comparers = [itemgetter(col) for col in columns_to_order_by]

        # comparer is the function that will be used as the basis for comparing the rows in the table
        def comparer(r):
            out = []
            # Go through each function in the comparers list and call that on the row, append it to a list / return
            for fn in comparers:
                out.append(fn(r))

            return out

        return sorted(self.rows, key=comparer)

    # Takes a dictionary and inserts it into the table's rows
    def insert_into(self, row):
        self.rows.append(row)

    # Returns the rows from the table based on the columns to display
    # columns_to_display: List of strings denoting the column names to output
    # columns_to_order_by: List of strings denoting the columns to order by
    def select(self, columns_to_display, columns_to_order_by):
        # Sort the Table's array of dictionaries
        sorted_list = self.self_sort(columns_to_order_by)

        # Now that the array of dictionaries is sorted, we can just grab the values we need
        output = []
        for row in sorted_list:
            values = []
            for column in columns_to_display:
                values.append(row[column])

            output.append(values)

        return output


# Testing the class
table = Table()

table.insert_into(row={"name": "Josh", "grade": 3.0, "age": 31, "eye": "brown"})
table.insert_into(row={"name": "Emily", "grade": 3.5, "age": 29, "eye": "hazel"})
table.insert_into(row={"name": "Josh", "grade": 3.5, "age": 30, "eye": "green"})
table.insert_into(row={"name": "Josh", "grade": 2.0, "age": 20, "eye": "red"})

result = table.select(
    columns_to_display=["grade", "age", "name"],
    columns_to_order_by=["name", "grade"])
print(result)