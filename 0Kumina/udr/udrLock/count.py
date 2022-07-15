from pathlib import Path

with Path("activation.iac") as file:
	text = file.read_text()
	print(len(text))
	input()
