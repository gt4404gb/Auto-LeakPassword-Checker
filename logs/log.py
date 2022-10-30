import time, os
import common_config

log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "result")
if not os.path.exists(log_dir):
    os.mkdir(log_dir)

date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
log_dir = os.path.join(log_dir,date)
if not os.path.exists(log_dir):
    os.mkdir(log_dir)

success_filename = os.path.join(log_dir, common_config.logConfig["success_filename"])
error_filename = os.path.join(log_dir, common_config.logConfig["error_filename"])
log_filename = os.path.join(log_dir, common_config.logConfig["log_filename"])
lock = {}
id = ''


def init_lock(l):
    global lock
    lock = l


def init_log_id(i):
    global id
    id = i


def get_time():
    return time.strftime('%Y-%m-%d %X', time.localtime(time.time()))


def write_log(filename, msg):
    if lock:
        with lock:
            with open(filename, "a+", encoding="UTF-8") as log:
                print(filename)
                log.write(msg + "\n")
    else:
        with open(filename, "a+", encoding="UTF-8") as log:
            log.write(msg + "\n")


def Info(msg):
    current_time = get_time()
    if id:
        msg = f"{current_time}  id: {id} {str(msg)}"
    else:
        msg = f"{current_time}  {str(msg)}"
    print(msg)
    write_log(log_filename, msg)


def Error(msg):
    current_time = get_time()
    if id:
        msg = f"{current_time}  id: {id} {str(msg)}"
    else:
        msg = f"{current_time}  {str(msg)}"
    print(msg)
    write_log(error_filename, msg)


def Success(msg):
    current_time = get_time()
    if id:
        msg = f"{current_time}  id: {id} {str(msg)}"
    else:
        msg = f"{current_time}  {str(msg)}"
    print(msg)
    write_log(success_filename, msg)
