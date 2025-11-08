materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
obtained = ""

while not obtained:
    parts = input().split()
    for i in range(0, len(parts), 2):
        qty = int(parts[i])
        mat = parts[i+1].lower()

        if mat in materials:
            materials[mat] += qty
            if materials[mat] >= 250 and not obtained:
                materials[mat] -= 250
                if mat == "shards":
                    obtained = "Shadowmourne"
                elif mat == "fragments":
                    obtained = "Valanyr"
                else:
                    obtained = "Dragonwrath"
                break
        else:
            junk[mat] = junk.get(mat, 0) + qty

print(f"{obtained} obtained!")

print(f"shards: {materials['shards']}")
print(f"fragments: {materials['fragments']}")
print(f"motes: {materials['motes']}")

for item, qty in junk.items():
    print(f"{item}: {qty}")
