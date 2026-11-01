def make_sandwich(*fillings):
    print("\nIsi sandwich:")
    for filling in fillings:
        print(f"- {filling}")

make_sandwich("keju")
make_sandwich("daging", "selada")
make_sandwich("ayam", "tomat", "mayones")