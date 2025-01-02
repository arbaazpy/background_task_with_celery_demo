# Debugging Redis


```shell
(background-task-demo) ➜  background_task_demo git:(master) ✗ redis-server
3690:C 02 Jan 2025 13:31:00.438 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
3690:C 02 Jan 2025 13:31:00.438 # Redis version=7.0.15, bits=64, commit=00000000, modified=0, pid=3690, just started
3690:C 02 Jan 2025 13:31:00.438 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
3690:M 02 Jan 2025 13:31:00.439 * Increased maximum number of open files to 10032 (it was originally set to 1024).
3690:M 02 Jan 2025 13:31:00.439 * monotonic clock: POSIX clock_gettime
3690:M 02 Jan 2025 13:31:00.439 # Warning: Could not create server TCP listening socket *:6379: bind: Address already in use
3690:M 02 Jan 2025 13:31:00.439 # Failed listening on port 6379 (TCP), aborting.
```

## Steps to Fix
#### 1. Check if Redis is already running
```bash
ps aux | grep redis
```

#### 2. Stop the existing Redis process

```bash
sudo kill <PID>
```
Replace <PID> with the actual process ID of the running Redis instance. You can also use:

```bash
sudo systemctl stop redis
```

#### 3. Check if the port is in use
```bash
ss -tuln | grep 6379
```
If the port is in use, identify the application and terminate it if needed.

#### 4. Start Redis with a different port
```bash
redis-server --port 6380
```
**NOTE: Running redis in different port worked for me.**
