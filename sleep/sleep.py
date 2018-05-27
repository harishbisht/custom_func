from datetime import datetime

def sleep(seconds):
	start_time = datetime.now()
	while (datetime.now() - start_time ).seconds < seconds:
		continue
	return