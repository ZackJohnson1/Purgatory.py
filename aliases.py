aliases = {
    "BP": "Barbell Bench Press",
    "Bench": "Barbell Bench Press",
    "Flat Bench": "Barbell Bench Press"
}

def resolve_alias(input_string):
    return aliases.get(input_string, input_string)

print(resolve_alias("BP")) # outputs "Barbell Bench Press"
print(resolve_alias("Bench")) # outputs "Barbell Bench Press"
print(resolve_alias("Flat Bench")) # outputs "Barbell Bench Press"
print(resolve_alias("Non-existing")) # outputs "Non-existing"
