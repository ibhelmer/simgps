# simgps
socat -d -d pty,raw,echo=0 pty,raw,echo=0
sudo socat -d -d pty,link=/dev/ttyS2,raw,echo=0 pty,link=/dev/ttyS3,raw,echo=0
