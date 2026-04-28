data = {
    "company": {
        "employees": [
            {"name": "Ali", "skills": ["Python", "Django"]},
            {"name": "Sara", "skills": ["React", "JS"]}
        ]
    }
}

skill = data['company']['employees']

for i in skill:
	for j in i["skills"]:
		print(j)

	