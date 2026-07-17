# PageSpeed Optimization Template

Applied to [shawndo.com](https://github.com/taoofshawn/shawndo.com) — commit range `ef85c44..ea0601e`

## Files to create

### `.dockerignore`
```
.git/
.gitignore
README.md
.hugo_build.lock
Dockerfile
.dockerignore
public/
resources/
```

### `nginx.conf`
```nginx
worker_processes auto;

events {
    worker_connections 1024;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    gzip on;
    gzip_static on;  # serve pre-compressed .gz files
    gzip_vary on;
    gzip_proxied any;
    gzip_comp_level 6;
    gzip_min_length 256;
    gzip_types
        text/html text/plain text/css text/javascript
        application/javascript application/json application/xml
        image/svg+xml font/ttf font/otf;

    server_tokens off;

    server {
        listen 80;
        root /usr/share/nginx/html;
        index index.html;

        # Cache fingerprinted assets 1y
        location ~* \.(css|js)$ {
            expires 1y;
            add_header Cache-Control "public, immutable";
        }

        # Cache images 30d
        location ~* \.(jpg|jpeg|png|gif|ico|webp|avif|svg)$ {
            expires 30d;
            add_header Cache-Control "public, immutable";
        }

        # HTML: no cache
        location / {
            expires -1;
            add_header Cache-Control "no-cache, must-revalidate";
            try_files $uri $uri/ =404;
        }
    }
}
```

### `scripts/add-img-dimensions.py`
Full script at `scripts/add-img-dimensions.py` in the shawndo.com repo.
- Reads JPEG SOF0 marker / PNG IHDR chunk (no PIL needed)
- Injects `width`/`height` attributes on `<img>` tags in Hugo-minified HTML
- Resolves paths from `static/` directory

### Dockerfile structure
```dockerfile
FROM alpine:3.21 AS builder
WORKDIR /src
RUN apk add --no-cache --repository=https://dl-cdn.alpinelinux.org/alpine/edge/community \
    hugo jpegoptim optipng python3
COPY . .
# Optimize images
RUN find static -type f \( -iname '*.jpg' -o -iname '*.jpeg' \) -print0 | xargs -0 jpegoptim --strip-all --max=85
RUN find static -type f -iname '*.png' -print0 | xargs -0 optipng -o3
# Build
RUN hugo --minify
# Lazy load + dimensions
RUN find public -name '*.html' -exec sed -i 's|<img |<img loading="lazy" |g' {} +
RUN python3 scripts/add-img-dimensions.py public
# Pre-compress for gzip_static
RUN find public -type f \( -name '*.html' -o -name '*.css' -o -name '*.js' \) -exec gzip -kf {} +

FROM nginx:1.27-alpine AS runner
COPY --from=builder /src/public /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
```

## CSS Accessibility fixes

- **Color contrast**: For text on dark backgrounds, ensure ≥4.5:1 (normal) or ≥3:1 (large/bold). Test with [webaim.org/contrastchecker](https://webaim.org/contrastchecker/)
- **Metadata text**: `#999` on white fails (2.84:1). Use `#666` or darker (≥4.5:1)
- **Form controls**: Always add `aria-label` to checkbox inputs used as toggles

## SEO fixes

- Add `<meta name="description" content="...">` to `<head>`
- Use Hugo's `.Description` → `.Summary` → `site.Params.siteDescription` fallback chain

## PSI API testing

```bash
KEY="your-api-key"
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=SITE_URL&strategy=mobile&key=$KEY&category=PERFORMANCE&category=ACCESSIBILITY&category=BEST_PRACTICES&category=SEO"
```

Available categories: `PERFORMANCE`, `ACCESSIBILITY`, `BEST_PRACTICES`, `SEO`

## Deployment loop

```bash
# After push:
kubectl -n external rollout restart deployment/YOUR_DEPLOYMENT
kubectl -n external rollout status deployment/YOUR_DEPLOYMENT --timeout=120s
```
