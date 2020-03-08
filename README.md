# HW5:twitter-summarizer-rest-service-noracnr
https://noracnr.github.io/twitter-summarizer-rest-service-noracnr/
### How to use
EC2 server: ec2-3-133-92-223.us-east-2.compute.amazonaws.com:8080
1. clone this repository and prepare a series of packages written in requirements.txt.
2. At first, open a bash and run:
```bash
python3 restApi.py
```
3. Then, open another bash and run:
```bash
curl -X POST -d "keyword=covid19" http://ec2-3-133-92-223.us-east-2.compute.amazonaws.com:8080/
```
* You can change 'milano' to any keyword. Here is the result of this command line:
```json
{
  "get_status": "3.133.92.223:8080/status/covid19", 
  "get_video": "3.133.92.223:8080/video/covid19", 
  "keyword": "covid19"
}
```
* You can check the status of twitter summarizer like this.
```bash
 curl http://ec2-3-133-92-223.us-east-2.compute.amazonaws.com:8080/status/milano
```
```json
{
  "error": "", 
  "keyword": "covid19", 
  "status": "finished"
}
```
* Also, watch the video in a browser when you type '3.133.92.223:8080/video/covid19' in the address bar. Like that,
  ![video](/img/restapiVideo1.png)
