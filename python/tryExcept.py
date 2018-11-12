try:
	f = open('file194.txt')
	if f.name == 'file194.txt':
		raise Exception
except FileNotFoundError as e:
	print(e)
except Exception as e:
	print('Testing...')
else: 
	print(f.read())
	f.close()
finally:
	print("Executing Finally...")