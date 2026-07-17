FROM alpine:3.21 AS builder

WORKDIR /src

# Install Hugo and image optimization tools
RUN apk add --no-cache --repository=https://dl-cdn.alpinelinux.org/alpine/edge/community \
    hugo \
    jpegoptim \
    optipng

COPY . .

# Strip metadata and compress JPEGs to quality 85
RUN find static -type f \( -iname '*.jpg' -o -iname '*.jpeg' \) -print0 | xargs -0 jpegoptim --strip-all --max=85

# Optimize PNGs
RUN find static -type f -iname '*.png' -print0 | xargs -0 optipng -o3

# Build site
RUN hugo --minify

# Add loading="lazy" to all content images in HTML output
RUN find public -name '*.html' -exec sed -i 's|<img |<img loading="lazy" |g' {} +

# Pre-compress text assets for nginx gzip_static
RUN find public -type f \( -name '*.html' -o -name '*.css' -o -name '*.js' \) -exec gzip -kf {} +

FROM nginx:1.27-alpine AS runner
COPY --from=builder /src/public /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
