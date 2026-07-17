#!/usr/bin/env python3
"""
Add explicit width and height attributes to <img> tags in HTML files.
This prevents Cumulative Layout Shift (CLS) by reserving image space.

Scans public/ for HTML files, finds <img> tags without dimensions,
looks up the image file to get its actual dimensions, and injects them.
"""

import os
import re
import struct
import sys

PUBLIC_DIR = sys.argv[1] if len(sys.argv) > 1 else 'public'

def get_jpeg_size(filepath):
    """Get JPEG dimensions by reading the SOF marker."""
    with open(filepath, 'rb') as f:
        data = f.read(1024 * 10)  # Read enough to get SOF
    # Find SOF0 marker (0xFF 0xC0)
    i = 0
    while i < len(data) - 1:
        if data[i] == 0xFF and data[i+1] == 0xC0:
            height = struct.unpack('>H', data[i+5:i+7])[0]
            width = struct.unpack('>H', data[i+7:i+9])[0]
            return width, height
        i += 1
    return None, None

def get_png_size(filepath):
    """Get PNG dimensions from IHDR chunk."""
    with open(filepath, 'rb') as f:
        f.read(8)  # Skip PNG signature
        data = f.read(8)  # IHDR chunk header + width/height
        if len(data) >= 8:
            width = struct.unpack('>I', data[4:8])[0]
            height = struct.unpack('>I', data[8:12])[0]
            return width, height
    return None, None

def get_image_size(filepath):
    """Get image dimensions based on file type."""
    if not os.path.exists(filepath):
        return None, None
    ext = os.path.splitext(filepath)[1].lower()
    if ext in ('.jpg', '.jpeg'):
        return get_jpeg_size(filepath)
    elif ext == '.png':
        return get_png_size(filepath)
    return None, None

def add_dimensions_to_html(html_path, static_dir):
    """Add width/height to <img> tags missing them."""
    with open(html_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    def replace_img(match):
        full_tag = match.group(0)
        # Skip if already has width or height
        if re.search(r'\b(width|height)\s*=', full_tag):
            return full_tag
        
        # Extract src
        src_match = re.search(r'src=["\']([^"\']+)["\']', full_tag)
        if not src_match:
            return full_tag
        
        src = src_match.group(1)
        # Map HTML src back to static file path
        # Static files are served at /, so /images/foo.jpg -> static/images/foo.jpg
        if src.startswith('/'):
            img_path = os.path.join(static_dir, src.lstrip('/'))
        else:
            # Relative path - resolve relative to HTML file
            img_path = os.path.join(os.path.dirname(html_path), src)
        
        w, h = get_image_size(img_path)
        if w and h:
            # Add width and height before the closing >
            tag = full_tag.rstrip()
            if tag.endswith('/>'):
                tag = tag[:-2] + f' width="{w}" height="{h}" />'
            elif tag.endswith('>'):
                tag = tag[:-1] + f' width="{w}" height="{h}">'
            return tag
        return full_tag
    
    # Match <img ...> tags
    new_content = re.sub(r'<img[^>]+>', replace_img, content)
    
    if new_content != content:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    static_dir = os.path.join(os.path.dirname(PUBLIC_DIR), 'static')
    if not os.path.exists(static_dir):
        # Try relative to current dir
        static_dir = 'static'
    
    modified = 0
    for root, dirs, files in os.walk(PUBLIC_DIR):
        for fname in files:
            if fname.endswith('.html'):
                path = os.path.join(root, fname)
                if add_dimensions_to_html(path, static_dir):
                    modified += 1
                    rel = os.path.relpath(path, PUBLIC_DIR)
                    print(f'  Augmented: {rel}')
    
    print(f'Modified {modified} HTML files')

if __name__ == '__main__':
    main()
