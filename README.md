# Setup
## Installing packages
### 1. create virtual environment and activate
```bash
uv venv
source .venv/bin/activate
```
### 2. Install dependencies
```bash
uv sync
```
or 
```
uv pip install -r pyproject.toml
```

## Running project
### 1. Run migration
```bash
python manage.py migrate
```
### 2. Run server
```
python manage.py runserver
```
### 3. Run celery
```bash
celery -A background_task_demo worker --loglevel=info
```
### 4. Create superuser to access admin site (optional)
```bash
python manage.py createsuperuser
```
### 5. Open server
Server wil be running on `http://127.0.0.1:8000/` \
Access admin site at `http://127.0.0.1:8000/admin`


## Access APIs
### 1. Create user
`POST http://127.0.0.1:8000/api/user/create/`
```json
{
    "first_name": "John",
    "last_name": "Doe"
}
```


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
