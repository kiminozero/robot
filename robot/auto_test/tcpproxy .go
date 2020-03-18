package main

import (
"flag"
"fmt"
"os"
"net"
"encoding/hex"
)

func usage() {
s := `
a tcp proxy util
tcpproxy -localhost 127.0.0.1 -localport 9000 -remotehost 192.168.1.2 -remoteport 80
-localhost 127.0.0.1 default is 0.0.0.0 - listen on [localhost]:[localport] for incoming connections
-localport
-remotehost
-remoteport redirect incomming connection to [remotehost]:[remoteport]

Examples:
tcpproxy -localhost 0.0.0.0 -localport 9000 -remotehost 20.3.3.3 -remoteport 80

browser open http://127.0.0.1:9000 is the same as open http://20.3.3.3:80

`
fmt.Println(s)
os.Exit(0)
}

//send all received data to my client
func remoteConnHandler(rc, lc net.Conn) {
buf := make([]byte, 4096)
for {
n, err := rc.Read(buf)
if err != nil {
break
}
if n > 0 {
fmt.Printf("[<==] Sending %d bytes to localhost.\n", n)
hex.Dump(buf[:n])
lc.Write(buf[:n])
}
}
fmt.Println("[*] Closing remote connection...")
rc.Close()
lc.Close()
}
//first connect to remote server
//then send all received data to remote server
func localConnHandler(c net.Conn, remoteHost string, remotePort int) {
rc, err := net.Dial("tcp", fmt.Sprintf("%s:%d", remoteHost, remotePort))
if err != nil {
fmt.Printf("connect to remote server failed!")
return
}
go remoteConnHandler(rc, c)
buf := make([]byte, 4096)
for {
n, err := c.Read(buf) // only proxy normal data, urgent data is ignored
if err != nil {
break
}
if n > 0 {
fmt.Printf("[==>] Received %d bytes from localhost.\n", n)
hex.Dump(buf[:n])
rc.Write(buf[:n])
}
}
fmt.Println("[*] close local connection...")
//duplicat close is ok
rc.Close()
c.Close()
}
func serverLoop(localHost string, localPort int, remoteHost string, remotePort int) {
listener, err := net.Listen("tcp", fmt.Sprintf("%s:%d", localHost, localPort))
if err != nil {
fmt.Errorf("listen on port %d error\n", localPort)
return
}
fmt.Printf("Listenging on %s:%d \n", localHost, localPort)
for {
conn, err := listener.Accept()
if err != nil {
fmt.Errorf("accept error:", err)
break
}
fmt.Printf("[==>] Received incoming connection from %s\n", conn.RemoteAddr())
go localConnHandler(conn, remoteHost, remotePort)
}
}
func main() {
var (
localHost string
localPort int
remoteHost string
remotePort int
)

flag.StringVar(&localHost, "localhost", "0.0.0.0", "listening local ip")
flag.StringVar(&remoteHost, "remotehost", "", "remote host address")
flag.IntVar(&localPort, "localport", 0, "listening local port")
flag.IntVar(&remotePort, "remoteport", 0, "remote host's port to connect")
flag.Parse()
if len(remoteHost) <= 0 || localPort == 0 || remotePort == 0 {
usage()
}
serverLoop(localHost, localPort, remoteHost, remotePort)
}