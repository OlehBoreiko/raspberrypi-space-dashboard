# Deploy Your Python App as a Linux Service with systemd

In this lecture, you learned how to create a systemd service to automatically run your Python project.

## Key Steps

1. Create a service file:

```bash
sudo nano /etc/systemd/system/project.service
```

2. Example project.service file:

```ini
[Unit]
Description=My Python Project
After=network.target

[Service]
ExecStart=/home/pi/project/venv/bin/python /home/pi/project/script.py
WorkingDirectory=/home/pi/project
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
```

> **Important:** If you see an error like `status=217/USER`, it means the system cannot find the specified user.  
> You can check your username with:
> ```bash
> whoami
> ```
> Then update the `User=` field accordingly, or remove the `User=` line if necessary.

3. Reload systemd to recognize the new service:

```bash
sudo systemctl daemon-reload
```

4. Start the service:

```bash
sudo systemctl start project.service
```

5. Enable the service on boot:

```bash
sudo systemctl enable project.service
```

6. Check service status:

```bash
sudo systemctl status project.service
```

7. View live logs:

```bash
journalctl -u project.service -f
```

---

> Replace `/home/pi/project/` with the correct path to your project if needed.
