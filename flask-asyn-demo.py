import flask
from flask import Flask, request, jsonify
from aiohttp import web

#ab -c 300 -n 10000 http://127.0.0.1:5000/
#https://www.jianshu.com/p/eda9fd632764

async def index(request):
    return web.Response(text='Hello World')

async def api(request):
    data = await request.json()
    question = data['question']
    question_analysis = await get_question_analysis(question)
    return web.json_response(question_analysis)

app = web.Application()
app.add_routes([web.get('/', index),
                web.post('/api', api)])

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=5000)