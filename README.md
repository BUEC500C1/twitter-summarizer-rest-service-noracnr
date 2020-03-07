# HW5:twitter-summarizer-rest-service-noracnr

### How to use
1. clone this repository and prepare a series of packages written in requirements.txt.
2. At first, open a bash and run:
```bash
python3 restApi.py
```
3. Then, open another bash and run:
```bash
curl http://127.0.0.1:5000/ -d "keyword=italy" -X POST
```
* You can change 'italy' to any keyword. Here is the result of this command line:
   ![post_result](/img/restapiPost.png)
* You can check the status of twitter summarizer like this.
```bash
 curl http://127.0.0.1:5000/status/italy
```

   ![status](/img/restapiStatus.png)
* Also, watch the video in a browser when you type http://127.0.0.1:5000/video/italy in the address bar. Like that,
  ![video](/img/restapiVideo.png)
