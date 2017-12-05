import json
json_str = '''{
  "age": 18,
  "name": "herry",
  "favotite": ["ping pong", "basket ball", "video game"],
  "2017-12-01 12:00:01": "do some work"
}'''

ret_d = json.loads(json_str)
print ret_d
