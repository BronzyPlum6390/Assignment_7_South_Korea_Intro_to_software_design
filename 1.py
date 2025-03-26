
def create_multiplication_tables():
    multiplication_tables = {}
    
    for num in range(2, 10, 2):
        table = []
        
        for i in range(1, 10):
            table.append(num * i)
        
        multiplication_tables[num] = table
    
    return multiplication_tables

tables = create_multiplication_tables()
print(tables)

