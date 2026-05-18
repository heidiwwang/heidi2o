import os
import re
import shutil
from pathlib import Path

# --- CONFIGURATION ---
OBSIDIAN_VAULT = Path('/home/hide/Documents/heidi2o/03_lab/')
OBSIDIAN_ATTACHMENTS = Path('/home/hide/Documents/heidi2o/02_library/attachments')
QUARTZ_CONTENT = Path('/home/hide/quartz/content')
QUARTZ_ATTACHMENTS = QUARTZ_CONTENT / "assets"

NOTE_FILENAME = "baby_guide.md"

def process_content(content):
    # 1. Update YAML title from H1 (Existing Logic)
    h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if h1_match:
        h1_text = h1_match.group(1).strip()
        content = re.sub(r'^#\s+.+$\n?', '', content, count=1, flags=re.MULTILINE)
        if re.search(r'^title:.*$', content, re.MULTILINE):
            content = re.sub(r'^title:.*$', f'title: "{h1_text}\n"', content, flags=re.MULTILINE)
        else:
            content = re.sub(r'^---', f'---\ntitle: "{h1_text}\n"', content, count=1)

    # 2. TRANSFORM ![[image.png|caption]] to <figure>
    # Regex breakdown: !\[\[  (Filename)  (?:\|  (Caption))?  \]\]
    def figure_replacement(match):
        filename = match.group(1).split('|')[0].strip()
        # Check if there's a caption after the pipe
        parts = match.group(1).split('|')
        caption = parts[1].strip() if len(parts) > 1 else ""

        if caption:
            return (
                f'<figure>\n'
                f'  <img src="/assets/{filename}" alt="{caption}">\n'
                f'  <figcaption>{caption}</figcaption>\n'
                f'</figure>\n'
            )
        else:
            # Fallback for images without captions
            return f'<img src="/assets/{filename}" alt="{filename}">'

    # Apply the replacement to all wikilink images
    content = re.sub(r'!\[\[(.*?)\]\]', figure_replacement, content)
            
    return content

def copy_to_quartz(note_name):
    note_matches = list(OBSIDIAN_VAULT.rglob(note_name))
    if not note_matches:
        print(f"❌ Error: {note_name} not found.")
        return
    
    source_path = note_matches[0]
    QUARTZ_CONTENT.mkdir(parents=True, exist_ok=True)
    QUARTZ_ATTACHMENTS.mkdir(parents=True, exist_ok=True)

    with open(source_path, 'r', encoding='utf-8') as f:
        raw_content = f.read()

    # Find attachments BEFORE transforming content to HTML
    # We need the filenames to copy the actual files
    attachment_links = re.findall(r'!\[\[(.*?)\]\]', raw_content)

    # Transform content (H1 to Title AND Images to Figures)
    updated_content = process_content(raw_content)

    with open(QUARTZ_CONTENT / note_name, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print(f"✅ Note processed and copied: {note_name}")

    # Copy actual image files
    for link in attachment_links:
        asset_name = link.split('|')[0].strip()
        src_asset = OBSIDIAN_ATTACHMENTS / asset_name
        
        if not src_asset.exists():
            fallback = list(OBSIDIAN_ATTACHMENTS.rglob(asset_name))
            src_asset = fallback[0] if fallback else None

        if src_asset and src_asset.exists():
            shutil.copy2(src_asset, QUARTZ_ATTACHMENTS / asset_name)
            print(f"   📎 Attachment copied: {asset_name}")

if __name__ == "__main__":
    copy_to_quartz(NOTE_FILENAME)