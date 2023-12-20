from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='localhost', port=6379)

@app.route('/')
def testwithredis():
    redis.incr('hits')
    return 'Nombre de visites : {}'.format(redis.get('hits').decode('utf-8'))

if __name__ == '__main__':
    app.run(debug=True)
