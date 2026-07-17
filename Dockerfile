FROM alpine:3.21 AS builder

WORKDIR /src
RUN apk add --no-cache --repository=https://dl-cdn.alpinelinux.org/alpine/edge/community hugo
COPY . .
RUN hugo --minify

FROM nginx:1.27-alpine AS runner
COPY --from=builder /src/public /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
