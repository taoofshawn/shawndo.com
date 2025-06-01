FROM alpine:latest as builder

WORKDIR /hugo
RUN doas apk add --no-cache --repository=https://dl-cdn.alpinelinux.org/alpine/edge/community git hugo && \
  git clone git@github.com:taoofshawn/shawndo.com.git /hugo && \
  hugo 

FROM nginx:latest as runner
COPY --from=builder /hugo/public /usr/share/nginx/html
