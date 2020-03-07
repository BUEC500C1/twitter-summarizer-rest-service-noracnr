# HW5:twitter-summarizer-rest-service-noracnr

### How to use
* clone this repository and prepare a series of packages written in requirements.txt.
* At first, open a bash and run:
```bash
python3 restApi.py
```
* Then, open another bash and run:
```bash
curl http://127.0.0.1:5000/ -d "keyword=italy" -X POST
```
You can change 'italy' to any keyword. Here is the result of this command line:
![post_result](/img/restapiPost.png)
