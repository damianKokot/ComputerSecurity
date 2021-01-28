http:
Server Software:        
Server Hostname:        localhost
Server Port:            443
TLS Server Name:        localhost

Document Path:          /
Document Length:        0 bytes

Concurrency Level:      10
Time taken for tests:   0.059 seconds
Complete requests:      100
Failed requests:        0
Total transferred:      0 bytes
HTML transferred:       0 bytes
Requests per second:    1705.06 [#/sec] (mean)
Time per request:       5.865 [ms] (mean)
Time per request:       0.586 [ms] (mean, across all concurrent requests)
Transfer rate:          0.00 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     0    1   0.3      0       2
Waiting:        0    0   0.0      0       0
Total:          0    1   0.3      0       2
ERROR: The median and mean for the processing time are more than twice the standard
       deviation apart. These results are NOT reliable.
ERROR: The median and mean for the total time are more than twice the standard
       deviation apart. These results are NOT reliable.

Percentage of the requests served within a certain time (ms)
  50%      0
  66%      1
  75%      1
  80%      1
  90%      1
  95%      1
  98%      1
  99%      2
 100%      2 (longest request)

https:
Server Software:        
Server Hostname:        localhost
Server Port:            443
SSL/TLS Protocol:       TLSv1.2,ECDHE-RSA-AES128-GCM-SHA256,2048,128
Server Temp Key:        X25519 253 bits
TLS Server Name:        localhost

Document Path:          /
Document Length:        12 bytes

Concurrency Level:      10
Time taken for tests:   0.194 seconds
Complete requests:      100
Failed requests:        0
Total transferred:      8700 bytes
HTML transferred:       1200 bytes
Requests per second:    515.62 [#/sec] (mean)
Time per request:       19.394 [ms] (mean)
Time per request:       1.939 [ms] (mean, across all concurrent requests)
Transfer rate:          43.81 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        6   11   3.0     10      23
Processing:     2    5   1.9      5       9
Waiting:        1    2   1.3      2       8
Total:         12   17   2.7     16      25

Percentage of the requests served within a certain time (ms)
  50%     16
  66%     17
  75%     18
  80%     19
  90%     21
  95%     22
  98%     23
  99%     25
 100%     25 (longest request)
