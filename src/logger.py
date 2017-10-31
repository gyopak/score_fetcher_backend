from datetime import datetime

def generate(level, message):
	log = {}
	log["time"] = str(datetime.now())
	log["level"] = level
	log["message"] = message
	return str(log)

def save_log(log):
	with open("log.txt", "a") as log_file:
		log_file.write(log + "\n")

def log(message, level = "INFO"):
	save_log(generate(level, message))