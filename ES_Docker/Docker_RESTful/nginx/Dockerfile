
# https://basketdeveloper.tistory.com/66

FROM nginx:1.17.4

COPY default.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]

# docker build -t nginx/swagger .
# docker run --name nginx -p 80:80 nginx/swagger