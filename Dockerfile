FROM alpine:3.21 AS builder

WORKDIR /src

# Install Hugo, image optimization tools, and ImageMagick for resizing
RUN apk add --no-cache --repository=https://dl-cdn.alpinelinux.org/alpine/edge/community \
    hugo \
    imagemagick \
    jpegoptim \
    optipng

COPY . .

# Resize overly large images to max 1200px wide (content area ~800px, 1200px covers retina)
RUN find static -type f \( -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.png' \) \
    -exec sh -c 'for f; do w=$(identify -format "%w" "$f"); [ "$w" -gt 1200 ] && convert "$f" -resize "1200>" -quality 85 "$f"; done' _ {} +

# Strip metadata and compress JPEGs to quality 85
RUN find static -type f \( -iname '*.jpg' -o -iname '*.jpeg' \) -exec jpegoptim --strip-all --max=85 {} +

# Optimize PNGs
RUN find static -type f -iname '*.png' -exec optipng -o3 {} +

# Build site
RUN hugo --minify

# Add loading="lazy" to all content images in HTML output
RUN find public -name '*.html' -exec sed -i 's|<img |<img loading="lazy" |g' {} +

# Pre-compress text assets for nginx gzip_static (serves .gz without runtime cost)
RUN find public -type f \( -name '*.html' -o -name '*.css' -o -name '*.js' \) -exec gzip -kf {} +

FROM nginx:1.27-alpine AS runner
COPY --from=builder /src/public /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
