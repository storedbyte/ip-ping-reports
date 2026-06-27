# IP Ping Reports

---

This is just my first python project I made on my own. It's nothing great, but I learned a lot while making this.

If you are ever in the need to ping a list of IP addresses and want the reachable status and ping exported to a text file, then this will do exactly that and nothing more.

---

## Usage

Run the script:
```
python script.py
```

When prompted, enter the path to your IP address list. The file should contain only one IP address per line:
```
10.0.0.1
10.0.0.2
10.0.0.3
...
```

---

## Example Output

```
10.0.0.1 | ONLINE | Ping(ms): 0.182

10.0.0.2 | ONLINE | Ping(ms): 0.386

10.0.0.3 | OFFLINE

10.0.0.4 | OFFLINE
```

---

## Requirements

- Python 3

---

Thanks for checking this out!
