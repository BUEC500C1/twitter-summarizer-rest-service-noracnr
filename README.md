# HW5:twitter-summarizer-rest-service-noracnr

### How to use
EC2 server: ec2-3-133-92-223.us-east-2.compute.amazonaws.com:8080
1. clone this repository and prepare a series of packages written in requirements.txt.
2. At first, open a bash and run:
```bash
python3 restApi.py
```
3. Then, open another bash and run:
```bash
curl -X POST -d "keyword=milano" http://ec2-3-133-92-223.us-east-2.compute.amazonaws.com:8080/
```
* You can change 'milano' to any keyword. Here is the result of this command line:
   ![post_result](/img/restapiPost.png)
* You can check the status of twitter summarizer like this.
```bash
 curl http://ec2-3-133-92-223.us-east-2.compute.amazonaws.com:8080/status/milano
```
   ![status](/img/restapiStatus.png)
* Also, watch the video in a browser when you type http://ec2-3-133-92-223.us-east-2.compute.amazonaws.com:8080/video/milano in the address bar. Like that,
  ![video](/img/restapiVideo.png)
