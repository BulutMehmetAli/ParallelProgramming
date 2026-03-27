import psutil

def list_processes():
    print(f"{'PID':<10} {'NAME':<30} {'STATUS':<15} {'CPU%':<8} {'MEM (MB)':<10}")
    print("-" * 75)
    counter = 0
    for proc in psutil.process_iter(['pid', 'name', 'status', 'cpu_percent', 'memory_info']):
        try:
            counter += 1
            pid    = proc.info['pid']
            name   = proc.info['name']
            status = proc.info['status']
            cpu    = proc.info['cpu_percent']
            mem_mb = proc.info['memory_info'].rss / (1024 * 1024)

            print(f"{pid:<10} {name:<30} {status:<15} {cpu:<8.1f} {mem_mb:<10.1f}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    print(counter)

if __name__ == '__main__':
    list_processes()
