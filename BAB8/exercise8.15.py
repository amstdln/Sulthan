def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        design = unprinted_designs.pop()
        print(f"Mencetak desain: {design}")
        completed_models.append(design)

def show_completed_models(completed_models):
    print("\nDesain yang sudah dicetak:")
    for model in completed_models:
        print(model)

unprinted_designs = ["model HP", "model laptop", "model tablet"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)