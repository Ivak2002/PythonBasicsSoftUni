users = {}
submissions = {}

while True:
    line = input()
    if line == "exam finished":
        break

    parts = line.split("-")

    if parts[1] == "banned":
        user = parts[0]
        if user in users:
            users.pop(user)
    else:
        user, lang, pts = parts[0], parts[1], int(parts[2])
        submissions[lang] = submissions.get(lang, 0) + 1

        if user not in users:
            users[user] = pts
        else:
            users[user] = max(users[user], pts)

print("Results:")
for user, pts in users.items():
    print(f"{user} | {pts}")

print("Submissions:")
for lang, count in submissions.items():
    print(f"{lang} - {count}")
