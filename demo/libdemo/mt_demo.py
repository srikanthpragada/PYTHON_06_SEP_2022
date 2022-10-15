import threading


class ChildThread(threading.Thread):
    def run(self):
        for n in range(10):
            print(f"Child {n}")


print(threading.current_thread())
ct = ChildThread()
ct.start()
print(threading.active_count())
for n in range(10):
    print(f"Main {n}")