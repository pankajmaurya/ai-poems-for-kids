# FlaskyGPT Playground

Make sure to fix your api keys in 2 places
1. Fix openai key in initopenai.py 
2. and eleven labs api in static/listen.js

## Local Dev

```
Pankajs-MacBook-Pro:pythonanywhere pankaj$ flask --app flask_app run
```

Check Health
```
curl http://localhost:5000/healthz
OK
```

Echo payload
```
curl -X POST -H "Content-Type: application/json" -d '{"code": "print(\"Hello, world\")"}' http://localhost:5000/echo
{"code":"print(\"Hello, world\")"}
```

Get analysis hints
```
curl -X POST -H "Content-Type: application/json" -d '{"code": "print(\"Hello, world\")"}' http://localhost:5000/analyze
{"hints":["Consider using a 'for' loop to iterate over elements.","Consider using an 'if' statement to add conditional logic."]}
```

### Misc Resources

https://api.elevenlabs.io/docs
https://openai.com/
