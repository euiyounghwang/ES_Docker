

# 172.17.0.1 - - [16/Jul/2022:16:48:22 +0000] "POST /interface HTTP/1.1" 200 65 "http://localhost:8001/docs" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36" "-"
# %{IPORHOST:clientip} (?:-|(%{WORD}.%{WORD})) %{USER:ident} \[%{HTTPDATE:timestamp}\] "(?:%{WORD:verb} %{NOTSPACE:request}(?: HTTP/%{NUMBER:httpversion})?|%{DATA:rawrequest})" %{NUMBER:response} (?:%{NUMBER:bytes}|-) %{QS:referrer} %{QS:agent} %{QS:forwarder}

# {
#   "request": "/interface",
#   "agent": "\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36\"",
#   "ident": "-",
#   "verb": "POST",
#   "referrer": "\"http://localhost:8001/docs\"",
#   "response": "200",
#   "bytes": "65",
#   "clientip": "172.17.0.1",
#   "forwarder": "\"-\"",
#   "httpversion": "1.1",
#   "timestamp": "16/Jul/2022:16:48:22 +0000"
# }

# https://basketdeveloper.tistory.com/66

FROM nginx:1.17.4

COPY default.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]

# docker build -t nginx/swagger .
# docker run --name nginx -p 80:80 nginx/swagger