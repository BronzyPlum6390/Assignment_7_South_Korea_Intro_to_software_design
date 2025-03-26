students = {}
    
for i in range(3):
    user_input = input()
    name, score = user_input.split()
    students[name] = int(score)
    
print("Which student's score?")
query_name = input()
    
if query_name in students:
    print(f"{query_name}'s score: {students[query_name]}")
else:
    print(f"{query_name} is not in the database.")
