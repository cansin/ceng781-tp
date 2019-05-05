# CENG 781 - Network Security - Term Project

Let's compile `blindbox.p4` and bring
up a switch in Mininet to test its behavior.

1. In your shell, run:
   ```
   pip install -r requirements.txt
   ```
   This will install the dependencies needed for the project.

2. In your shell, run:
   ```bash
   make run
   ```
   This will:
   * compile `blindbox.p4`, and
   * start a Mininet instance with a single switch (`s1`), connecting three hosts  
     (`h1`, and `h2`).
   * The hosts are assigned IPs of `10.0.1.1`, and `10.0.2.2`.

3. You should now see a Mininet command prompt. Open two terminals
for `h1` and `h2`, respectively:
   ```bash
   mininet> xterm h1 h2
   ```
4. Each host includes a small Python-based messaging client and
server. In `h2`'s xterm, start the server:
   ```bash
   python -m client.receiver
   ```
5. In `h1`'s xterm, send a message to `h2`:
   ```bash
   python -m client.sender "This is a safe message."
   ```
   The message will be received. 
6. In `h1`'s xterm, send a message to `h2`:
   ```bash
   python -m client.sender "This is a malicious message."
   ```
   The message will be received but will be marked as _malicious_. 
7. Type `exit` to leave each xterm and the Mininet command line.
   Then, to stop mininet:
   ```bash
   make stop
   ```
   And to delete all pcaps, build files, and logs:
   ```bash
   make clean
   ```

#### Cleaning up Mininet

In the latter two cases above, `make run` may leave a Mininet instance
running in the background. Use the following command to clean up
these instances:

```bash
make stop
```


